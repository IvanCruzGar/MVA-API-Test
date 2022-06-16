from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class Apm_Widgetiframe(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_widgetifram_all(self):
        sql = f"SELECT * FROM [apmv].[ApmvWidgetsIframe]"
        return self.db_helper.execute_select(sql)