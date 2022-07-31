import envkeys
import hiveosapi
import telegramka
import tuya_api

keys = envkeys.GetEnvKeys()
hiveos = hiveosapi.CloudApi(keys.hiveos_apikey)
sender = telegramka.Telegramka(keys.telegram_api, keys.telegram_chat_id)
mySockets = tuya_api.Sockets(
    keys.tuya_region, keys.tuya_apikey, keys.tuya_apisecret, keys.tuya_device_id
)


mySockets.getmySockets()
