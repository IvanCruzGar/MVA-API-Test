class ValuesObject(object):

    def assets_object_db(self, asset_db):
        db_apmvid = [i['ApmvId'] for i in asset_db]
        db_id = [i['Id'] for i in asset_db]
        db_name = [i['Name'] for i in asset_db]

        db_list = [db_apmvid, db_id, db_name]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

    def assets_object_api(self, asset_api):
        api_apmv_object_id = [i['apmvObjectId'] for i in asset_api]
        api_id = [i['id'] for i in asset_api]
        api_name = [i['name'] for i in asset_api]

        api_list = [api_apmv_object_id, api_id, api_name]

        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api

    def assets_object_db_list(self, asset_db):
        db_site_name = [i['SiteName'] for i in asset_db]
        db_live_agent_name = [i['LiveAgentName'] for i in asset_db]
        db_live_agent_type_string = [i['LiveAgentTypeString'] for i in asset_db]
        db_asset_id = [i['AssetId'] for i in asset_db]

        db_list = [db_site_name, db_live_agent_name,
                   db_live_agent_type_string, db_asset_id, ]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

    def assets_object_api_list(self, asset_api):
        api_site_name = [i['siteName'] for i in asset_api]
        api_live_agent_name = [i['liveAgentName'] for i in asset_api]
        api_live_agent_type_string = [i['liveAgentTypeString'] for i in asset_api]
        api_asset_id = [i['assetId'] for i in asset_api]

        api_list = [api_site_name, api_live_agent_name,
                    api_live_agent_type_string, api_asset_id]

        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api

    def object_db_list(self, asset_db):
        db_name = [i['Name'] for i in asset_db]
        db_id = [i['AssetId'] for i in asset_db]
        db_apmv_id = [i['ApmvObjectId'] for i in asset_db]

        db_list = [db_name, db_id, db_apmv_id]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

    def object_api_list(self, asset_api):
        api_name = [i['name'] for i in asset_api]
        api_id = [i['id'] for i in asset_api]
        api_apmv_object_id = [i['apmvObjectId'] for i in asset_api]

        api_list = [api_name, api_id, api_apmv_object_id]

        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api

    def get_workitems_object_db(self, objects_db):
        db_object_id = [i['WorkItemStrId'] for i in objects_db]
        db_object_worktitle = [i['WorkItemTitle'] for i in objects_db]
        db_object_problemcode = [i['ProblemCode'] for i in objects_db]

        db_list = [db_object_id, db_object_worktitle, db_object_problemcode]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}
        return frozen_live_a_db

    def get_workitems_object_api(self, objects_api):
        api_strid = [i['workItemStrId'] for i in objects_api]
        api_title = [i['workItemTitle'] for i in objects_api]
        api_code = [i['problemCode'] for i in objects_api]

        api_list = [api_strid, api_title, api_code]

        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api

    def get_object_db(self, objects_db):
        db_object_apmvid = [i['ApmvId'] for i in objects_db]
        db_object_id = [i['Id'] for i in objects_db]
        db_object_name = [i['Name'] for i in objects_db]

        db_list = [db_object_apmvid, db_object_id, db_object_name]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}
        return frozen_live_a_db

    def get_object_api(self, objects_api):
        api_object_apmvid = [i['apmvId'] for i in objects_api]
        api_object_id = [i['id'] for i in objects_api]
        api_object_name = [i['name'] for i in objects_api]

        api_list = [api_object_apmvid, api_object_id, api_object_name]

        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api