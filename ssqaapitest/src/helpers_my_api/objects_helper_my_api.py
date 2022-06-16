from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class EndpointsObjects(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_api_objects(self):
        api_get = self.requests_utility.get(f"Object/GetObject")
        api_sorted = sorted(api_get, key=lambda k: k['apmvId'], reverse=False)
        return api_sorted

    def get_api_workitemsrelated(self, apmvobjectid_api):
        api_workitems = self.requests_utility.get(f"Object/WorkItemsRelated?apmvObjectId={apmvobjectid_api}")
        api_sorted = sorted(api_workitems, key=lambda k: k['apmvWorkItemId'], reverse=False)
        return api_sorted

    def get_object_all(self):
        return self.requests_utility.get(f"Object/GetAll")

    def get_object_alerts_related(self, apmvobjectid):
        return self.requests_utility.get(f"Object/AlertsRelated?apmvObjectId={apmvobjectid}")

    def get_object_get_by_alert(self, apmvalertid):
        return self.requests_utility.get(f"Object/GetByAlert?apmvAlertId={apmvalertid}")
