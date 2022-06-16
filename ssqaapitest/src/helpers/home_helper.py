from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class Endpoints_home(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_db(self):
        return self.requests_utility.get(f"Database/Status")

    def get_license(self):
        return self.requests_utility.get(f"License/Status")
