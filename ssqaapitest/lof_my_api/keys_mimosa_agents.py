class ValuesMimosaAgents(object):

    def assets_mimosa_agents_db(self, asset_db):
        db_fk_connection_id = [i['FK_ConnectionId'] for i in asset_db]
        db_enterprise_id = [i['EnterpriseId'] for i in asset_db]
        db_site_id = [i['SiteId'] for i in asset_db]
        db_display_name = [i['DisplayName'] for i in asset_db]
        db_type_code = [i['TypeCode'] for i in asset_db]
        db_type_database_id = [i['TypeDatabaseId'] for i in asset_db]
        db_id = [i['Id'] for i in asset_db]
        db_description = [i['Description'] for i in asset_db]

        db_list = [db_fk_connection_id, db_enterprise_id, db_site_id, db_display_name, db_type_code,
                   db_type_database_id, db_id, db_description]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

    def assets_mimosa_agents_api(self, asset_api):
        api_fk_connection_id = [i['fkConnectionId'] for i in asset_api]
        api_enterprise_id = [i['enterpriseId'] for i in asset_api]
        api_site_id = [i['siteId'] for i in asset_api]
        api_display_name = [i['displayName'] for i in asset_api]
        api_type_code = [i['typeCode'] for i in asset_api]
        api_type_database_id = [i['typeDatabaseId'] for i in asset_api]
        api_id = [i['id'] for i in asset_api]
        api_description = [i['description'] for i in asset_api]

        api_list = [api_fk_connection_id, api_enterprise_id, api_site_id, api_display_name, api_type_code,
                    api_type_database_id, api_id, api_description]

        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api