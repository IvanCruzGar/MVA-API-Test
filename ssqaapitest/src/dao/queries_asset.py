from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class Apm_Asset(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_assets(self):
        sql = f'SELECT * FROM [RCM].[tbl_Object] where NodeType = 3 and Disabled = 0;'
        return self.db_helper.execute_select(sql)

    def get_assets_id(self, asset_id):
        sql = f'SELECT * FROM [RCM].[tbl_Object] WHERE ObjectUid = {asset_id}'
        return self.db_helper.execute_select(sql)

    def get_assets_objects(self, parent_id):
        sql = f'SELECT * FROM [RCM].[tbl_Object] WHERE ParentUid = {parent_id}'
        return self.db_helper.execute_select(sql)

    def get_assets_alerts(self):
        sql = f"SELECT * FROM [CBM].[Alert] ORDER BY AlertId DESC " #ORDER BY AlertId DESC
        return self.db_helper.execute_select(sql)

    def get_live_agent(self):
        sql = f"SELECT * FROM [CBM].[Profile]"
        return self.db_helper.execute_select(sql)


    def get_all_alerts_tagrankings(self, alert_id):
        sql = f"SELECT * FROM [CBM].[AlertTagRankings] WHERE FK_AlertId = {alert_id}"
        rs_sql = self.db_helper.execute_select(sql)
        rs_sql = sorted(rs_sql, key=lambda k: k['FK_TagReferenceId'], reverse=False)
        return rs_sql
