import pdb


class Values_alerts(object):

    def get_alerts_db(self, alerts_db):
        db_alertid = [i['ApmvId'] for i in alerts_db]
        db_profileid = [i['AlertId'] for i in alerts_db]
        db_alertsever = [i['FK_ConnectionId'] for i in alerts_db]
        db_work_title = [i['FK_LiveAgentId'] for i in alerts_db]
        db_acked = [i['Severity'] for i in alerts_db]
        db_acked_by = [i['WorkTitle'] for i in alerts_db]
        db_ack_comments = [i['WorkDescription'] for i in alerts_db]
        db_state = [i['ApmvState'] for i in alerts_db]
        db_close_mode = [i['AckedByName'] for i in alerts_db]
        db_close_by = [i['State'] for i in alerts_db]
        db_is_failure = [i['ClosedMode'] for i in alerts_db]
        db_intervention_type = [i['ClosedByName'] for i in alerts_db]
        db_intervention_note = [i['InterventionType'] for i in alerts_db]
        db_live_name = [i['LiveAgentName'] for i in alerts_db]
        db_asset_id = [i['AssetId'] for i in alerts_db]
        db_site_id = [i['SiteId'] for i in alerts_db]
        db_liveagent_type = [i['LiveAgentTypeString'] for i in alerts_db]
        db_mlagent = [i['MLAgentCategoryString'] for i in alerts_db]
        db_mlagent_type = [i['MLAgentTypeString'] for i in alerts_db]
        db_site = [i['SiteName'] for i in alerts_db]

        db_list = [db_alertid, db_profileid, db_alertsever, db_work_title, db_acked, db_acked_by, db_ack_comments,
                   db_state, db_close_mode, db_close_by, db_is_failure, db_intervention_type, db_intervention_note,
                   db_live_name, db_asset_id, db_site_id, db_liveagent_type, db_mlagent, db_mlagent_type, db_site]

        return db_list

    def get_alerts_api(self, alerts_api):
        api_alertid = [i['apmvId'] for i in alerts_api]
        api_profileid = [i['alertId'] for i in alerts_api]
        api_alertsever = [i['fkConnectionId'] for i in alerts_api]
        api_work_title = [i['fkLiveAgentId'] for i in alerts_api]
        api_acked = [i['severity'] for i in alerts_api]
        api_acked_by = [i['workTitle'] for i in alerts_api]
        api_ack_comments = [i['workDescription'] for i in alerts_api]
        api_state = [i['apmvState'] for i in alerts_api]
        api_close_mode = [i['ackedByName'] for i in alerts_api]
        api_close_by = [i['state'] for i in alerts_api]
        api_is_failure = [i['closedMode'] for i in alerts_api]
        api_intervention_type = [i['closedByName'] for i in alerts_api]
        api_intervention_note = [i['interventionType'] for i in alerts_api]
        api_liveagent = [i['liveAgentName'] for i in alerts_api]
        api_assetid = [i['assetId'] for i in alerts_api]
        api_site1d = [i['siteId'] for i in alerts_api]
        api_live_agent = [i['liveAgentTypeString'] for i in alerts_api]
        api_m_la_agent = [i['mlAgentCategoryString'] for i in alerts_api]
        api_m_la_type = [i['mlAgentTypeString'] for i in alerts_api]
        api_site_name = [i['siteName'] for i in alerts_api]

        api_list = [api_alertid, api_profileid, api_alertsever, api_work_title, api_acked, api_acked_by,
                    api_ack_comments, api_state, api_close_mode, api_close_by, api_is_failure, api_intervention_type,
                    api_intervention_note, api_liveagent, api_assetid, api_site1d, api_live_agent, api_m_la_agent,
                    api_m_la_type, api_site_name]

        return api_list

    def get_by_id_api(self, apmvalertid):
        api_alert = [apmvalertid['apmvAlertId']]
        api_live_agent = [apmvalertid['liveAgentId']]
        api_worktitle = [apmvalertid['workTitle']]
        api_name = [apmvalertid['name']]

        api_list = [api_alert, api_live_agent, api_worktitle, api_name]

        return api_list

    def get_by_id_db(self, alerts_db):
        db_alertid = [i['ApmvId'] for i in alerts_db]
        db_profile_id = [i['FK_LiveAgentId'] for i in alerts_db]
        db_work_title = [i['WorkTitle'] for i in alerts_db]
        db_name = [i['LiveAgentName'] for i in alerts_db]

        db_list = [db_alertid, db_profile_id, db_work_title, db_name]

        return db_list

    def get_by_liveagentid_db(self, live_db):
        db_live_agent = [i['LiveAgentId'] for i in live_db]
        db_connection = [i['FK_ConnectionId'] for i in live_db]
        db_id = [i['Id'] for i in live_db]

        db_list = [db_live_agent, db_connection, db_id]

        return db_list

    def get_by_liveagentid_api(self, live_api):
        api_live_agent = [i['liveAgentId'] for i in live_api]
        api_connection = [i['connectionId'] for i in live_api]
        api_id = [i['name'] for i in live_api]

        api_list = [api_live_agent, api_connection, api_id]

        return api_list

    def get_open_api(self, open_api):
        api_alertid = [i['apmvAlertId'] for i in open_api]
        api_live_agent = [i['liveAgentId'] for i in open_api]
        api_name = [i['name'] for i in open_api]
        api_asset_name = [i['assetName'] for i in open_api]
        api_site_name = [i['siteName'] for i in open_api]

        api_list = [api_alertid, api_live_agent, api_name, api_asset_name, api_site_name]

        frozen_api = {(frozenset(item)) for item in api_list}

        return frozen_api

    def get_open_db(self, open_db):
        db_apmvid = [i['ApmvId'] for i in open_db]
        db_live_agent = [i['FK_LiveAgentId'] for i in open_db]
        db_name = [i['LiveAgentName'] for i in open_db]
        db_asset_name = [i['AssetId'] for i in open_db]
        db_site_name = [i['SiteId'] for i in open_db]

        db_list = [db_apmvid, db_live_agent, db_name, db_asset_name, db_site_name]

        frozen_db = {(frozenset(item)) for item in db_list}

        return frozen_db


