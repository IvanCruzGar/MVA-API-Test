import logging as logger
from typing import Dict
import pymssql
from ssqaapitest.src.utilities.credentialsUtility import CredentialsUtility

import pdb


class DBUtility(object):

    #TO DO Manage credentials by user or by environment
    def __init__(self):
        creds_helper = CredentialsUtility()
        #self.creds = creds_helper.get_user_credentials(ip='172.22.4.151', dbName= 'MtellReservoir04152022') #alpha1
        self.creds = creds_helper.get_user_credentials(ip=creds_helper.get_local_ip(), dbName= 'AspenProcessPulse')

    def create_connection(self):
        connection = pymssql.connect(server=self.creds['db_ip'], port=self.creds['db_port'], user=self.creds['db_user'],
                                     password=self.creds['db_password'], database=self.creds["db_database"],
                                     charset=self.creds["db_charset"], autocommit=True)
        return connection

    #Implement Where as a parameter, need to manage what happen if the sql parameter has a ; maybe replace it
    def execute_select(self, sql):

        conn = self.create_connection()
        if sql[-1] != ';':
            sql += ';'
        try:
            logger.debug(f"Executing: {sql}")
            cur = conn.cursor(as_dict=True)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql}\n |.Error: {str(e)}")
        finally:
            conn.close()
        return rs_dict

    def execute_sql(self, sql):
        pass

    def add_select_columns(self, columns = None):
        if not (type(columns) == list or type(columns) == str):
            return 'SELECT * '
        query = 'SELECT '
        if (type(columns) == str):
            query += columns + ' '
            return query
        for column in columns:
            query += column + ' '
        return query

    def add_condition_where(self, conditionsDict):
        if (type(conditionsDict) != dict):
            return ''
        query = 'WHERE '
        addAnd = False
        for key, value in conditionsDict.items():
            if addAnd:
                query += 'AND '
            query += f"{key} = '{value}' "
            addAnd = True
        return query

    def add_GroupBy(self, column):
        if (type(column) != str):
            return ''
        query = ' Group By ' + column
        return query


