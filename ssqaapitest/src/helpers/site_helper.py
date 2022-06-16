from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class Endpoints_Site(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_objects(self):
        return self.requests_utility.get(f"Sites")

    def get_dates(self):
        return self.requests_utility.get(f"Sites/IntervalOfDates")

    def get_ids(self):
        return self.requests_utility.get(f"Sites/Ids")

    def get_rows_ids(self, row_id):
        return self.requests_utility.get(f"Sites/{row_id}")

    def get_object(self, row_id):
        return self.requests_utility.get(f"Sites/{row_id}/Objects")

    def get_alerts(self, row_id):
        api_alerts = self.requests_utility.get(f"Sites/{row_id}/Alerts")
        api_sorted = sorted(api_alerts, key=lambda k: k['RowId'], reverse=False)
        return api_sorted

    def get_live_agents(self, row_id):
        return self.requests_utility.get(f"Sites/{row_id}/LiveAgents")
