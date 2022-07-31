import requests


class Telegramka(object):
    def __init__(self, apikey, chatid):
        self.apikey = apikey
        self.chatid = chatid

    def send(self, message):
        requests.get(
            f"https://api.telegram.org/bot{self.apikey}/sendMessage?text={message}&chat_id={self.chatid}"
        )
