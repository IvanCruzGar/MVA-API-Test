from ssqaapitest.src.utilities.dbUtility import DBUtility
import pdb


class Apm_string_mapping(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_string_mapping(self):
        sql = f'SELECT * FROM [APMInsights_MVT_mvt-ins-c-d1].apmv.ApmvStringMapping;'
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql


