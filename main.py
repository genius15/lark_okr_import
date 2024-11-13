from okr_importer import okr

if __name__ == '__main__':
    print(okr.sync_okr_to_project(
        user_key="",
        okr_period_id="",
        project_key="",
        objective_work_item_type="",
        objective_templ=0,
        objective_id_field="",
        objective_assignee_field="",
        objective_period_field="",
        kr_work_item_type="",
        kr_tmpl=0,
        kr_related_o_field="",
        kr_id_field="",
        kr_assignee_field=""
    ))

