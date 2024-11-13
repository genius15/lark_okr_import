from okr_importer import okr

if __name__ == '__main__':
    print(okr.sync_okr_to_project(
        user_key="wangchen.wanzi",
        okr_period_id="7414921851280261148",  # 7-9月:7380768388039458817,10-12: 7414921851280261148
        project_key="5c91d3166a874fce64415f4c",
        objective_work_item_type="6705277859fbf80ace06f6c2",
        objective_templ=325268,
        objective_id_field="field_4c38c6",
        objective_assignee_field="field_77a467",
        objective_period_field="field_616243",
        kr_work_item_type="670527bb438a7a37c446964a",
        kr_tmpl=325273,
        kr_related_o_field="field_ebe585",
        kr_id_field="field_ccb423",
        kr_assignee_field="field_5529a1"
    ))

