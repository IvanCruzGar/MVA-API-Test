from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class Apm_Objects(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_objects(self, object_id):
        sql = f'SELECT * FROM [RCM].[tbl_Object] where Disabled = {object_id}'
        return self.db_helper.execute_select(sql)

    def get_objects_enterprise(self, nodetype, disable):
        sql = f'SELECT * FROM [RCM].[tbl_Object] where NodeType = {nodetype} and Disabled = {disable}'
        return self.db_helper.execute_select(sql)

    def get_object_site(self, nodetype, disable):
        sql = f'SELECT * FROM [RCM].[tbl_Object] where NodeType = {nodetype} and Disabled = {disable}'
        return self.db_helper.execute_select(sql)

    def get_object_segment(self, nodetype, disable):
        sql = f"SELECT * FROM [RCM].[tbl_Object] where NodeType = {nodetype} and Disabled = {disable}"
        return self.db_helper.execute_select(sql)

    def get_object_asset(self, nodetype, disable):
        sql = f"SELECT * FROM [RCM].[tbl_Object] where NodeType = {nodetype} and Disabled = {disable}"
        return self.db_helper.execute_select(sql)

    def get_object_id(self):
        sql = f"SELECT * FROM [RCM].[tbl_Object]"
        return self.db_helper.execute_select(sql)

    def get_object_row_id(self, row_id):
        sql = f"SELECT * FROM [RCM].[tbl_Object] WHERE ObjectUid = {row_id}"
        return self.db_helper.execute_select(sql)

    def get_object_site_row_id(self, disabled):
        sql = f"SELECT * FROM [RCM].[tbl_Object] where Disabled = {disabled} and ObjectType = 'Site'"
        return self.db_helper.execute_select(sql)

    def get_object_live_agents(self):
        sql = f"SELECT * FROM [CBM].[Profile]"
        return self.db_helper.execute_select(sql)

    def get_object_alert(self):
        sql = f"SELECT * FROM [CBM].[Alert] ORDER BY AlertId DESC" #  ORDER BY AlertId DESC
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql
