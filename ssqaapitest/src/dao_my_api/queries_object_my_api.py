from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class ApmObjects(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_object_workitems_related(self, fk_apmvObjectId):
        sql = f'SELECT * FROM [apmv].[ApmvWorkItem] WHERE FK_ApmvObjectId= {fk_apmvObjectId}'
        return self.db_helper.execute_select(sql)

    def get_object(self):
        sql = f'SELECT * FROM [apmv].[ApmvObject]'
        return self.db_helper.execute_select(sql)

    def get_object_alerts_related(self, apmvid):
        sql = f'SELECT * FROM [apmv].[ApmvObject] as m join apmv.ApmvAlert as t on m.Id=t.SiteId WHERE m.ApmvId = {apmvid}'
        return self.db_helper.execute_select(sql)

    def get_object_get_by_alert(self, apmvid):
        sql = f'SELECT * FROM [apmv].[ApmvObject] as m join apmv.ApmvAlert as t on m.ApmvId=t.ApmvObjectId WHERE t.ApmvId = {apmvid}'
        return self.db_helper.execute_select(sql)