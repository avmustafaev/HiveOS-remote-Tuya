import envkeys
import hiveosapi
import tuya_api

keys = envkeys.GetKeys()
hiveos = hiveosapi.CloudApi(keys.hiveos_apikey)


mySockets = tuya_api.Sockets(
    keys.tuya_region, keys.tuya_apikey, keys.tuya_apisecret, keys.tuya_device_id
)


mySockets.getmySockets()
