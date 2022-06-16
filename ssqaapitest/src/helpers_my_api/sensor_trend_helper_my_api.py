from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb


class Endpoint_sensor_trend(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_sensor_trend_cm(self, apmvAlertId):
        return self.requests_utility.get(f"SensorTrend/GetCMSensorTrend?apmvAlertId={apmvAlertId}")

    def get_sensor_trend_rp(self, apmvAlertId):
        return self.requests_utility.get(f"SensorTrend/GetRulePolicyTrend?apmvAlertId={apmvAlertId}")

