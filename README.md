# lark_okr_import
飞书 OKR 导入飞书项目

首先完成config里的飞书应用认证信息及飞书项目插件认证信息的填写，执行脚本

飞书机器人需要的权限：
1. 获取 OKR 信息 okr:okr:readonly
2. 获取用户 user ID contact:user.employee_id:readonly

飞书项目插件需要的权限：
1. 创建、更新工作项及工作流 work_item:work_item.info:write


脚本输入参数解释
| 参数名 | 解释 |
| --- | --- |
| user_key |必填，需要导入的人的飞书项目 userkey|
| okr_period_id |必填，okr 周期id，可以通过 okr 获取周期接口来获取，因为不常用，所以这里做成了直接输入|
|project_key | 必填，空间key|
| objective_work_item_type | 必填，objective 的工作项type key|
|objective_templ=2186825| 必填，objective 使用的模板id|
|objective_id_field | 必填，okr 的数据id字段，该字段在执行重复导入时用来判断是更新还是新建 objective|
|objective_assignee_field|选填，okr 指派人存储字段，多选人员字段|
|objective_period_field | 选填，okr 周期记录字段key，单行文本类型，值示例：2024 年 10 月 - 12 月|
|kr_work_item_type |必填， key results 工作项type key|
|kr_tmpl|必填，key results 的模板id|
|kr_related_o_field | 必填，key results关联的objective关联字段，单选关联工作项类型|
|kr_id_field|必填，存储okr里key results的数据id|
|kr_assignee_field|选填，指派人，多选人员类型|



