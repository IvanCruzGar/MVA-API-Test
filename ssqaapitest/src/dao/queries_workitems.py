from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class Apm_Workitems(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_work_items(self):
        sql = f'SELECT * FROM [RCM].[tbl_WorkItem]'
        return self.db_helper.execute_select(sql)
