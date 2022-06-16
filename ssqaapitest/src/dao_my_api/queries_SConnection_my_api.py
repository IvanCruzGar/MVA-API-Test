from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class Apm_SConnection(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_connection_id(self):
        sql = f"SELECT * FROM [RCM].[tbl_Object]"
        return self.db_helper.execute_select(sql)

    def get_connectionbyid(self, connectionId):
        # sql = f'SELECT * FROM [RCM].[tbl_WorkItem] WHERE FK_ObjectUid= {workitem_id}'
        sql = f'SELECT * FROM [dbo].[ConnectionSettings] WHERE ConnectionId = {connectionId}'
        return self.db_helper.execute_select(sql)

    def get_system_connection(self):
        sql = f"SELECT * FROM [dbo].[ConnectionSettings]"
        return self.db_helper.execute_select(sql)
