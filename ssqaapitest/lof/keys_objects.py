import pdb


class Values_objects(object):

    def objects_db(self, objects_db):
        db_failure_title = [i['ObjectUid'] for i in objects_db]
        db_failure_id = [i['ObjectId'] for i in objects_db]
        db_failure_set = [i['ObjectName'] for i in objects_db]
        db_fk_default = [i['FailureCount'] for i in objects_db]
        db_offline = [i['FK_ObjectTypeCode'] for i in objects_db]

        db_list = [db_failure_title, db_failure_id, db_failure_set, db_fk_default, db_offline]

        frozen_objects_db = {(frozenset(item)) for item in db_list}

        return frozen_objects_db

    def objects_api(self, objects_api):
        api_failure_title = [i['RowId'] for i in objects_api]
        api_failure_id = [i['Id'] for i in objects_api]
        api_failure_set = [i['Name'] for i in objects_api]
        api_fk_default = [i['FailureCount'] for i in objects_api]
        api_offline = [i['ObjectTypeRowId'] for i in objects_api]

        api_list = [api_failure_title, api_failure_id, api_failure_set, api_fk_default, api_offline]

        frozen_objects_api = {(frozenset(item)) for item in api_list}

        return frozen_objects_api

    def objects_db_id(self, objects_db):
        db_id = [i['ObjectUid'] for i in objects_db]
        return db_id

    def objects_api_dictionary(self, objects_api):
        api_failure_title = [objects_api['RowId']]
        api_failure_id = [objects_api['Id']]
        api_failure_set = [objects_api['Name']]
        api_fk_default = [objects_api['FailureCount']]
        api_offline = [objects_api['ObjectTypeRowId']]

        api_list = [api_failure_title, api_failure_id, api_failure_set, api_fk_default, api_offline]

        frozen_objects_api = {(frozenset(item)) for item in api_list}

        return frozen_objects_api

    def object_live_agents_api(self, objects_db):
        api_live_profile = [i['ProfileId'] for i in objects_db]
        api_live_name = [i['ProfileName'] for i in objects_db]
        api_live_object = [i['ApmObjectUid'] for i in objects_db]

        api_list = [api_live_profile, api_live_name, api_live_object]

        frozen_live_api = {(frozenset(item)) for item in api_list}

        return frozen_live_api

    def objects_liveagents_api(self, object_api):
        api_object_rowid = [i['ObjectRowId'] for i in object_api]
        api_profile_type = [i['LiveAgentType'] for i in object_api]
        api_alarm_duration = [i['MinimumAlertDuration'] for i in object_api]
        api_alarm_units = [i['MinimumAlertDurationUnits'] for i in object_api]
        api_alert_severity = [i['AlertSeverity'] for i in object_api]
        api_deployment = [i['DeploymentStatus'] for i in object_api]
        api_id = [i['Id'] for i in object_api]
        api_rowid = [i['RowId'] for i in object_api]
        #api_corretive = [i['CorrectiveSteps'] for i in asset_api]
        #api_last_g = [i['LastGeneratedWorkId'] for i in asset_api]

        api_list = [api_object_rowid, api_profile_type, api_alarm_duration, api_alarm_units, api_alert_severity,
                    api_deployment, api_id, api_rowid]

        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api

    def objects_liveagents_db(self, objects_db):
        db_rowid = [i['ApmObjectUid'] for i in objects_db]  #
        db_profile_type = [i['ProfileType'] for i in objects_db]  #
        db_alarm_duration = [i['MinimumAlarmDuration'] for i in objects_db]  #
        db_alarm_units = [i['MinimumAlarmDurationUnits'] for i in objects_db]  #
        db_alert_severity = [i['AlertSeverity'] for i in objects_db]  #
        db_deploy_status = [i['DeploymentStatus'] for i in objects_db]  #
        db_profile_name = [i['ProfileName'] for i in objects_db]  #
        db_profile_id = [i['ProfileId'] for i in objects_db]  #
        #db_corretive = [i['CorrectiveSteps'] for i in asset_db]
        #db_last_g = [i['LastGeneratedWorkId'] for i in asset_db]

        db_list = [db_rowid, db_profile_type, db_alarm_duration, db_alarm_units, db_alert_severity, db_deploy_status,
                   db_profile_name, db_profile_id]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

    def object_site_db(self, objects_db):
        db_live_profile = [i['ObjectUid'] for i in objects_db]
        db_live_name = [i['ObjectId'] for i in objects_db]
        db_live_object = [i['ObjectName'] for i in objects_db]

        db_list = [db_live_profile, db_live_name, db_live_object]

        frozen_live_api = {(frozenset(item)) for item in db_list}

        return frozen_live_api

    def object_site_api(self, objects_api):
        api_live_profile = [objects_api['RowId']]
        api_live_name = [objects_api['Id']]
        api_live_object = [objects_api['Name']]

        api_list = [api_live_profile, api_live_name, api_live_object]

        frozen_live_api = {(frozenset(item)) for item in api_list}

        return frozen_live_api

    def object_alerts_db(self, alerts_db):
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

        frozen_live_db = {(frozenset(item)) for item in db_list}

        return frozen_live_db



    def object_alerts_api(self, alert_api):
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

        frozen_live_api = {(frozenset(item)) for item in api_list}

        return frozen_live_api




