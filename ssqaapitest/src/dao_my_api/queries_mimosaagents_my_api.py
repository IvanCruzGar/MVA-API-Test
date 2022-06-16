from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class ApmMimosaAgents(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_mimosa_agents(self):
        sql = f'SELECT * FROM [mtell].[MimosaAgent]'
        return self.db_helper.execute_select(sql)
