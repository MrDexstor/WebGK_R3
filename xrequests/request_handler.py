import json
import requests
from .telegram_bot import send_request_via_telegram, get_response_from_telegram

class RequestHandler:
    def __init__(self, config_path):
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)

    def send_request(self, method, url, headers=None, params=None):
        if self.config.get('use_telegram_bot'):
            return self._send_request_via_telegram(method, url, headers, params)
        else:
            return self._send_request_directly(method, url, headers, params)

    def _send_request_via_telegram(self, method, url, headers, params):
        request_data = {
            "method": method,
            "url": url,
            "headers": headers,
            "params": params
        }
        send_request_via_telegram(self.config['telegram_bot_token'], self.config['work_device_chat_id'], request_data)
        response = get_response_from_telegram(self.config['telegram_bot_token'], self.config['home_device_chat_id'])
        return response

    def _send_request_directly(self, method, url, headers, params):
        response = requests.request(method, url, headers=headers, params=params)
        return response
