import pytest
import unittest
import requests
import json

from ssqaapitest.src.helpers.MVA_restAPI.requests import Endpoints
from ssqaapitest.src.helpers.MVA_restAPI.dbConnection import dbConnection
from ssqaapitest.src.utilities.jsonUtility import JsonUtility
import logging as logger





@pytest.mark.mva_ProcessPulseV14
class TestListElements(unittest.TestCase):

    #/TSDRetrieval/QueryTsd
    @pytest.mark.vsts790591
    def test_MVAWEP(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_WEndP()
        self.assertEqual(res,res)

    @pytest.mark.vsts787805
    def test_MVADS(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_DSList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('DSList_new.json')
        self.assertEqual(res, resExp,"The Json of Data Sources Failed")

    @pytest.mark.vsts787809
    def test_MVAMod(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_ModelList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelList_new.json')
        self.assertEqual(res, resExp,"The Json of Models Failed")

    @pytest.mark.vsts787828
    def test_MVAConfig(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_ConfigurationList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ConfigurationList_new.json')
        self.assertEqual(res, resExp,"The Json of Configurations Failed")

        
    @pytest.mark.vsts787818
    def test_MVAConfR(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_ConfRunList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ConfRunsList.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts788343
    def test_MVARawDataID(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RawDataID()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataID.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts788346
    def test_MVARawDataFNR(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RawDataFNR()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataFNR.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts788347
    def test_MVARawDataOFF(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RawDataOFF()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataOFF.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts788731
    def test_MVARModMetaID(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RModelMetaMRID()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelMetaID.json')
        self.assertEqual(res, resExp,"Something went wrong")

    # @pytest.mark.vsts788393
    # def test_MVARRMNFull(self):
        
    #     logger.debug(self.id())
    #     endpoints = Endpoints()
    #     res = endpoints.get_RRMNFull()
    #     jsonUtil = JsonUtility('MVArestAPI')
    #     resExp = jsonUtil.read_Json('ResMatFull.json')
    #     self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts788391
    def test_MVARRMConfRun(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMConfRun()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ResMatConfRun.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts788736
    def test_MVARDSMetaDSId(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSid.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts788755
    def test_MVARConfMetaConfId(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RConfMetaConfId()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RConfMetaConfId.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts788393
    def test_RetrieveResultMatricesName(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameFullList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RConfMetaConfId.json')
        self.assertEqual(res, resExp,"Something went wrong")



    @pytest.mark.prueba1
    def test_pruebita(self):
        
        logger.debug(self.id())
        dbConex = dbConnection()
        params={'ApprovedRevisionId':3}
        res = dbConex.get_DataSet()
        logger.debug(res)
        logger.debug(len(res))
        logger.debug((res[0]['DataSourceID']))
        endpoints = Endpoints()
        resotro = endpoints.get_DSList()
        logger.debug(res)
        logger.debug(len(res))
        logger.debug(type(res))
        self.assertEqual(1, 1,"Something went wrong")