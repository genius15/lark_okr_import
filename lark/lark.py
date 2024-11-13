import requests

class LarkProxy:
    def __init__(self,app_id,app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.api_host = "https://open.larkoffice.com"
        api = "https://open.larkoffice.com/open-apis/auth/v3/tenant_access_token/internal"
        resp = requests.post(api,json={
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }).json()
        token = resp.get("tenant_access_token")
        self.headers = {"Authorization":"Bearer "+token}
        pass

    def get_okr_by_user(self,user_union_id,period_ids):
        api = self.api_host+"/open-apis/okr/v1/users/{}/okrs?limit=10&offset=0&lang=zh_cn&user_id_type=union_id&period_ids={}".\
            format(user_union_id,period_ids)
        resp = requests.get(api, headers=self.headers).json()
        if resp.get("code") != 0:
            print("faild to get okr ret={}", resp)
            return {}
        return resp.get("data", {})