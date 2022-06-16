from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class EndpointsTagRankings(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_api_tag_rankings(self):
        api_get = self.requests_utility.get(f"TagRankings/GetTagRankings")
        api_sorted = sorted(api_get, key=lambda k: k['apmvId'], reverse=False)
        return api_sorted