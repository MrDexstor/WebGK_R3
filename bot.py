import logging, os, django
from telegram.ext import Updater
from Core.config import TELEGRAM_BOT_TOKEN
from telegram.registration.handler import registration_handler

# Настройка Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# Включение логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    # Создание Updater и передача ему токена вашего бота.
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Получение диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчика разговора
    dispatcher.add_handler(registration_handler())

    # Запуск бота
    updater.start_polling()

    # Ожидание завершения бота
    updater.idle()

if __name__ == '__main__':
    main()
