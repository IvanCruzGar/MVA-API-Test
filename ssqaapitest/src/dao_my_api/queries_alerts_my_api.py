from ssqaapitest.src.utilities.dbUtility import DBUtility
import pdb


class Apm_Alerts(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_alerts_ids(self):
        sql = f'SELECT * FROM [APMInsights_MVT_mvt-ins-c-d1].apmv.ApmvAlert;'
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_open(self):
        sql = f'SELECT * FROM [APMInsights_MVT_mvt-ins-c-d1].apmv.ApmvAlert WHERE ClosedByName IS NULL;'
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_alerts_tag_rank(self, tag_id):
        sql = f'SELECT * FROM [CBM].[AlertTagRankings] WHERE FK_AlertId = {tag_id} ORDEr BY FK_TagReferenceId ASC'
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_alerts_by_id(self, alert_id):
        sql = f'SELECT * FROM [APMInsights_MVT_mvt-ins-c-d1].apmv.ApmvAlert WHERE ApmvId = {alert_id}'
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_liveagent_id(self, apmvliveAgentid):
        sql = f"SELECT * FROM [apmv].ApmvLiveAgent WHERE ApmvId = {apmvliveAgentid}"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql
