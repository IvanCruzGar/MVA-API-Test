from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb
import logging as logger

class dbConnection(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_DataSet(self, dbParams = None):
        sql = f'SELECT * FROM {self.db_helper.creds["db_database"]}.[dbo].[DataSource] '
        sql += self.db_helper.add_condition_where(dbParams)
        return self.db_helper.execute_select(sql)

    def get_TimeSeriesData(self, select= None, dbParams = None, groupBy = None):
        sql = self.db_helper.add_select_columns(select)
        sql += f'FROM {self.db_helper.creds["db_database"]}.[tsd].[TimeSeriesData] '
        sql += self.db_helper.add_condition_where(dbParams)
        sql += self.db_helper.add_GroupBy(groupBy)
        return self.db_helper.execute_select(sql)