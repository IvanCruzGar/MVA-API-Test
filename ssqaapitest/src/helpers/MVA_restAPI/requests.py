from ssqaapitest.src.utilities.requestsMVUtility import RequestsMVUtility
from ssqaapitest.src.utilities.jsonUtility import JsonUtility
import pdb
import logging as logger
import json

#http://172.22.4.151:8080/Aspentech/APM/TSDConsumerService/swagger/index.html
class Endpoints(object):

    def __init__(self):
        self.requests_utility = RequestsMVUtility()
        self.json_Utility = JsonUtility('TSD_ConsumerService')
        
    def get_DSList(self):
        api_res = self.requests_utility.restApiCall("/DataSource/List")
        # with open('DSList_otro.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        
        return api_res

    def get_ModelList(self):
        api_res = self.requests_utility.restApiCall("/Model/List")
        # with open('ModelList_otro.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        return api_res

    def get_ConfigurationList(self):
        api_res = self.requests_utility.restApiCall("/Configuration/List")
        # with open('ConfigurationList_otro.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        return api_res
    
    

