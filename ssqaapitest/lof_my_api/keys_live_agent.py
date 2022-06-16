class ValuesLiveAgent(object):

    def assets_live_agent_db(self, asset_db):
        db_fk_object_rowid = [i['FK_ObjectRowId'] for i in asset_db]
        db_live_agent_type = [i['LiveAgentType'] for i in asset_db]
        db_alarm_duration = [i['MinimumAlertDuration'] for i in asset_db]
        db_alarm_units = [i['MinimumAlertDurationUnits'] for i in asset_db]
        db_alert_severity = [i['AlertSeverity'] for i in asset_db]
        db_deploy_status = [i['DeploymentStatus'] for i in asset_db]
        db_id = [i['Id'] for i in asset_db]
        db_live_agent_id = [i['LiveAgentId'] for i in asset_db]

        db_list = [db_fk_object_rowid, db_live_agent_type, db_alarm_duration, db_alarm_units, db_alert_severity, db_deploy_status,
                   db_id, db_live_agent_id]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

    def assets_live_agent_api(self, asset_api):
        api_fk_object_rowid = [i['fkObjectRowId'] for i in asset_api]
        api_live_agent_type = [i['liveAgentType'] for i in asset_api]
        api_alarm_duration = [i['minimumAlertDuration'] for i in asset_api]
        api_alarm_units = [i['minimumAlertDurationUnits'] for i in asset_api]
        api_alert_severity = [i['alertSeverity'] for i in asset_api]
        api_deployment = [i['deploymentStatus'] for i in asset_api]
        api_id = [i['id'] for i in asset_api]
        api_live_agent_id = [i['liveAgentId'] for i in asset_api]

        api_list = [api_fk_object_rowid, api_live_agent_type, api_alarm_duration, api_alarm_units, api_alert_severity,
                    api_deployment, api_id, api_live_agent_id]

        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api

    def assets_live_agent_db_dict(self, asset_db):
        db_live_agent_type = [i['LiveAgentType'] for i in asset_db]
        db_severity = [i['Severity'] for i in asset_db]
        db_deploy_status = [i['DeploymentStatus'] for i in asset_db]
        db_live_agent_name = [i['LiveAgentName'] for i in asset_db]

        db_list = [db_live_agent_type, db_severity, db_deploy_status,
                   db_live_agent_name]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

    def assets_live_agent_api_dict(self, asset_api):
        api_live_agent_type = [asset_api['liveAgentType']]
        api_alert_severity = [asset_api['alertSeverity']]
        api_deployment = [asset_api['deploymentStatus']]
        api_id = [asset_api['id']]

        api_list = [api_live_agent_type, api_alert_severity,
                    api_deployment, api_id]

        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api