class Values_asset(object):

    def assets_rows_db(self, asset_db):
        db_objectuid = [i['ObjectUid'] for i in asset_db]
        db_objectid = [i['ObjectId'] for i in asset_db]
        db_objectname = [i['ObjectName'] for i in asset_db]
        db_objectdescription = [i['ObjectDescription'] for i in asset_db]
        db_parentuid = [i['ParentUid'] for i in asset_db]
        db_fk_objecttype = [i['FK_ObjectTypeCode'] for i in asset_db]
        db_disabled = [i['Disabled'] for i in asset_db]
        db_failurecount = [i['FailureCount'] for i in asset_db]
        db_customfield1 = [i['CustomField1'] for i in asset_db]
        db_customfield2 = [i['CustomField2'] for i in asset_db]
        db_customfield3 = [i['CustomField3'] for i in asset_db]
        db_customfield4 = [i['CustomField4'] for i in asset_db]
        db_mtbyears = [i['MTBFYears'] for i in asset_db]
        db_timeinserviceyears = [i['TimeInServiceYears'] for i in asset_db]
        db_manufacturer = [i['Manufacturer'] for i in asset_db]
        db_model = [i['Model'] for i in asset_db]
        db_test = ["testing2"]

        db_list = [db_objectuid, db_objectid, db_objectname, db_objectdescription, db_parentuid, db_fk_objecttype,
                   db_disabled, db_failurecount, db_customfield1, db_customfield2, db_customfield3, db_customfield4,
                   db_mtbyears, db_timeinserviceyears, db_manufacturer, db_model, db_test]

        frozen_asset_db = {(frozenset(item)) for item in db_list}

        return frozen_asset_db

    def assets_rows_api(self, asset_api):
        api_rowid = [i['RowId'] for i in asset_api]
        api_id = [i['Id'] for i in asset_api]
        api_name = [i['Name'] for i in asset_api]
        api_description = [i['Description'] for i in asset_api]
        api_objectrowid = [i['ObjectRowId'] for i in asset_api]
        api_objecttyperowid = [i['ObjectTypeRowId'] for i in asset_api]
        api_istemplate = [i['IsTemplate'] for i in asset_api]
        api_failurecount = [i['FailureCount'] for i in asset_api]
        api_customfield1 = [i['CustomField1'] for i in asset_api]
        api_customfield2 = [i['CustomField2'] for i in asset_api]
        api_customfield3 = [i['CustomField3'] for i in asset_api]
        api_customfield4 = [i['CustomField4'] for i in asset_api]
        api_mtbyears = [i['MtbfYears'] for i in asset_api]
        api_timeinservice = [i['TimeInServiceYears'] for i in asset_api]
        api_manufactured = [i['ManufacturerId'] for i in asset_api]
        api_modelid = [i['ModelId'] for i in asset_api]
        api_test = ["testing2"]

        api_list = [api_rowid, api_id, api_name, api_description, api_objectrowid, api_objecttyperowid, api_istemplate,
                    api_failurecount, api_customfield1, api_customfield2, api_customfield3, api_customfield4,
                    api_mtbyears, api_timeinservice, api_manufactured, api_modelid, api_test]

        frozen_asset_api = {(frozenset(item)) for item in api_list}

        return frozen_asset_api

    def assets_rows_api_dictionary(self, asset_api):
        api_rowid = [asset_api['RowId']]
        api_id = [asset_api['Id']]
        api_name = [asset_api['Name']]
        api_description = [asset_api['Description']]
        api_objectrowid = [asset_api['ObjectRowId']]
        api_objecttyperowid = [asset_api['ObjectTypeRowId']]
        api_istemplate = [asset_api['IsTemplate']]
        api_failurecount = [asset_api['FailureCount']]
        api_customfield1 = [asset_api['CustomField1']]
        api_customfield2 = [asset_api['CustomField2']]
        api_customfield3 = [asset_api['CustomField3']]
        api_customfield4 = [asset_api['CustomField4']]
        api_mtbyears = [asset_api['MtbfYears']]
        api_timeinservice = [asset_api['TimeInServiceYears']]
        api_manufactured = [asset_api['ManufacturerId']]
        api_modelid = [asset_api['ModelId']]
        api_test = ["testing2"]

        api_list = [api_rowid, api_id, api_name, api_description, api_objectrowid, api_objecttyperowid, api_istemplate,
                    api_failurecount, api_customfield1, api_customfield2, api_customfield3, api_customfield4,
                    api_mtbyears, api_timeinservice, api_manufactured, api_modelid, api_test]

        frozen_asset_api = {(frozenset(item)) for item in api_list}

        return frozen_asset_api

    def assets_liveagents_db(self, asset_db):
        db_rowid = [i['ApmObjectUid'] for i in asset_db]  #
        db_profile_type = [i['ProfileType'] for i in asset_db]  #
        db_alarm_duration = [i['MinimumAlarmDuration'] for i in asset_db]  #
        db_alarm_units = [i['MinimumAlarmDurationUnits'] for i in asset_db]  #
        db_alert_severity = [i['AlertSeverity'] for i in asset_db]  #
        db_deploy_status = [i['DeploymentStatus'] for i in asset_db]  #
        db_profile_name = [i['ProfileName'] for i in asset_db]  #
        db_profile_id = [i['ProfileId'] for i in asset_db]  #
        #db_corretive = [i['CorrectiveSteps'] for i in asset_db]
        #db_last_g = [i['LastGeneratedWorkId'] for i in asset_db]

        db_list = [db_rowid, db_profile_type, db_alarm_duration, db_alarm_units, db_alert_severity, db_deploy_status,
                   db_profile_name, db_profile_id]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

    def assets_liveagents_api(self, asset_api):
        api_object_rowid = [i['ObjectRowId'] for i in asset_api]
        api_profile_type = [i['LiveAgentType'] for i in asset_api]
        api_alarm_duration = [i['MinimumAlertDuration'] for i in asset_api]
        api_alarm_units = [i['MinimumAlertDurationUnits'] for i in asset_api]
        api_alert_severity = [i['AlertSeverity'] for i in asset_api]
        api_deployment = [i['DeploymentStatus'] for i in asset_api]
        api_id = [i['Id'] for i in asset_api]
        api_rowid = [i['RowId'] for i in asset_api]
        #api_corretive = [i['CorrectiveSteps'] for i in asset_api]
        #api_last_g = [i['LastGeneratedWorkId'] for i in asset_api]

        api_list = [api_object_rowid, api_profile_type, api_alarm_duration, api_alarm_units, api_alert_severity,
                    api_deployment, api_id, api_rowid]

        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api

    def assets_liveagents_api_dict(self, asset_api):
        api_object_rowid = [asset_api['ObjectRowId']]
        api_profile_type = [asset_api['LiveAgentType']]
        api_alarm_duration = [asset_api['MinimumAlertDuration']]
        api_alarm_units = [asset_api['MinimumAlertDurationUnits']]
        api_alert_severity = [asset_api['AlertSeverity']]
        api_deployment = [asset_api['DeploymentStatus']]
        api_id = [asset_api['Id']]
        api_rowid = [asset_api['RowId']]
        #api_corretive = [i['CorrectiveSteps'] for i in asset_api]
        #api_last_g = [i['LastGeneratedWorkId'] for i in asset_api]

        api_list = [api_object_rowid, api_profile_type, api_alarm_duration, api_alarm_units, api_alert_severity,
                    api_deployment, api_id, api_rowid]

        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api
