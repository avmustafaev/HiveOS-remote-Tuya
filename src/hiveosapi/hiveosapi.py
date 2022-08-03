import requests


class ConnectHiveOS:
    def __init__(self, apikey=None):
        if apikey is None:
            raise ValueError("apikey is required")
        else:
            self.apikey = apikey
        if self.check_connect():
            print("Соединение с HiveOS API успешно установлено!")

    def getfarms(self):
        responce_list = []
        farms_json = self.get_farms_json()
        if farms_json is None:
            return farms_json
        for fa in farms_json:
            farm_name = fa["name"]
            farm_id = fa["id"]
            responce_list.append((farm_id, farm_name))
        return responce_list

    def getrigs(self):
        responce_dict = {}
        farmss = self.getfarms()
        for nm, idd in farmss.items():
            rigs_json = self.get_rigs_json(idd)
            for rigg in rigs_json:
                rig_name = rigg["name"]
                rig_id = rigg["id"]
                responce_dict[rig_name] = rig_id
        return responce_dict

    def get_api(self, request_part, jsoned=True):
        url = "https://api2.hiveos.farm/api/v2"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.apikey}",
        }

        url_full = f"{url}/{request_part}" if request_part != "" else url
        try:
            resp = requests.get(url_full, headers=headers)
        except requests.exceptions.ConnectionError:
            return None
        return resp.json() if jsoned else resp.ok

    def patch_api(self):
        pass

    def get_farms_json(self):
        resp = self.get_api("/account")
        return resp if resp is None else resp["farms"]

    def get_rigs_json(self, farms_id):
        resp = self.get_api(f"/farms/{farms_id}/workers/preview")
        return resp if resp is None else resp["data"]

    def check_connect(self):
        return self.get_api("/account/meta", jsoned=False)
