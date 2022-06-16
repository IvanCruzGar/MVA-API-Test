import requests
import json
from ssqaapitest.src.configs.hosts_config import API_HOSTS
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import logging as logger

class RequestsMVUtility(object):
    def __init__(self, bearerToken = None):
        
        self.base_url = API_HOSTS['MVApp']
        self.bearerToken = bearerToken
        auth= "/auth/LogIn"
        params = json.dumps({"username" : "TestApi", "password" : "Aspen101"})
        response = requests.post(self.base_url+auth, data = params)
        decoded_data = response.content.decode('utf-8-sig')
        data = json.loads(decoded_data)
        self.AccessToken = data['AccessToken']
        logger.debug(self.AccessToken)
        
        self.requesUtility = RequestsUtility(bearerToken=self.AccessToken)



    def restApiCall(self,endpoint):
        head = {'AccessToken': self.AccessToken}
        response = requests.get(self.base_url+endpoint, headers=head)
        #logger.debug(response.content)
        #logger.debug('Respuesta')
        #response2 = self.requesUtility.get('DataSource/List')
        #logger.debug(response2)
        return response.content.decode('utf-8-sig')

    