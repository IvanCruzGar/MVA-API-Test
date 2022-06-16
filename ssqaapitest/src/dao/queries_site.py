from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class Apm_Site(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_site(self, parent_id):
        sql = f'SELECT * FROM [RCM].[tbl_Object] where ParentUid = {parent_id} ORDER BY ObjectUid ASC'
        return self.db_helper.execute_select(sql)

    def get_site_row_ids(self, objectuid):
        sql = f"SELECT * FROM [RCM].[tbl_Object] where ObjectUid = {objectuid}"
        return self.db_helper.execute_select(sql)

    def get_site_objects(self):
        sql = f"SELECT * FROM [RCM].[tbl_Object] where ParentMimosaSiteCode = 0000000100000004"
        return self.db_helper.execute_select(sql)

    def get_site_alerts(self):
        sql = f"SELECT * FROM [CBM].[Alert]  WHERE AlertId = 4 OR AlertId = 5 OR AlertId = 15 OR AlertId = 16 OR " \
              f"AlertId = 17 OR AlertId = 18 OR AlertId = 19 OR AlertId = 20 OR AlertId = 21"
        return self.db_helper.execute_select(sql)

    def get_site_live_agent(self, site_id):
        sql = f"SELECT * FROM [CBM].[Profile] where SiteId = {site_id}"
        return self.db_helper.execute_select(sql)

