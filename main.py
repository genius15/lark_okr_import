from okr_importer import okr

if __name__ == '__main__':
    print(okr.sync_okr_to_project(
        user_key="",
        okr_period_id="",
        project_key="",
        objective_work_item_type="", # objective 的工作项type key
        objective_templ=0, # obejctive使用的模板id
        objective_id_field="",# 必填，okr 的数据id字段，该字段在执行重复导入时用来判断是更新还是新建objective
        objective_assignee_field="", # 选填，okr 指派人存储字段，多选人员字段
        objective_period_field="", # 选填，okr 周期记录字段key，单行文本类型，值示例：2024 年 10 月 - 12 月
        kr_work_item_type="",
        kr_tmpl=0,
        kr_related_o_field="",# 必填，key results关联的objective关联字段，单选关联工作项类型
        kr_id_field="",# 必填，存储okr里key results的数据id
        kr_assignee_field=""# 选填，指派人，多选人员类型
    ))

