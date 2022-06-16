from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class Endpoints_mappings(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_api_mappings(self):
        return self.requests_utility.get(f"ApmvStringMapping/GetApmvStringMapping")
