import pytest
import unittest

from ssqaapitest.src.helpers.TSD_DataAcquisitionService.request import Endpoints
from ssqaapitest.src.helpers.TSD_DataAcquisitionService.dbConnection import dbConnection
from ssqaapitest.src.utilities.jsonUtility import JsonUtility
import logging as logger

#2 s pass, 4 fail, 2 progress
#http://172.22.4.151:8080/Aspentech/APM/TSDDataAcquisitionService/swagger/index.html
#Needs Autorization
@pytest.mark.tsd_DataAcquisitionService
class TestListElements(unittest.TestCase):

    #Add Comparison with the DB
    #Check results response 200
    #/CycleBuilder
    @pytest.mark.vsts633167
    def test_CycleBuilder_Get(self):
        logger.debug(self.id())
        dbUtil = dbConnection()
        dbData = dbUtil.get_CycleObject()
        status = 415 if (len(dbData) == 0) else 200
        endpoints = Endpoints()
        res = endpoints.get_CycleBuilder(status)
        logger.debug(res)
        #jsonUtil = JsonUtility('TSD_DataAcquisitionService')
        #resExp = []
        #self.assertEqual(res, resExp, f"{self.id()}  #/CycleBuilder, Response different Json")
        
        
    #/CycleBuilder
    @pytest.mark.vsts633169
    def test_CycleBuilder_Post(self):
        logger.debug(self.id())
        self.skipTest("In progress, create a new register, check how to implement this")
        endpoints = Endpoints()
        #res = endpoints.post_CycleBuilder()
        

    #/CycleBuilder Put
    #@pytest.mark.vsts633170

    #Add Comparison with the DB
    #/CycleBuilder/after/{startDate}
    @pytest.mark.vsts633171
    def test_CycleBuilderAfter(self):
        logger.debug(self.id())
        self.skipTest("In progrss, Needed comparison with the DB")
        endpoints = Endpoints()
        #res = endpoints.get_CycleBuilderAfter()
        #jsonUtil = JsonUtility('TSD_DataAcquisitionService')
        
        #self.assertEqual(res, resExp, f"{self.id()}  #/CycleBuilder, Response different Json")

    #Add Comparison with the DB
    #/CycleBuilder/{Object id}
    @pytest.mark.vsts633174
    def test_CycleBuilder_Object(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_CycleBuilder_Object()
        #jsonUtil = JsonUtility('TSD_DataAcquisitionService')
        self.skipTest("In progress, Needed comparison with the DB")
        #self.assertEqual(res, resExp, f"{self.id()}  #/CycleBuilder/Objectid, Response different Json")

    #/GranularityTypes
    @pytest.mark.vsts633177
    def test_GranularityTypes(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_GranularityTypes()
        jsonUtil = JsonUtility('TSD_DataAcquisitionService')
        resExp = jsonUtil.read_Json('GranularityTypes_res_get.json')
        self.assertEqual(res, resExp, f"{self.id()}  #/GranularityTypes, Response different Json")

    #/GranularityTypes/{Object id}
    @pytest.mark.vsts633178
    def test_GranularityTypes_Object(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_GranularityTypes_Object()
        jsonUtil = JsonUtility('TSD_DataAcquisitionService')
        resExp = jsonUtil.read_Json('GranularityTypes_Object10_res_get.json')
        self.assertEqual(res, resExp, f"{self.id()}  #/GranularityTypes/Objectid, Response different Json")

    #Add Db Comparison
    #/Submissions/{requestType}/{startDate}/{endDate}
    @pytest.mark.vsts633182
    def test_Submision_Object(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_Submision_Object()
        #jsonUtil = JsonUtility('TSD_DataAcquisitionService')
        #resExp = jsonUtil.read_Json('GranularityTypes_Object10_res_get.json')
        #self.assertEqual(res, resExp, f"{self.id()}  #/GranularityTypes/Objectid, Response different Json")
        self.skipTest("In progress, Needed comparison with the DB")

    #Add Comparison with the DB
    #/Submissions 
    @pytest.mark.vsts633183
    def test_Submissions (self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_Submision()
        #jsonUtil = JsonUtility('TSD_DataAcquisitionService')
        resExp = []
        #self.assertEqual(res, resExp, f"{self.id()}  #/CycleBuilder, Response different Json")
        self.skipTest("In progress, Needed comparison with the DB")

    #Add Db Comparison
    #/Submissions/date/{startDate}/{endDate}
    @pytest.mark.vsts633184
    def get_SubmisionDate_Object(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_SubmisionDate_Object()
        #jsonUtil = JsonUtility('TSD_DataAcquisitionService')
        #resExp = jsonUtil.read_Json('GranularityTypes_Object10_res_get.json')
        #self.assertEqual(res, resExp, f"{self.id()}  #/GranularityTypes/Objectid, Response different Json")
        self.skipTest("In progress, Needed comparison with the DB")

    
    