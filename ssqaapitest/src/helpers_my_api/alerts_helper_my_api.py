from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class Endpoints_Alerts(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_api_alerts_ids(self):
        return self.requests_utility.get(f"Alert/GetIds")

    def get_api_get_alerts(self):
        api_alerts = self.requests_utility.get("Alert/GetAlert")
        #api_sorted = sorted(api_alerts, key=lambda k: k['alertId'], reverse=False)
        return api_alerts

    def get_api_get_all(self):
        api_alerts = self.requests_utility.get("Alert/GetAll")
        #api_sorted = sorted(api_alerts, key=lambda k: k['alertId'], reverse=False)
        return api_alerts

    def get_api_open(self):
        api_open = self.requests_utility.get("Alert/GetOpen")
        return api_open

    def get_by_id(self, apmvalertid):
        api_alerts = self.requests_utility.get(f"Alert/GetById/{apmvalertid}")
        return api_alerts

    def get_api_alert_tag_rankings(self, tag_api):
        api_alerts = self.requests_utility.get(f"Alert/GetAlertTagRanking/{tag_api}")
        api_sorted = sorted(api_alerts, key=lambda k: k['tagReferenceId'], reverse=False)
        return api_sorted

    def get_by_liveaget_db(self, live_id):
        api_alerts = self.requests_utility.get(f"Alert/GetByLiveAgentId/{live_id}")
        return api_alerts

    def get_work_items(self, getwork_id):
        api_alerts = self.requests_utility.get(f"Alert/GetWorkItems?apmvAlertId={getwork_id}")
        return api_alerts

