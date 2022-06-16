from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class Endpoints_Workitems(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_work_items(self):
        return self.requests_utility.get(f"WorkItems")

    def get_work_item_ids(self):
        return self.requests_utility.get(f"WorkItems/Ids")
