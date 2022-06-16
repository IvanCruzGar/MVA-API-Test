from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb
import logging as logger

class dbConnection(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_CsvFileFormat(self, dbParams = None):
        sql = f'SELECT * FROM {self.db_helper.creds["db_database"]}.[tsd].[CsvFileFormat] '
        sql += self.db_helper.add_condition_where(dbParams)
        return self.db_helper.execute_select(sql)

    def get_DataSourceProfile(self, dbParams = None):
        sql = f'SELECT * FROM {self.db_helper.creds["db_database"]}.[tsd].[DataSourceProfile] '
        sql += self.db_helper.add_condition_where(dbParams)
        return self.db_helper.execute_select(sql)

    def get_TagReference(self, dbParams = None):
        sql = f'SELECT * FROM {self.db_helper.creds["db_database"]}.[tsd].[TagReference] '
        sql += self.db_helper.add_condition_where(dbParams)
        return self.db_helper.execute_select(sql)

    def get_TagReference_Join_DataSource(self, dbParams = None):
        sql = f'select {self.db_helper.creds["db_database"]}.[tsd].[DataSourceProfile].RowId, {self.db_helper.creds["db_database"]}.[tsd].[DataSourceProfile].DataSourceName, {self.db_helper.creds["db_database"]}.[tsd].[TagReference].Id , {self.db_helper.creds["db_database"]}.[tsd].[TagReference].RowId "Tag Id" '
        sql += f'from {self.db_helper.creds["db_database"]}.[tsd].[TagReference] '
        sql += f'Inner Join {self.db_helper.creds["db_database"]}.[tsd].[DataSourceProfile] ON {self.db_helper.creds["db_database"]}.[tsd].[TagReference].FK_DataSourceProfile = {self.db_helper.creds["db_database"]}.[tsd].[DataSourceProfile].RowId'
        sql += self.db_helper.add_condition_where(dbParams)
        return self.db_helper.execute_select(sql)
