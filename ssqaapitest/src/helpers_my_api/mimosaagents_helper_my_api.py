from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class EndpointsMimosaAgents(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_mimosa_agents(self):
        return self.requests_utility.get(f"MimosaAgents/GetMimosaAgents")