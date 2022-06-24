import pytest
import unittest
import requests
import json

from ssqaapitest.src.helpers.MVA_restAPI.requests import Endpoints
from ssqaapitest.src.helpers.TSD_ConsumerService.dbConnection import dbConnection
from ssqaapitest.src.utilities.jsonUtility import JsonUtility
import logging as logger





@pytest.mark.mva_ProcessPulseV14
class TestListElements(unittest.TestCase):

    #/TSDRetrieval/QueryTsd
    @pytest.mark.vsts787805
    def test_MVADS(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_DSList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('DSList_new.json')
        self.assertEqual(res, resExp)

    @pytest.mark.vsts787809
    def test_MVAMod(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_ModelList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelList_new.json')
        self.assertEqual(res, resExp)

    @pytest.mark.vsts787828
    def test_MVAConfig(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_ConfigurationList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ConfigurationList_new.json')
        self.assertEqual(res, resExp)

        
        