class Values_site(object):

    def site_db(self, site_db):
        db_disabled = [i['Disabled'] for i in site_db]
        db_parentid = [i['ParentUid'] for i in site_db]
        db_objectid = [i['ObjectId'] for i in site_db]
        db_objectname = [i['ObjectName'] for i in site_db]
        db_objectuid = [i['ObjectUid'] for i in site_db]

        db_list = [db_disabled, db_parentid, db_objectid, db_objectname, db_objectuid]

        frozen_objects_db = {(frozenset(item)) for item in db_list}

        return frozen_objects_db

    def site_api(self, site_api):
        api_template = [i['IsTemplate'] for i in site_api]
        api_crowid = [i['CustomerRowId'] for i in site_api]
        api_id = [i['Id'] for i in site_api]
        api_name = [i['Name'] for i in site_api]
        api_rowid = [i['RowId'] for i in site_api]

        db_list = [api_template, api_crowid, api_id, api_name, api_rowid]

        frozen_objects_db = {(frozenset(item)) for item in db_list}

        return frozen_objects_db

    def site_ids_db(self, site_ids):
        db_parentid = [i['ObjectUid'] for i in site_ids]
        return db_parentid

    def site_api_dictionary(self, id_api):
        api_template = [id_api['IsTemplate']]
        api_crowid = [id_api['CustomerRowId']]
        api_id = [id_api['Id']]
        api_name = [id_api['Name']]
        api_rowid = [id_api['RowId']]

        db_list = [api_template, api_crowid, api_id, api_name, api_rowid]

        frozen_objects_db = {(frozenset(item)) for item in db_list}

        return frozen_objects_db

    def site_object_db(self, site_db):
        db_objectuid = [i['ObjectUid'] for i in site_db]
        db_object_id = [i['ObjectId'] for i in site_db]
        db_object_name = [i['ObjectName'] for i in site_db]
        db_failure_count = [i['FailureCount'] for i in site_db]
        db_parent_uid = [i['ParentUid'] for i in site_db]
        db_fk_object_type = [i['FK_ObjectTypeCode'] for i in site_db]

        db_list = [db_objectuid, db_object_id, db_object_name, db_failure_count, db_parent_uid, db_fk_object_type]

        frozen_objects_db = {(frozenset(item)) for item in db_list}

        return frozen_objects_db

    def site_object_api(self, site_api):
        api_objectuid = [i['RowId'] for i in site_api]
        api_object_id = [i['Id'] for i in site_api]
        api_object_name = [i['Name'] for i in site_api]
        api_failure_count = [i['FailureCount'] for i in site_api]
        api_parent_uid = [i['ObjectRowId'] for i in site_api]
        api_fk_object_type = [i['ObjectTypeRowId'] for i in site_api]

        api_list = [api_objectuid, api_object_id, api_object_name, api_failure_count, api_parent_uid, api_fk_object_type]

        frozen_objects_db = {(frozenset(item)) for item in api_list}

        return frozen_objects_db

    def site_alerts_db(self, alerts_db):
        db_alertid = [i['AlertId'] for i in alerts_db]
        db_profileid = [i['FK_ProfileId'] for i in alerts_db]
        db_work_title = [i['DefaultWorkTitle'] for i in alerts_db]
        work_description = [i['DefaultWorkDescription'] for i in alerts_db]
        db_acked = [i['Acked'] for i in alerts_db]
        db_acked_by = [i['AckedBy'] for i in alerts_db]
        db_ack_comments = [i['AckComments'] for i in alerts_db]
        db_state = [i['State'] for i in alerts_db]
        db_close_mode = [i['CloseMode'] for i in alerts_db]
        db_close_by = [i['ClosedBy'] for i in alerts_db]
        db_is_failure = [i['IsFailure'] for i in alerts_db]
        db_intervention_type = [i['InterventionType'] for i in alerts_db]
        db_intervention_note = [i['InterventionNotes'] for i in alerts_db]
        db_deployment = [i['DeploymentStatus'] for i in alerts_db]

        db_list = [db_alertid, db_profileid, db_work_title, work_description, db_acked, db_acked_by,
                   db_ack_comments, db_state, db_close_mode, db_close_by, db_is_failure, db_intervention_type,
                   db_intervention_note, db_deployment]

        return db_list

    def site_alerts_api(self, alert_api):
        api_rowid = [i['RowId'] for i in alert_api]
        api_liveagentrowid = [i['LiveAgentRowId'] for i in alert_api]
        api_work_title = [i['DefaultWorkTitle'] for i in alert_api]
        api_work_description = [i['DefaultWorkDescription'] for i in alert_api]
        api_acked = [i['Acked'] for i in alert_api]
        api_acked_by = [i['AckedByName'] for i in alert_api]
        api_ack_comments = [i['AckComments'] for i in alert_api]
        api_state = [i['State'] for i in alert_api]
        api_close_mode = [i['CloseMode'] for i in alert_api]
        api_closed_by = [i['ClosedByName'] for i in alert_api]
        api_is_failure = [i['IsFailure'] for i in alert_api]
        api_intervention_type = [i['InterventionType'] for i in alert_api]
        api_intervention_notes = [i['InterventionNotes'] for i in alert_api]
        api_deployment_status = [i['DeploymentStatus'] for i in alert_api]

        api_list = [api_rowid, api_liveagentrowid, api_work_title, api_work_description, api_acked, api_acked_by,
                    api_ack_comments, api_state, api_close_mode, api_closed_by, api_is_failure, api_intervention_type,
                    api_intervention_notes, api_deployment_status]

        return api_list

    def site_liveagents_api(self, site_api):
        api_object_rowid = [i['ObjectRowId'] for i in site_api]
        api_profile_type = [i['LiveAgentType'] for i in site_api]
        api_alarm_duration = [i['MinimumAlertDuration'] for i in site_api]
        api_alarm_units = [i['MinimumAlertDurationUnits'] for i in site_api]
        api_alert_severity = [i['AlertSeverity'] for i in site_api]
        api_deployment = [i['DeploymentStatus'] for i in site_api]
        api_id = [i['Id'] for i in site_api]
        api_rowid = [i['RowId'] for i in site_api]
        #api_corretive = [i['CorrectiveSteps'] for i in site_api]
        #api_last_g = [i['LastGeneratedWorkId'] for i in site_api]

        api_list = [api_object_rowid, api_profile_type, api_alarm_duration, api_alarm_units, api_alert_severity,
                    api_deployment, api_id, api_rowid]

        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api

    def objects_liveagents_db(self, site_db):
        db_rowid = [i['ApmObjectUid'] for i in site_db]  #
        db_profile_type = [i['ProfileType'] for i in site_db]  #
        db_alarm_duration = [i['MinimumAlarmDuration'] for i in site_db]  #
        db_alarm_units = [i['MinimumAlarmDurationUnits'] for i in site_db]  #
        db_alert_severity = [i['AlertSeverity'] for i in site_db]  #
        db_deploy_status = [i['DeploymentStatus'] for i in site_db]  #
        db_profile_name = [i['ProfileName'] for i in site_db]  #
        db_profile_id = [i['ProfileId'] for i in site_db]  #
        #db_corretive = [i['CorrectiveSteps'] for i in site_db]
        #db_last_g = [i['LastGeneratedWorkId'] for i in site_db]

        db_list = [db_rowid, db_profile_type, db_alarm_duration, db_alarm_units, db_alert_severity, db_deploy_status,
                   db_profile_name, db_profile_id]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db





















