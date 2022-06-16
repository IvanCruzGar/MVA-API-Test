class Values_equipment(object):

    def equipment_db(self, equipment_db):
        db_failure_title = [i['FailureSetTitle'] for i in equipment_db]
        db_failure_id = [i['FailureSetProfileId'] for i in equipment_db]
        db_failure_set = [i['FailureSetDescription'] for i in equipment_db]
        db_fk_default = [i['FK_DefaultSensorGroupId'] for i in equipment_db]
        db_offline = [i['OfflineCondition'] for i in equipment_db]

        db_list = [db_failure_title, db_failure_id, db_failure_set, db_fk_default, db_offline]

        return db_list

    def equipment_api(self, equipment_api):
        api_failure_title = [i['EquipmentSetTitle'] for i in equipment_api]
        api_failure_id = [i['RowId'] for i in equipment_api]
        api_failure_set = [i['EquipmentSetDescription'] for i in equipment_api]
        api_fk_default = [i['FK_DefaultSensorGroupId'] for i in equipment_api]
        api_offline = [i['OfflineCondition'] for i in equipment_api]

        api_list = [api_failure_title, api_failure_id, api_failure_set, api_fk_default, api_offline]

        return api_list
