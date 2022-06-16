from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class Endpoints_Asset(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_asset(self):
        return self.requests_utility.get(f"Assets")

    def get_asset_id(self, asset_id):
        return self.requests_utility.get(f"Assets/{asset_id}")

    def get_asset_object(self, object_id):
        return self.requests_utility.get(f"Assets/{object_id}/Objects")

    def get_asset_alerts(self, alerts_id):
        return self.requests_utility.get(f"Assets/{alerts_id}/Alerts")

    def get_live_agents(self, live_id):
        return self.requests_utility.get(f"Assets/{live_id}/LiveAgents")
