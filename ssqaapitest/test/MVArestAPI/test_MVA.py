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
    @pytest.mark.DataSourceList
    def test_MVADS(self):
        
        logger.debug(self.id())
        logger.debug("Hola mundo")
        endpoints = Endpoints()
        res = endpoints.get_DSList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('DSList_otro.json')
        self.assertEqual(res, resExp)

    @pytest.mark.ModelList
    def test_MVAMod(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_ModelList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelList_otro.json')
        self.assertEqual(res, resExp)

    @pytest.mark.ConfigList
    def test_MVAConfig(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_ConfigurationList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ConfigurationList_otro.json')
        self.assertEqual(res, resExp)

        
        