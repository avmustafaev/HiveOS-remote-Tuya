import os
from pathlib import Path

from dotenv import load_dotenv

""" Модуль подтягивает параметры настроек из файла .env
и загружает в переменные окружения, затем из переменных окружения 
инициализирует настройки в переменные модуля
"""


class GetEnvKeys(object):
    def __init__(self):
        load_dotenv()
        env_path = Path(".") / ".env"
        load_dotenv(dotenv_path=env_path)
        self.hiveos_apikey = os.getenv("HIVEOS_API")
        self.tuya_apikey = os.getenv("TUYA_API_KEY")
        self.tuya_apisecret = os.getenv("TUYA_API_SECRET")
        self.tuya_region = os.getenv("TUYA_REGION")
        self.tuya_device_id = os.getenv("TUYA_DEVICE_ID")
        self.telegram_chat_id = os.getenv("CHAT_ID")
        self.telegram_api = os.getenv("TELEGRAM_API")
        self.pause = int(os.getenv("PAUSE"))
        print(f"В настройках установлена пауза: {self.pause} секунд\n")


""""
heroku_host = os.getenv("HEROKU_HOST")
heroku_db = os.getenv("HEROKU_DB")
heroku_user = os.getenv("HEROKU_USER")
heroku_password = os.getenv("HEROKU_PASSWORD")
heroku_port = os.getenv("HEROKU_PORT")
"""
