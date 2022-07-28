
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
        otroNombre = {"username" : "API1", "password" : "Aspen100"}
        
        response = self.requestUtility.post('/auth/LogIn', payload=otroNombre)
        #logger.debug('Esto salio:')
        #logger.debug(response)
       
        
        self.requestUtility.accessToken = response['AccessToken']
        
        

     
    def get_WEndP(self):
        api_res = self.requestUtility.get("/DataSource/Listo", expected_status_code = 404, resEmpty = True)
        with open('Error_header.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res

    def get_DSList(self):
        api_res = self.requestUtility.get("/DataSource/List")
        # with open('DSList_new.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res

    def get_ModelList(self):
        api_res = self.requestUtility.get("/Model/List")
        # with open('ModelList_new.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res

    def get_ConfigurationList(self):
        api_res = self.requestUtility.get("/Configuration/List")
        # with open('ConfigurationList_new.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res

    def get_ConfRunList(self):
        api_res = self.requestUtility.get("/Configuration/RunsList?ConfigurationId=1")
        # with open('ConfRunsList.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        # logger.debug(api_res)
        return api_res

    def get_RawDataID(self):
        api_res = self.requestUtility.get("/Configuration/RawData?ConfigurationRunId=1")
        # with open('RawDataID.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res
    def get_RawDataFNR(self):
        api_res = self.requestUtility.get("/Configuration/RawData?ConfigurationRunId=1&FirstNRows=5")
        # with open('RawDataFNR.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res
    def get_RawDataOFF(self):
        api_res = self.requestUtility.get("/Configuration/RawData?ConfigurationRunId=1&Offset=5&Rows=5")
        # with open('RawDataOFF.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res
    def get_RModelMetaMRID(self):
        api_res = self.requestUtility.get("/model/metadata?modelRevisionId=14")
        # with open('ModelMetaID.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res
    #
    def get_RRMNFull(self):
        api_res = self.requestUtility.get("/Configuration/ResultMatrices?configurationId=2?MatrixName=HotellingsT2")
        # with open('ResMatFull.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res

    def get_RRMConfRun(self):
        api_res = self.requestUtility.get("/Configuration/ResultTypes?configurationRunId=14")
        # with open('ResMatConfRun.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res

    def get_RDSMetaDSId(self):
        api_res = self.requestUtility.get("/datasource/metadata?datasourceRevisionId=1")
        # with open('RDSMbyDSid.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res

    def get_RConfMetaConfId(self):
        api_res = self.requestUtility.get("/Configuration/Metadata?configurationRevisionId=1")
        # with open('RConfMetaConfId.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res


    def get_RRMatricesNameFullList(self):
        api_res = self.requestUtility.get("/Configuration/ResultMatrices?configurationId=1?MatrixName=Scores", expected_status_code = 200, resEmpty = True)
        # with open('RConfMetaConfId.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('Quedo tu archivo chavo')
        #logger.debug(api_res)
        return api_res
