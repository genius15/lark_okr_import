from lark.lark import LarkProxy
from project import project_bot
import config


def get_okr_by_user(user_union_id,period_ids):
    larkapi = LarkProxy(config.lark_app.get("key"), config.lark_app.get("secret"))
    return larkapi.get_okr_by_user(user_union_id,period_ids)


def get_work_item_by_okr_id(project_proxy,project_key,work_item_type_key,id,okr_id_field_key):
    search_groups = [{
        "conjunction": "AND",
        "search_params": [
            {
                "param_key": okr_id_field_key,
                "value": id,
                "operator": "="
            }
        ], "search_groups": []
    }]

    wi_data = project_proxy.get_work_item_list(project_key, work_item_type_key, {
        "conjunction": "OR",
        "search_params": [],
        "search_groups": search_groups}, fields=["name"])
    return wi_data


def sync_okr_to_project(user_key,
                        okr_period_id,
                        project_key,
                        objective_work_item_type,
                        objective_templ,
                        objective_id_field,
                        objective_assignee_field,
                        objective_period_field,
                        kr_work_item_type,
                        kr_tmpl,
                        kr_related_o_field,
                        kr_id_field,
                        kr_assignee_field):
    project = project_bot.Project(config.project_plugin, userkey=user_key)
    uids = project.query_user_by_user_keys([user_key])
    if len(uids["data"]) == 0:
        print("no user :"+user_key)
        return "failed"

    okr_list = get_okr_by_user(uids["data"][0]["out_id"],okr_period_id).get("okr_list",[])
    if len(okr_list) == 0:
        return
    objective_list= okr_list[0].get('objective_list',[])
    objective_period = okr_list[0].get("name")
    for o in objective_list:
        oid = o.get("id")
        objects = get_work_item_by_okr_id(project,project_key,objective_work_item_type,oid,objective_id_field)
        content = o.get("content").strip("\n")
        objective_assignees = []
        objective_fields = []
        if objective_assignee_field != "":
            mentioned_user_list = o.get("mentioned_user_list",[])
            union_ids = []
            for uid in mentioned_user_list:
                union_ids.append(uid.get("user_id"))
            urs = project.query_user_by_union_ids(union_ids)
            for u in urs["data"]:
                objective_assignees.append(u.get("user_key"))
            objective_fields.append({"field_key": objective_assignee_field, "field_value": objective_assignees})
        if objective_period_field != "":
            objective_fields.append({"field_key": objective_period_field, "field_value": objective_period})

        if len(objects) > 0 :
            object_wid = objects[0].get("id")
            objective_fields.extend([{"field_key":"name","field_value":content}])
            ret = project.update_work_item(object_wid, objective_fields, project_key, objective_work_item_type)
            print(ret)
        else:
            objective_fields.extend([{"field_key":objective_id_field,"field_value":oid}])
            resp = project.create_work_item(project_key, objective_work_item_type, objective_templ,
                                            objective_fields, content)

            object_wid = resp.get("data")

        kr_list = o.get("kr_list")
        for kr in kr_list:
            kr_content = kr.get("content").strip("\n")
            kr_id = kr.get("id")
            krs = get_work_item_by_okr_id(project, project_key, kr_work_item_type, kr_id, kr_id_field)
            kr_assignees = []
            if kr_assignee_field != "":
                mentioned_user_list = kr.get("mentioned_user_list")
                union_ids = []
                for uid in mentioned_user_list:
                    union_ids.append(uid.get("user_id"))
                urs = project.query_user_by_union_ids(union_ids)
                for u in urs["data"]:
                    kr_assignees.append(u.get("user_key"))

            if len(krs) > 0 :
                kr_wid = krs[0].get("id")
                fields = [{"field_key": "name", "field_value": kr_content}]
                if kr_assignee_field != "":
                    fields.append({"field_key":kr_assignee_field,"field_value":kr_assignees})
                ret = project.update_work_item(kr_wid, fields, project_key,
                                               kr_work_item_type)
                print(str(ret)+":"+kr_content)
            else:
                fields = [
                    {
                        "field_key":kr_related_o_field,
                        "field_value":object_wid
                    },
                    {
                        "field_key":kr_id_field,
                        "field_value":kr_id
                    }
                ]
                if kr_assignee_field != "":
                    fields.append({"field_key": kr_assignee_field, "field_value": kr_assignees})
                ret = project.create_work_item(project_key, kr_work_item_type, kr_tmpl, fields, kr_content)
                print(str(ret)+":"+kr_content)
        print("finish object:"+content)
    return "finish okr"

