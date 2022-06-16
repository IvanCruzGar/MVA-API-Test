from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class EndpointsLiveAgents(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_live_agent(self):
        return self.requests_utility.get(f"LiveAgent/GetLiveAgent")

    def get_live_agent_ids(self):
        return self.requests_utility.get(f"LiveAgent/GetIds")

    def get_live_agent_apmvalertid(self, apmvalertid):
        return self.requests_utility.get(f"LiveAgent/GetByAlertId/{apmvalertid}")





