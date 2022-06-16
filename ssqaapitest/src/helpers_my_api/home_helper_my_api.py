from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb


class EndpointsHome(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_home_status(self):
        return self.requests_utility.get(f"Home/Status")


