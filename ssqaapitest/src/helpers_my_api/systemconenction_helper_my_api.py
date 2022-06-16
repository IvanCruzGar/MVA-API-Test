from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class Endpoints_SConnection(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_systems_connectionid(self, connectionId):
        return self.requests_utility.get(f"SystemConnection/GetById?id={connectionId}")

    def get_system_connection_get_all(self):
        return self.requests_utility.get(f"SystemConnection/GetAll")