from ssqaapitest.src.utilities.dbUtility import DBUtility
import random
import pdb


class Apm_Live_agents(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_live_agents(self):
        sql = f'SELECT * FROM [CBM].[Profile]'
        return self.db_helper.execute_select(sql)

    def get_live_agents_cm(self, agent_id):
        sql = f'SELECT * FROM [CBM].[Profile] where ProfileType = {agent_id}'
        return self.db_helper.execute_select(sql)

    def get_live_agents_pm(self, agent_id):
        sql = f'SELECT * FROM [CBM].[Profile] where ProfileType = {agent_id}'
        return self.db_helper.execute_select(sql)

    def get_live_agent_rp(self, agent_id):
        sql = f'SELECT * FROM [CBM].[Profile] where ProfileType = {agent_id}'
        return self.db_helper.execute_select(sql)

    def get_live_agent_ml(self, agent_id):
        sql = f'SELECT * FROM [CBM].[Profile] where ProfileType = {agent_id}'
        return self.db_helper.execute_select(sql)

    def get_live_agent_row(self, agent_id):
        sql = f'SELECT * FROM [CBM].[Profile] WHERE ProfileId  = {agent_id}'
        return self.db_helper.execute_select(sql)

    def get_live_agent_alert(self, id_alert):
        sql = f"SELECT * FROM [CBM].[Alert] WHERE FK_ProfileId = {id_alert}"
        return self.db_helper.execute_select(sql)

    def get_live_agent_object(self, object_id):
        sql = f"SELECT * FROM [RCM].[tbl_Object] WHERE ObjectUid = {object_id}"
        return self.db_helper.execute_select(sql)

    def get_live_agent_tags(self, tag_id):
        sql = f'SELECT FK_TagReferenceId, TagName FROM [RCM].[tbl_MachineLearningProfileTagMappings] WHERE ' \
              f'FK_MachineLearningProfileId = {tag_id}'
        return self.db_helper.execute_select(sql)
