from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class Apm_Alerts(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty=1):
        sql = 'SELECT * FROM local.wp_posts WHERE post_type = "product" LIMIT 5000;'
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(qty))

    def get_product_by_id(self, product_id):
        sql = f'SELECT * FROM local.wp_posts WHERE ID = {product_id};'
        return self.db_helper.execute_select(sql)

    def get_alert_by_id(self):
        sql = f"SELECT * FROM [CBM].[Alert] ORDER BY AlertId DESC" #  ORDER BY AlertId DESC
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_alert_alerts(self):
        sql = f"SELECT * FROM [CBM].[Alert]"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_all_alert(self, intervention_num):
        sql = f"SELECT * FROM [CBM].[Alert] where InterventionType = {intervention_num} AND ClosedBy IS NULL " # ORDER BY AlertId DESC
        #SELECT * FROM [CBM].[Alert] where InterventionType = 0 AND Acked = 0
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_all_alert_rowid(self, alert_id):
        sql = f"SELECT * FROM [CBM].[Alert] WHERE AlertId = {alert_id}"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_all_alerts_tagrankings(self, alert_id):
        sql = f"SELECT * FROM [CBM].[AlertTagRankings] WHERE FK_AlertId = {alert_id}"
        rs_sql = self.db_helper.execute_select(sql)
        rs_sql = sorted(rs_sql, key=lambda k: k['FK_TagReferenceId'], reverse=False)
        return rs_sql

    def get_all_alerts_liveagent(self, profileid):
        sql = f"SELECT * FROM [CBM].[Profile] WHERE profileId = {profileid}"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_products_created_after_given_date(self, _date):
        sql = f'SELECT * FROM local.wp_posts WHERE post_type = "product" AND post_date > "{_date}" LIMIT 5000;'
        return self.db_helper.execute_select(sql)
