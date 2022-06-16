import pytest
import unittest

from ssqaapitest.src.helpers.TSD_ConsumerService.request import Endpoints
from ssqaapitest.src.helpers.TSD_ConsumerService.dbConnection import dbConnection
from ssqaapitest.src.utilities.jsonUtility import JsonUtility
import logging as logger

#7 passs, 1 fail, 1 progress
@pytest.mark.tsd_ConsumerService
class TestListElements(unittest.TestCase):

    #/TSDRetrieval/QueryTsd
    @pytest.mark.vsts632117
    def test_QueryTsd(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.post_QueryTsd()
        jsonUtil = JsonUtility('TSD_ConsumerService')
        resExp = jsonUtil.read_Json('QueryTsd_res_post.json')
        self.assertEqual(res, resExp, f"{self.id()}  #/TSDRetrieval/GetTsd, Response different Json")

    #/TSDRetrieval/GetTsd
    @pytest.mark.vsts632118  
    def test_GetTsd(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.post_GetTsd()
        jsonUtil = JsonUtility('TSD_ConsumerService')
        resExp = jsonUtil.read_Json('GetTds_res_post.json')
        self.assertEqual(res, resExp, f"{self.id()}  #/TSDRetrieval/GetTsd, Response different Json")

    #/TSDRetrieval/GetAvailableGranularitiesForTag
    @pytest.mark.vsts633099
    def test_GetAvailableGranularitiesForTag(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.post_GetAvailableGranularitiesForTag()
        jsonUtil = JsonUtility('TSD_ConsumerService')
        resExp = jsonUtil.read_Json('GetAvailableGranularitiesForTag_res_post.json')
        self.assertEqual(res, resExp, f"{self.id()}  #/TSDRetrieval/GetTsd, Response different Json")

    #/TSDRetrieval/GetGranularityListing
    @pytest.mark.vsts633108 
    def test_GetGranularityListing(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_GetGranularityListing()
        jsonUtil = JsonUtility('TSD_ConsumerService')
        resExp = jsonUtil.read_Json('GetGranularityListing_res_get.json')
        self.assertEqual(res, resExp, f"{self.id()}  #/TSDRetrieval/GetTsd, Response different Json")

    #/Custom/GetTrainingDataSet
    @pytest.mark.vsts633112
    def test_GetTrainingDataSet_Post(self):
        logger.debug(self.id())
        self.skipTest("In progress, looks made to test vsts632118")
        endpoints = Endpoints()
        self.assertEqual(1,1)

    #/TSDRetrieval/GetRangeOfExistingData
    @pytest.mark.vsts633135
    def test_GetRangeOfExistingData(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.post_GetRangeOfExistingData()
        jsonUtil = JsonUtility('TSD_ConsumerService')
        resExp = jsonUtil.read_Json('GetRangeOfExistingData_res_post.json')
        self.assertEqual(res, resExp, f"{self.id()}  #/TSDRetrieval/GetRangeOfExistingData, Response different Json")

    #Add comparison with the DB
    #Error parameter typo
    #/PDR/GetDataSet
    @pytest.mark.vsts633140
    def test_GetDataSet(self):
        logger.debug(self.id())
        reqParams = {'AppId' : 1,
            'ComponentTypeId' : 1,
            'CompnentId' : 144,
            'TypeId' : 1}
        dbParams = {'AppId' : reqParams['AppId'],
            'ComponentTypeId' : reqParams['ComponentTypeId'],
            'ComponentId' : reqParams['CompnentId'],
            'FK_TypeId' : reqParams['TypeId']
        }
        dbUtil = dbConnection()
        dbData = dbUtil.get_DataSet(dbParams)
        endpoints = Endpoints()
        status = 204 if (len(dbData) == 0) else 200
        res = endpoints.get_GetDataSet(reqParams, status)
        if status == 200:
            self.assertEqual(res['setId'], dbData[0]['SetId'], f"{self.id()}  #/PDR/GetDataSet, Response Dataset Id is different")
        #Doesnt Match with the TC

    #Add comparison with the DB
    #/PDR/GetDataSetById
    @pytest.mark.vsts633142
    def test_GetDataSetById(self):
        logger.debug(self.id())
        reqParams = {'SetId' : 2}
        endpoints = Endpoints()
        res = endpoints.get_GetDataSetById(reqParams)
        jsonUtil = JsonUtility('TSD_ConsumerService')
        resExp = jsonUtil.read_Json('GetDataSetById_res_get.json')
        dbUtil = dbConnection()
        dbData = dbUtil.get_DataSet(reqParams)
        self.assertEqual(res['setId'], dbData[0]['SetId'], f"{self.id()}  #/PDR/GetDataSet, Response Dataset Id is different")
        
    #/PDR/SaveDataSet
    @pytest.mark.vsts6633152
    def test_GetDataSetByIdTest(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        self.skipTest("In progress, This Saves a New Data set, is needed to check if we can run this TC twice, or we need to delete the register")
        
    
    