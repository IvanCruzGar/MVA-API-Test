import pdb


class Values_work(object):

    def work_items_db(self, work_items_db):
        db_work_item = [i['WorkItemUid'] for i in work_items_db]
        db_work_item_id = [i['WorkItemId'] for i in work_items_db]
        db_work_item_title = [i['WorkItemTitle'] for i in work_items_db]
        db_work_description = [i['WorkItemDescription'] for i in work_items_db]
        db_work_type = [i['WorkItemType'] for i in work_items_db]
        db_fk_object = [i['FK_ObjectUid'] for i in work_items_db]
        db_fk_object_mimosa = [i['FK_ObjectMimosaSiteCode'] for i in work_items_db]
        db_fk_object_mimosa_id = [i['FK_ObjectMimosaId'] for i in work_items_db]
        db_work_mgmt = [i['WorkMgmtType'] for i in work_items_db]
        db_disabled = [i['Disabled'] for i in work_items_db]
        db_work_category = [i['WorkCategory'] for i in work_items_db]
        #db_is_failure = [i['IsFailure'] for i in work_items_db]
        db_priority = [i['Priority'] for i in work_items_db]
        db_work_status = [i['WorkStatus'] for i in work_items_db]

        db_list = [db_work_item, db_work_item_id, db_work_item_title, db_work_description, db_work_type, db_fk_object,
                   db_fk_object_mimosa, db_fk_object_mimosa_id, db_work_mgmt, db_disabled, db_work_category,
                   db_priority, db_work_status]

        frozen_objects_db = {(frozenset(item)) for item in db_list}

        return frozen_objects_db

    def work_items_api(self, work_items_api):
        api_work_item = [i['WorkItemUid'] for i in work_items_api]
        api_work_item_id = [i['WorkItemId'] for i in work_items_api]
        api_work_item_title = [i['WorkItemTitle'] for i in work_items_api]
        api_work_description = [i['WorkItemDescription'] for i in work_items_api]
        api_work_type = [i['WorkItemType'] for i in work_items_api]
        api_fk_a = [i['Fk_ObjectUid'] for i in work_items_api]
        api_fk_b = [i['Fk_ObjectMimosaSiteCode'] for i in work_items_api]
        api_fk_c = [i['Fk_ObjectMimosaId'] for i in work_items_api]
        api_work_mgmt = [i['WorkMgmtType'] for i in work_items_api]
        api_disabled = [i['Disabled'] for i in work_items_api]
        api_work_category = [i['WorkCategory'] for i in work_items_api]
        #api_is_failure = [i['IsFailure'] for i in work_items_api]
        api_priority = [i['Priority'] for i in work_items_api]
        api_work_status = [i['WorkStatus'] for i in work_items_api]

        db_list = [api_work_item, api_work_item_id, api_work_item_title, api_work_description, api_work_type,
                   api_fk_a, api_fk_b, api_fk_c, api_work_mgmt, api_disabled, api_work_category, api_priority,
                   api_work_status]

        frozen_objects_db = {(frozenset(item)) for item in db_list}

        return frozen_objects_db

    def work_items_id_api(self, work_items_api):

        api_work_item = [i['WorkItemUid'] for i in work_items_api]
        return api_work_item
