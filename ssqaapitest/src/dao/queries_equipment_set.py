from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class Apm_Equipment(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_equipment(self):
        sql = f'SELECT * FROM [RCM].tbl_FailureSetProfile WHERE Disabled = 0;'
        return self.db_helper.execute_select(sql)
