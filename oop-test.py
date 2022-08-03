import os

from src.envkeys import GetEnvKeys
from src.hiveosapi import ConnectHiveOS
from src.sqlite3crud import ManageDB
from src.telegramka import ConnectTelegram
from src.tuya_api import ConnectTuya

keys = GetEnvKeys()
hiveos = ConnectHiveOS(keys.hiveos_apikey)
telegram = ConnectTelegram(keys.telegram_api, keys.telegram_chat_id)
db = ManageDB(os.path.join("db", "data.db"))
sockets = ConnectTuya(
    keys.tuya_region, keys.tuya_apikey, keys.tuya_apisecret, keys.tuya_device_id
)

farms_list = hiveos.getfarms()

if farms_list is None:
    print("🚫 Не могу установить соединение с сервером HiveOS")
    telegram.send('🚫 Не могу установить соединение с сервером HiveOS')
else:
    db.add("farms_id", farms_list, many=True)
