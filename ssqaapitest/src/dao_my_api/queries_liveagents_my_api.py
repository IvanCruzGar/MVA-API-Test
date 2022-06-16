from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class ApmLiveAgents(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_live_agent(self):
        sql = f'SELECT * FROM [apmv].[ApmvLiveAgent]'
        return self.db_helper.execute_select(sql)

    def get_live_agent_apmvid(self, ApmvId):
        sql = f'SELECT * FROM [apmv].[ApmvAlert] WHERE ApmvId  = {ApmvId}'
        return self.db_helper.execute_select(sql)