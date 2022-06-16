from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class Apm_Workitems(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_workitem_all(self):
        sql = f"SELECT * FROM [apmv].[ApmvWorkItem]"
        return self.db_helper.execute_select(sql)

    def get_workitem_byid(self, WorkItemId):
        sql = f"SELECT * FROM [apmv].[ApmvWorkItem] WHERE WorkItemId={WorkItemId}"
        return self.db_helper.execute_select(sql)