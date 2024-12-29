from telegram import Bot
import json
import time

def send_request_via_telegram(token, chat_id, request_data):
    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text=json.dumps(request_data))

def get_response_from_telegram(token, chat_id):
    bot = Bot(token=token)
    updates = bot.get_updates()
    for update in updates:
        if update.message and update.message.chat.id == chat_id:
            return json.loads(update.message.text)
    # Wait for a response
    time.sleep(5)
    updates = bot.get_updates()
    for update in updates:
        if update.message and update.message.chat.id == chat_id:
            return json.loads(update.message.text)
    return None
