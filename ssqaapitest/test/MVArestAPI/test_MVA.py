import pytest
import unittest
import requests
import json

from ssqaapitest.src.helpers.MVA_restAPI.requests import Endpoints
from ssqaapitest.src.helpers.MVA_restAPI.dbConnection import dbConnection
from datetime import datetime
from ssqaapitest.src.utilities.jsonUtility import JsonUtility
import logging as logger
import random





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

        #Get information from DataBase and RestAPI
        dbConex = dbConnection()
        resDB = dbConex.get_DataSet(table = 'DataSourceRevision')
        resDB2 = dbConex.get_DataSet(table = 'DataSource')
        endpoints = Endpoints()
        resAPI = endpoints.get_DSList()

        #Check both have the same number of Data Sources
        self.assertEqual(len(resDB),len(resAPI))
        
        #Check structure information in the RestAPI response 
        info=list(resAPI[0].keys())
        structure= ['Id', 'RevisionId', 'RevisionNumber', 'Name', 'Type', 'Created', 'IsEnabled', 'IsApproved']
        self.assertEqual(info, structure,"Something went wrong")

        #Check information of a random datasource
        aleat= random.randint(1, 11)
        logger.debug(aleat)
        #DataSourceID
        """ 
        logger.debug((resDB[aleat-1]['DataSourceID']))
        logger.debug(resAPI[-aleat]['Id']) """
        self.assertEqual((resDB[aleat-1]['DataSourceID']),(resAPI[-aleat]['Id']))
        #RevisionID
        """ logger.debug((resDB[aleat-1]['RevisionID']))
        logger.debug(resAPI[-aleat]['RevisionId']) """
        self.assertEqual((resDB[aleat-1]['RevisionID']),(resAPI[-aleat]['RevisionId']))
        #Name
        """ logger.debug((resDB[aleat-1]['Name']))
        logger.debug(resAPI[-aleat]['Name']) """
        self.assertEqual((resDB[aleat-1]['Name']),(resAPI[-aleat]['Name']))
        #Created
        """ logger.debug(str(resDB[aleat-1]['CreatedDate'])[0:22])
        logger.debug(resAPI[-aleat]['Created'][0:10]+' '+resAPI[-aleat]['Created'][11:22]) """
        self.assertEqual(str(resDB[aleat-1]['CreatedDate'])[0:22],(resAPI[-aleat]['Created'][0:10]+' '+resAPI[-aleat]['Created'][11:22]))
        #IsEnabled
        """ logger.debug(bool(resDB2[aleat-1]['Disabled']))
        logger.debug(resAPI[-aleat]['IsEnabled']) """
        self.assertFalse(bool(resDB2[aleat-1]['Disabled']),resAPI[-aleat]['IsEnabled'])

    @pytest.mark.vsts787809
    def test_MVAMod(self):
        
        logger.debug(self.id())

        #Get information from DataBase and RestAPI
        dbConex = dbConnection()
        resDB = dbConex.get_DataSet(table = 'ModelRevision')
        resDB2 = dbConex.get_DataSet(table = 'Model')
        endpoints = Endpoints()
        resAPI = endpoints.get_ModelList()

        #Check both have the same number of Data Sources
        self.assertEqual(len(resDB),len(resAPI))
        
        #Check structure information in the RestAPI response 
        info=list(resAPI[0].keys())
        #logger.debug(info)
        structure= ['ModelId', 'RevisionID', 'Name', 'Revision', 'ModelSoftware', 'ModelType', 'UploadedBy', 'UploadedDate', 'IsApproved', 'IsEnabled']
        self.assertEqual(info, structure,"Something went wrong")

        #Check information of a random Model
        aleat= random.randint(1, 11)
        logger.debug(aleat)
        #ModelID
        """ 
        logger.debug((resDB[aleat-1]['DataSourceID']))
        logger.debug(resAPI[-aleat]['Id']) """
        self.assertEqual((resDB[aleat-1]['ModelID']),(resAPI[aleat-1]['ModelId']))
        #RevisionID
        """ logger.debug((resDB[aleat-1]['RevisionID']))
        logger.debug(resAPI[-aleat]['RevisionId']) """
        self.assertEqual((resDB[aleat-1]['RevisionID']),(resAPI[aleat-1]['RevisionID']),'Revision')
        #Name
        """ logger.debug((resDB2[aleat-1]['Name']))
        logger.debug(resAPI[aleat-1]['Name']) """
        self.assertEqual((resDB2[aleat-1]['Name']),(resAPI[aleat-1]['Name']))
        #Created
        """ logger.debug(str(resDB[aleat-1]['UploadDate'])[0:22])
        logger.debug(resAPI[-aleat]['UploadedDate'][0:10]+' '+resAPI[aleat-1]['UploadedDate'][11:22]) """
        self.assertEqual(str(resDB[aleat-1]['UploadDate'])[0:22],(resAPI[aleat-1]['UploadedDate'][0:10]+' '+resAPI[aleat-1]['UploadedDate'][11:22]))
        #IsEnabled
        """ logger.debug(bool(resDB2[aleat-1]['Disabled']))
        logger.debug(resAPI[-aleat]['IsEnabled']) """
        self.assertFalse(bool(resDB2[aleat-1]['Disabled']),resAPI[aleat-1]['IsEnabled'])
        #IsEnabled
        """ logger.debug((resDB[aleat-1]['UploadedBy']))
        logger.debug(resAPI[aleat-1]['UploadedBy']) """
        self.assertEqual((resDB[aleat-1]['UploadedBy']),resAPI[aleat-1]['UploadedBy'])
        
        

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

    @pytest.mark.vsts788393
    def test_MVARRMNFull(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMNFull()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ResMatFull.json')
        self.assertEqual(res, resExp,"Something went wrong")

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

        #Get information from DataBase and RestAPI
        dbConex = dbConnection()
        resDB = dbConex.get_DataSet(table = 'ModelRevision')
        resDB2 = dbConex.get_DataSet(table = 'Model')
        endpoints = Endpoints()
        resAPI = endpoints.get_ModelList()

        #Check both have the same number of Data Sources
        self.assertEqual(len(resDB),len(resAPI))
        
        #Check structure information in the RestAPI response 
        info=list(resAPI[0].keys())
        logger.debug(info)
        structure= ['ModelId', 'RevisionID', 'Name', 'Revision', 'ModelSoftware', 'ModelType', 'UploadedBy', 'UploadedDate', 'IsApproved', 'IsEnabled']
        self.assertEqual(info, structure,"Something went wrong")

        #Check information of a random Model
        aleat= random.randint(1, 11)
        logger.debug(aleat)
        #ModelID
        """ 
        logger.debug((resDB[aleat-1]['DataSourceID']))
        logger.debug(resAPI[-aleat]['Id']) """
        self.assertEqual((resDB[aleat-1]['ModelID']),(resAPI[aleat-1]['ModelId']))
        #RevisionID
        """ logger.debug((resDB[aleat-1]['RevisionID']))
        logger.debug(resAPI[-aleat]['RevisionId']) """
        self.assertEqual((resDB[aleat-1]['RevisionID']),(resAPI[aleat-1]['RevisionID']),'Revision')
        #Name
        """ logger.debug((resDB2[aleat-1]['Name']))
        logger.debug(resAPI[aleat-1]['Name']) """
        self.assertEqual((resDB2[aleat-1]['Name']),(resAPI[aleat-1]['Name']))
        #Created
        """ logger.debug(str(resDB[aleat-1]['UploadDate'])[0:22])
        logger.debug(resAPI[-aleat]['UploadedDate'][0:10]+' '+resAPI[aleat-1]['UploadedDate'][11:22]) """
        self.assertEqual(str(resDB[aleat-1]['UploadDate'])[0:22],(resAPI[aleat-1]['UploadedDate'][0:10]+' '+resAPI[aleat-1]['UploadedDate'][11:22]))
        #IsEnabled
        """ logger.debug(bool(resDB2[aleat-1]['Disabled']))
        logger.debug(resAPI[-aleat]['IsEnabled']) """
        self.assertFalse(bool(resDB2[aleat-1]['Disabled']),resAPI[aleat-1]['IsEnabled'])
        #IsEnabled
        logger.debug((resDB[aleat-1]['UploadedBy']))
        logger.debug(resAPI[aleat-1]['UploadedBy'])
        self.assertEqual((resDB[aleat-1]['UploadedBy']),resAPI[aleat-1]['UploadedBy'])
        
        
        
        
