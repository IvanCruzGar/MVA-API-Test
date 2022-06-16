from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class Apm_Tag(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_tag_rankings(self):
        sql = f'SELECT * FROM [CBM].[AlertTagRankings]'
        return self.db_helper.execute_select(sql)
