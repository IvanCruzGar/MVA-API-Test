from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class Endpoints_Objects(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_objects(self):
        return self.requests_utility.get(f"Objects")

    def get_objects_enterprise(self):
        return self.requests_utility.get(f"Objects?type=Enterprise")

    def get_objects_site(self):
        return self.requests_utility.get(f"Objects?type=site")

    def get_objects_segment(self):
        return self.requests_utility.get(f"Objects?type=Segment")

    def get_objects_asset(self):
        return self.requests_utility.get(f"Objects?type=Asset")

    def get_objects_id(self):
        return self.requests_utility.get(f"Objects/Ids")

    def get_object_date(self):
        return self.requests_utility.get(f"Objects/IntervalOfDates")

    def get_object_row_id(self, row_id):
        return self.requests_utility.get(f"Objects/{row_id}")

    def get_object_row_id_object(self, row_id):
        return self.requests_utility.get(f"/Objects/{row_id}/Objects")

    def get_object_parent(self, row_id):
        return self.requests_utility.get(f"Objects/{row_id}/Parent")

    def get_object_site(self, row_id):
        return self.requests_utility.get(f"Objects/{row_id}/Site")

    def get_object_live_agent(self, row_id):
        return self.requests_utility.get(f"Objects/{row_id}/LiveAgents")

    def get_object_alerts(self, row_id):
        return self.requests_utility.get(f"Objects/{row_id}/Alerts")

