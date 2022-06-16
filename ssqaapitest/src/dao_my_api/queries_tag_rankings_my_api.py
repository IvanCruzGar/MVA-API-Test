from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class ApmTagRankings(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_tag_rankings(self):
        sql = f'SELECT * FROM [apmv].[ApmvTagRankings]'
        return self.db_helper.execute_select(sql)