from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class Endpoints_Live_agents(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_live_agent(self):
        return self.requests_utility.get(f"LiveAgents")

    def get_live_agent_all(self):
        return self.requests_utility.get("LiveAgents?type=all")

    def get_live_agent_cm(self):
        return self.requests_utility.get("LiveAgents?type=CM")

    def get_live_agent_pm(self):
        return self.requests_utility.get("LiveAgents?type=PM")

    def get_live_agent_rp(self):
        return self.requests_utility.get("LiveAgents?type=RulePolicy")

    def get_live_agent_ml(self):
        return self.requests_utility.get("LiveAgents?type=MachineLearning")

    def get_live_agent_row(self, rowid):
        return self.requests_utility.get(f'LiveAgents/{rowid}')

    def get_live_dates(self):
        return self.requests_utility.get(f'LiveAgents/IntervalOfDates')

    def get_live_ids(self, id):
        return self.requests_utility.get(f'LiveAgents/Ids?changedSince={id}')

    def get_live_alerts(self, rowid):
        return self.requests_utility.get(f'LiveAgents/{rowid}/Alerts')

    def get_live_alerts_objects(self, objectid):
        return self.requests_utility.get(f'LiveAgents/{objectid}/Object')

    def get_live_tags(self, tagsid):
        return self.requests_utility.get(f'LiveAgents/{tagsid}/Tags')

    def get_live_lead_time(self, rowid):
        return self.requests_utility.get(f'LiveAgents/{rowid}/LeadTimeAverage')

    def get_live_all_lead_time(self):
        return self.requests_utility.get(f'LiveAgents/AllLeadTimeAverages')
