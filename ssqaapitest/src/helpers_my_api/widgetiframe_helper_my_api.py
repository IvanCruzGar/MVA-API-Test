from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class Endpoints_WidgetIframe(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_api_widgetiframe(self):
        api_get = self.requests_utility.get(f"WidgetIframe/GetAll")
        return api_get


