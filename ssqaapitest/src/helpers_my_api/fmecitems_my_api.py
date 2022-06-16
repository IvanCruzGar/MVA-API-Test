from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class Endpoints_fmecitems(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_api_fmecitems(self):
        return self.requests_utility.get(f"FmecaItems/GetFmecaItems")

    def get_api_fmecagroupsitems(self):
        return self.requests_utility.get(f"FmecaItems/GetFmecaGroupsItems")
