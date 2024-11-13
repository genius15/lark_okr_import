import requests


class Project:
    def __init__(self,bot_info,host="https://project.feishu.cn",userkey=""):
        self.bot_info = bot_info
        self.host = host
        self.bot_token = self.get_header()

        self.headers= {
            "X-PLUGIN-TOKEN": self.bot_token,
            "X-USER-KEY": userkey
        }

    def get_header(self):
        api_url = self.host+"/bff/v2/authen/plugin_token"
        headers = {
            "Content-Type": "application/json"
        }

        resp = requests.post(api_url, json=self.bot_info, headers=headers).json()
        return resp.get("data").get("token")

    def get_work_item_list(self,project_key,work_item_type_key,search_group,fields):
        api = "{}/open_api/{}/work_item/{}/search/params".format(self.host,project_key,work_item_type_key)
        body = {
            "page_size":50,
            "page_num":0,
            "search_group":search_group,
        }
        if fields is not None:
            body["fields"] = fields

        all_data = []
        num = 0
        while True:
            num += 1
            body["page_num"] = num
            resp = requests.post(api,headers=self.headers,json=body,timeout=10).json()
            if resp.get("err_msg") != "":
                print("get work_item list failed:"+resp.get("err_msg"))
                break
            data = resp.get("data")
            if len(data) == 0:
                break
            all_data.extend(data)

        return all_data

    def create_work_item(self, project_key, work_item_type, template_id, fields, name):
        api = "{}/open_api/{}/work_item/create".format(self.host,project_key)
        body = {
            "work_item_type_key": work_item_type,
            "template_id": template_id,
            "name":name,
            "field_value_pairs":fields
        }
        resp = requests.post(api, headers=self.headers,json=body, timeout=10).json()
        return resp

    def update_work_item(self, work_item_id, update_fields, project_key, work_item_type_key="story"):
        api_url = "{}/open_api/{}/work_item/{}/{}".format(self.host,project_key, work_item_type_key,
                                                                               work_item_id)
        req_body = {
            "update_fields": update_fields
        }
        ret = requests.put(api_url, json=req_body, headers=self.headers)
        return ret.json()

    def query_user_by_union_ids(self, union_ids):
        if len(union_ids) == 0:
            return {"data":[]}
        api = "{}//open_api/user/query".format(self.host)
        body = {
            "out_ids":union_ids
        }
        resp = requests.post(api, headers=self.headers, json=body, timeout=10).json()
        return resp

    def query_user_by_user_keys(self,user_keys):
        if len(user_keys) == 0:
            return {"data":[]}
        api = "{}//open_api/user/query".format(self.host)
        body = {
            "user_keys":user_keys
        }
        resp = requests.post(api, headers=self.headers, json=body, timeout=10).json()
        return resp
