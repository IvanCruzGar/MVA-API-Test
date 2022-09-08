
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
        otroNombre = {"username" : "API1", "password" : "Aspen100"}
        response = self.requestUtility.post('/auth/LogIn', payload=otroNombre)
        logger.debug('Token created')
        logger.debug(response)
       
        
        self.requestUtility.accessToken = response['AccessToken']
        
        

     
    ########

    def get_DSList(self):
        api_res = self.requestUtility.get("/DataSource/List")
        with open('DSList_new.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_ModelList(self):
        api_res = self.requestUtility.get("/Model/List")
        with open('ModelList_new.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_ConfigurationList(self):
        api_res = self.requestUtility.get("/Configuration/List")
        with open('ConfigurationList_new.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_ConfRunList(self):
        api_res = self.requestUtility.get("/Configuration/RunsList?ConfigurationId=1")
        with open('ConfRunsList.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_code404(self):
        api_res = self.requestUtility.get("/DataSource/Listo", expected_status_code=404, resEmpty = True)
        #logger.debug(api_res)
        return api_res

    def get_code401WrongUser(self):
        auth= "/auth/LogIn"
        usuarioincorrecto = {"username" : "WUser", "password" : "Aspen100"}
        api_res = self.requestUtility.post('/auth/LogIn', payload=usuarioincorrecto,expected_status_code=401)
        logger.debug(api_res)
        return api_res

    def get_code401WrongPassword(self):
        auth= "/auth/LogIn"
        usuarioincorrecto = {"username" : "API1", "password" : "Aspen888"}
        api_res = self.requestUtility.post('/auth/LogIn', payload=usuarioincorrecto,expected_status_code=401)
        logger.debug(api_res)
        return api_res

    def get_code401WrongToken(self):
        self.requestUtility.accessToken = 'dlrbESTOESUNTOKENINCORRECTOYxOajUPUeFc/jObmjNNiuAjOA2WFiwqJog9Ulc/T6Ql3NmDohuVi+G1fSaP/hzgX380xf6sLBSNqE0C30mkBMCeytFjqR/NxAQKbo+IkhuW1tR/f91XgO3PMwG+/t1xpkJoAVxzKXF8GnJDtWky1uS+tDGF6w1N8JLITUV4VOO24Z1DKRYNNQJ/nBkujjRuYZ3EjSJREM0XBXgPE='
        api_res = self.requestUtility.get("/DataSource/List", expected_status_code=500)
        # with open('DSList_new.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_RawDataID(self, RevID=1,Titulo='',expRes=200,empRes=False):
        api_res = self.requestUtility.get("/Configuration/RawData?ConfigurationRunId="+str(RevID),expected_status_code=expRes,resEmpty=empRes)
        with open('RawDataID'+Titulo+'.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_RawDataLastNRows(self, RevID=1,Rows='1',Titulo='',expRes=200,empRes=False):
        api_res = self.requestUtility.get("/Configuration/RawData?ConfigurationRunId="+str(RevID)+'&LastN='+str(Rows),expected_status_code=expRes,resEmpty=empRes)
        with open('RawDataIDLastNRows'+Titulo+'.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res
    
    def get_RDIDOffset(self,Titulo='', RevID=1,Off=1,Rows=1,expRes=200,empRes=False):
        api_res = self.requestUtility.get("/Configuration/RawData?ConfigurationRunId="+str(RevID)+"&Offset="+str(Off)+"&Rows="+str(Rows),expected_status_code=expRes,resEmpty=empRes)
        with open('RawDataIDOffsetandRows'+Titulo+'.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        #logger.debug(api_res)
        return api_res
    
    def get_RDRecent(self,Titulo='', RevID=1,Time=5,expRes=200,empRes=False):
        api_res = self.requestUtility.get("/Configuration/RawData?ConfigurationRunId="+str(RevID)+"&Recent="+str(Time),expected_status_code=expRes,resEmpty=empRes)
        with open('RawDataRecentTime'+Titulo+'.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_RDStartStopTime(self,Titulo='', RevID=1,Start="",Stop="",expRes=200,empRes=False):
        api_res = self.requestUtility.get("/Configuration/RawData?ConfigurationRunId="+str(RevID)+"&TimeStart="+str(Start)+"&TimeEnd=",expected_status_code=expRes,resEmpty=empRes)
        with open('RawDataStartStopTime'+Titulo+'.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_RDStartTime(self,Titulo='', RevID=1,Start="", expRes=200,empRes=False):
        api_res = self.requestUtility.get("/Configuration/RawData?ConfigurationRunId="+str(RevID)+"&TimeStart="+str(Start),expected_status_code=expRes,resEmpty=empRes)
        with open('RawDataStartTime'+Titulo+'.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    
    def get_RModelMetaMRID(self,RevID=1,expRes=200,empRes=False):
        api_res = self.requestUtility.get("/model/metadata?modelRevisionId="+str(RevID),expected_status_code=expRes,resEmpty = empRes)
        with open('ModelMetaID.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res
    
    def get_RDSMetaDSId(self, RevID=1,expRes=200,empRes=False):
        api_res = self.requestUtility.get("/datasource/metadata?datasourceRevisionId="+str(RevID),expected_status_code=expRes,resEmpty = empRes)
        with open('RDSMbyDSid.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_RConfMetaConfId(self,RevID=1,expRes=200,empRes=False):
        api_res = self.requestUtility.get("/Configuration/Metadata?configurationRevisionId="+str(RevID),expected_status_code=expRes,resEmpty=empRes)
        with open('RConfMetaConfId.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res
    
    def get_RetMetaInfoConfRuns(self,RevID=1,expRes=200,empRes=False):
        api_res = self.requestUtility.get("/Configuration/GetConfigurationRunMetadataByRunID?runID="+str(RevID),expected_status_code=expRes,resEmpty=empRes)
        with open('MetaInfoConfigRun.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_ConfigTags(self, Titulo='Tags',LabelName='',expRes=200,empRes=False):
        api_res = self.requestUtility.get("/configuration/GetTagInformation?label="+LabelName,expected_status_code=expRes,resEmpty=empRes)
        with open('ConfigTagsRetrieve'+Titulo+'.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_RetConfRunbyMetaTag(self, Titulo='Tags',TagName='',TagValue='',expRes=200,empRes=False):
        api_res = self.requestUtility.get("/Configuration/GetConfigurationRunsByTags?TagKey="+TagName+"&TagValue="+TagValue,expected_status_code=expRes,resEmpty=empRes)
        with open('ConfigRunbyMetaData'+Titulo+'.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_RRMNFull(self):
        api_res = self.requestUtility.get("/Configuration/ResultMatrices?configurationId=3?MatrixName=Scores")
        # with open('ResMatFull.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_RRMConfRun(self):
        api_res = self.requestUtility.get("/Configuration/ResultTypes?configurationRunId=10")
        with open('ResMatConfRun.json', 'w') as f:
            json.dump(api_res, f, indent=2)
            logger.debug('File Created')
        logger.debug(api_res)
        return api_res

    def get_RRMatricesNameFullList(self):
        api_res = self.requestUtility.get("/Configuration/ResultMatrices?configurationId=1?MatrixName=Scores", expected_status_code = 200, resEmpty = True)
        # with open('RConfMetaConfId.json', 'w') as f:
        #     json.dump(api_res, f, indent=2)
        #     logger.debug('File Created')
        #logger.debug(api_res)
        return api_res
