import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from TelegramBot.models import User
import django
import os

# Включение логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Определение состояний разговора
NAME, LAST_NAME, POSITION, SAP_NUMBER, CONFIRM = range(5)

# Функция для начала разговора
def start(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    if UserData.objects.filter(user_id=user_id).exists():
        update.message.reply_text('Привет! Вы уже зарегистрированы.')
        return ConversationHandler.END
    else:
        update.message.reply_text('Привет! Как тебя зовут?')
        return NAME

# Функция для получения имени
def get_name(update: Update, context: CallbackContext) -> int:
    context.user_data['first_name'] = update.message.text
    update.message.reply_text('Какая у тебя фамилия?')
    return LAST_NAME

# Функция для получения фамилии
def get_last_name(update: Update, context: CallbackContext) -> int:
    context.user_data['last_name'] = update.message.text
    reply_keyboard = [['ПК', 'Сборщик', 'Адм', 'ДМ']]
    update.message.reply_text(
        'Выберите вашу должность:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return POSITION

# Функция для получения должности
def get_position(update: Update, context: CallbackContext) -> int:
    context.user_data['position'] = update.message.text
    update.message.reply_text('Введите ваш SAP(ТОРГ) номер магазина:')
    return SAP_NUMBER

# Функция для получения SAP номера
def get_sap_number(update: Update, context: CallbackContext) -> int:
    context.user_data['sap_number'] = update.message.text
    user_data = context.user_data
    confirmation_message = (
        f"Подтвердите ваши данные:\n"
        f"Имя: {user_data['first_name']}\n"
        f"Фамилия: {user_data['last_name']}\n"
        f"Должность: {user_data['position']}\n"
        f"SAP номер: {user_data['sap_number']}\n"
        f"Подтвердите (да/нет):"
    )
    update.message.reply_text(confirmation_message)
    return CONFIRM

# Функция для подтверждения данных
def confirm(update: Update, context: CallbackContext) -> int:
    if update.message.text.lower() == 'да':
        user_data = context.user_data
        UserData.objects.create(
            user_id=update.message.from_user.id,
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            position=user_data['position'],
            sap_number=user_data['sap_number']
        )
        update.message.reply_text('Ваши данные сохранены. Спасибо!')
    else:
        update.message.reply_text('Пожалуйста, начните заново. /start')
    return ConversationHandler.END

# Функция для отмены разговора
def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Отменено. /start для начала заново.')
    return ConversationHandler.END

def registration_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(Filters.text & ~Filters.command, get_name)],
            LAST_NAME: [MessageHandler(Filters.text & ~Filters.command, get_last_name)],
            POSITION: [MessageHandler(Filters.text & ~Filters.command, get_position)],
            SAP_NUMBER: [MessageHandler(Filters.text & ~Filters.command, get_sap_number)],
            CONFIRM: [MessageHandler(Filters.text & ~Filters.command, confirm)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
