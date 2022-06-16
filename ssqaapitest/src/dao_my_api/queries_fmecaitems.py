from ssqaapitest.src.utilities.dbUtility import DBUtility
import pdb


class Apm_fmecaitems(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_string_mapping(self):
        sql = f'SELECT * FROM [mtell].[FmecaItem]'
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql


