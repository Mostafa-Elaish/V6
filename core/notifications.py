import requests, os
class TelegramBot:
    def __init__(self, settings):
        self.settings = settings
        self.token = self.settings.get('notifications.telegram_bot_token')
        self.chat_id = self.settings.get('notifications.telegram_chat_id')
    def send_alert(self, text):
        if not self.token or not self.chat_id:
            print('Telegram not configured. Alert:', text)
            return
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        try:
            requests.post(url, data={'chat_id': self.chat_id, 'text': text}, timeout=5)
        except Exception as e:
            print('Telegram send error', e)
