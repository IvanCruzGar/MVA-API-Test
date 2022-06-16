from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger

class Endpoints_Workitems(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_work_items(self):
        api_workitems = self.requests_utility.get(f"WorkItem/GetWorkItem")
        api_sorted = sorted(api_workitems, key=lambda k: k['apmvId'], reverse=False)
        return api_sorted

    def get_work_item_ids(self):
        return self.requests_utility.get(f"WorkItems/Ids")

    def get_api_workitemsbyid(self, rowId, aconnectionId):
        api_workitems = self.requests_utility.get(f"WorkItem/GetById?rowId={rowId}&connectionId={aconnectionId}")
        return api_workitems

