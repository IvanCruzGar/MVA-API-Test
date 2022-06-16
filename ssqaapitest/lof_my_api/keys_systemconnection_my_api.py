import pdb


class Values_SConnection(object):

    def get_system_connection_db(self, sconnection_db):
        db_connectionid = [i['ConnectionId'] for i in sconnection_db]
        db_apitype = [i['APIType'] for i in sconnection_db]
        db_api_id = [i['APIDescription'] for i in sconnection_db]
        #db_licenced = [i['Licenced'] for i in sconnection_db]
        #db_status = [i['Status'] for i in sconnection_db]
        #db_dbstatusmjs = [i['DatabaseStatusMessage'] for i in sconnection_db]

        db_list = [db_connectionid, db_apitype, db_api_id]
        return db_list

    def get_system_connection_api(self, sconnection_api):
        api_connectionid = [sconnection_api['connectionId']]
        api_apitype = [sconnection_api['apitype']]
        api_api_id = [sconnection_api['connectionName']]
        #api_licenced = [sconnection_api['licensed']]
        #api_status = [sconnection_api['status']]
        # api_dbstatusmjs = [i['databaseStatusMessage'] for i in sconnection_db]

        api_list = [api_connectionid, api_apitype, api_api_id]
        return api_list

    def get_system_connection_all_db(self, connection_db):
        db_connection_id = [i['ConnectionId'] for i in connection_db]
        db_api_type = [i['APIType'] for i in connection_db]
        db_api_id = [i['APIDescription'] for i in connection_db]

        db_list = [db_connection_id, db_api_type, db_api_id]
        return db_list

    def get_system_connection_all_api(self, connection_api):
        api_connection_id = [i['connectionId'] for i in connection_api]
        api_api_type = [i['apitype'] for i in connection_api]
        api_api_id = [i['connectionName'] for i in connection_api]

        api_list = [api_connection_id, api_api_type, api_api_id]
        return api_list