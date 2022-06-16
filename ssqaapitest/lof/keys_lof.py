import pdb


class Values_lof(object):

    def live_agents_rows_db(self, alerts_db):
        db_profileId = [i['ProfileId'] for i in alerts_db]
        db_profilename = [i['ProfileName'] for i in alerts_db]
        db_apmobjectid = [i['ApmObjectUid'] for i in alerts_db]
        db_profiletype = [i['ProfileType'] for i in alerts_db]
        db_minimumalarm = [i['MinimumAlarmDuration'] for i in alerts_db]  ############
        db_minimumunits = [i['MinimumAlarmDurationUnits'] for i in alerts_db]
        db_alertseverity = [i['AlertSeverity'] for i in alerts_db]
        db_deployment = [i['DeploymentStatus'] for i in alerts_db]
        db_profilestate = [i['ProfileState'] for i in alerts_db]
        db_alertclosemode = [i['AlertCloseMode'] for i in alerts_db]
        db_profileprocess = [i['ProfileProcessState'] for i in alerts_db]
        db_profileprocessstate = [i['ProfileProcessStateDescriptor'] for i in alerts_db]
        db_profilecomments = [i['ProfileProcessStateComments'] for i in alerts_db]
        db_lastprofileprocess = [i['LastProfileProcessState'] for i in alerts_db]
        db_lastprofiledescriptor = [i['LastProfileProcessStateDescriptor'] for i in alerts_db]
        db_lastprofilestate = [i['LastProfileProcessStateComments'] for i in alerts_db]
        db_lastexecutiontime = [i['LastExecutionTime'] for i in alerts_db]

        db_list = [db_profileId, db_profilename, db_apmobjectid, db_profiletype, db_minimumalarm, db_minimumunits,
                   db_alertseverity, db_deployment, db_profilestate, db_alertclosemode, db_profileprocess,
                   db_profileprocessstate, db_profilecomments, db_lastprofileprocess, db_lastprofiledescriptor,
                   db_lastprofilestate, db_lastexecutiontime]

        frozen_alerts_db = {(frozenset(item)) for item in db_list}

        return frozen_alerts_db

    def live_agents_rows_api(self, alert_api):
        api_rowid = [alert_api['RowId']]
        api_id = [alert_api['Id']]
        api_objectrowid = [alert_api['ObjectRowId']]
        api_liveagenttype = [alert_api['LiveAgentType']]
        api_minimumalertduration = [alert_api['MinimumAlertDuration']]  #######
        api_minimumalertunits = [alert_api['MinimumAlertDurationUnits']]
        api_alertseverity = [alert_api['AlertSeverity']]
        api_deploymentstatus = [alert_api['DeploymentStatus']]
        api_liveagentstate = [alert_api['LiveAgentState']]
        api_alertclosemode = [alert_api['AlertCloseMode']]
        api_laps = [alert_api['LiveAgentProcessState']]
        api_lapsd = [alert_api['LiveAgentProcessStateDescriptor']]
        api_lapsc = [alert_api['LiveAgentProcessStateComments']]
        api_llaps = [alert_api['LastLiveAgentProcessState']]
        api_llapsd = [alert_api['LastLiveAgentProcessStateDescriptor']]
        api_llapsc = [alert_api['LastLiveAgentProcessStateComments']]
        api_let = [alert_api['LastExecutionTime']]

        api_list = [api_rowid, api_id, api_objectrowid, api_liveagenttype, api_minimumalertduration,
                    api_minimumalertunits, api_alertseverity, api_deploymentstatus, api_liveagentstate,
                    api_alertclosemode, api_laps, api_lapsd, api_lapsc, api_llaps, api_llapsd, api_llapsc, api_let]

        frozen_asset_api = {(frozenset(item)) for item in api_list}

        return frozen_asset_api

    def get_alerts_db(self, alerts_db):
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

        frozen_asset_db = {(frozenset(item)) for item in db_list}

        return frozen_asset_db

    def get_alerts_api(self, alert_api):
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

        frozen_asset_api = {(frozenset(item)) for item in api_list}

        return frozen_asset_api

    def live_agents_rows_api_list(self, alert_api):
        api_rowid = [i['RowId'] for i in alert_api]
        api_id = [i['Id'] for i in alert_api]
        api_objectrowid = [i['ObjectRowId'] for i in alert_api]
        api_liveagenttype = [i['LiveAgentType'] for i in alert_api]
        api_minimumalertduration = [i['MinimumAlertDuration'] for i in alert_api]  #######
        api_minimumalertunits = [i['MinimumAlertDurationUnits'] for i in alert_api]
        api_alertseverity = [i['AlertSeverity'] for i in alert_api]
        api_deploymentstatus = [i['DeploymentStatus'] for i in alert_api]
        api_liveagentstate = [i['LiveAgentState'] for i in alert_api]
        api_alertclosemode = [i['AlertCloseMode'] for i in alert_api]
        api_laps = [i['LiveAgentProcessState'] for i in alert_api]
        api_lapsd = [i['LiveAgentProcessStateDescriptor'] for i in alert_api]
        api_lapsc = [i['LiveAgentProcessStateComments'] for i in alert_api]
        api_llaps = [i['LastLiveAgentProcessState'] for i in alert_api]
        api_llapsd = [i['LastLiveAgentProcessStateDescriptor'] for i in alert_api]
        api_llapsc = [i['LastLiveAgentProcessStateComments'] for i in alert_api]
        api_let = [i['LastExecutionTime'] for i in alert_api]

        api_list = [api_rowid, api_id, api_objectrowid, api_liveagenttype, api_minimumalertduration,
                    api_minimumalertunits, api_alertseverity, api_deploymentstatus, api_liveagentstate,
                    api_alertclosemode, api_laps, api_lapsd, api_lapsc, api_llaps, api_llapsd, api_llapsc, api_let]

        frozen_asset_api = {(frozenset(item)) for item in api_list}

        return frozen_asset_api
