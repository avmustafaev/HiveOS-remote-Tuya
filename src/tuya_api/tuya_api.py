import tinytuya


class ConnectTuya(tinytuya.Cloud):
    def getmySockets(self):
        # print(mySockets)
        return self.getdevices()


"""
        for i in mySockets:
            mySocket_name = i.get("name")
            mySocket_id = i.get("id")
            # mySocket_key = i.get("key")
            # sw_name = ""
            result = self.getstatus(mySocket_id)["result"]
            for x in result:
                name = x.get("code")
                # val = x.get("value")
                if name in ["switch_1", "switch"]:
                    print(
                        f"☣️ smart socket: {mySocket_name} | "
                        f"id:{mySocket_id} | "
                        # f"key:{mySocket_key} | "
                        # f"on:{str(val)} | "
                        f"code:{str(name)}"
                    )
                    # sw_name = name
"""
