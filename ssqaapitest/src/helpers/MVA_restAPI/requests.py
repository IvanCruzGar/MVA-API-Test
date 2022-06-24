
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
from ssqaapitest.src.utilities.jsonUtility import JsonUtility
from ssqaapitest.src.configs.hosts_config import API_HOSTS
import requests
import pdb
import logging as logger
import json

#http://172.22.4.151:8080/Aspentech/APM/TSDConsumerService/swagger/index.html
class Endpoints(object):

    def __init__(self):
        
        
        self.requestUtility = RequestsUtility()
        auth= "/auth/LogIn"
        otroNombre = {"username" : "TestApi", "password" : "Aspen101"}
        
        response = self.requestUtility.post('/auth/LogIn', payload=otroNombre)
        #logger.debug('Esto salio: '+str(response))
        self.AccessToken = response['AccessToken']
        
        self.requestUtility.AccessToken = self.AccessToken

        
    def get_DSList(self):
        api_res = self.requestUtility.get("/DataSource/List")
        # with open('DSList_new.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        logger.debug(api_res)
        return api_res

    def get_ModelList(self):
        api_res = self.requestUtility.get("/Model/List")
        with open('ModelList_new.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('Quedo tu archivo chavo')
        return api_res

    def get_ConfigurationList(self):
        api_res = self.requestUtility.get("/Configuration/List")
        with open('ConfigurationList_new.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('Quedo tu archivo chavo')
        return api_res
    
    

