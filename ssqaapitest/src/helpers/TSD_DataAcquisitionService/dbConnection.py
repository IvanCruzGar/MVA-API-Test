from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb
import logging as logger

class dbConnection(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_CycleObject(self, dbParams = None):
        sql = f'SELECT * FROM {self.db_helper.creds["db_database"]}.[tsd].[CycleObject] '
        sql += self.db_helper.add_condition_where(dbParams)
        return self.db_helper.execute_select(sql)