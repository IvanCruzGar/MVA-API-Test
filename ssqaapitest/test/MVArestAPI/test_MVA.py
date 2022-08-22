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

   

    @pytest.mark.vsts787805
    def test_RetrieveListOfDataSources(self):
        
        logger.debug(self.id())

        #Get information from DataBase and RestAPI
        dbConex = dbConnection()
        resDB = dbConex.get_DataSet(table = 'DataSourceRevision')
        resDB2 = dbConex.get_DataSet(table = 'DataSource')
        endpoints = Endpoints()
        resAPI = endpoints.get_DSList()

        #Check both have the same number of Data Sources
        self.assertEqual(len(resDB),len(resAPI),'Diferent number of Data Sources')
        
        #Check structure information in the RestAPI response 
        info=list(resAPI[0].keys())
        structure= ['Id', 'RevisionId', 'RevisionNumber', 'Name', 'Type', 'Created', 'IsEnabled', 'IsApproved']
        self.assertEqual(info, structure,"Structure of response is wrong")

        #Check information of a random datasource
        aleat= random.randint(1, len(resDB))
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
        logger.debug(str(resDB[aleat-1]['CreatedDate'])[0:22])
        logger.debug(resAPI[-aleat]['Created'])
        self.assertEqual(str(resDB[aleat-1]['CreatedDate'])[0:22],(resAPI[-aleat]['Created'][0:10]+' '+resAPI[-aleat]['Created'][11:22]))
        #IsEnabled
        """ logger.debug(bool(resDB2[aleat-1]['Disabled']))
        logger.debug(resAPI[-aleat]['IsEnabled']) """
        self.assertFalse(bool(resDB2[aleat-1]['Disabled']),resAPI[-aleat]['IsEnabled'])

    @pytest.mark.vsts787828
    def test_RetrieveListOfModels(self):
        
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
        self.assertEqual(info, structure,"Structure is wrong")

        #Check information of a random Model
        aleat= random.randint(1, len(resDB))
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
        
    @pytest.mark.vsts787809
    def test_RetrieveListOfConfigurations(self):
        logger.debug(self.id())

        #Get information from DataBase and RestAPI
        dbConex = dbConnection()
        resDB = dbConex.get_DataSet(table = 'ConfigurationRevision')
        resDB2 = dbConex.get_DataSet(table = 'Configurations')
        endpoints = Endpoints()
        resAPI = endpoints.get_ConfigurationList()

        #Check both have the same number of Configurations
        self.assertEqual(len(resDB),len(resAPI))
        
        #Check structure information in the RestAPI response 
        info=list(resAPI[0].keys())
        #logger.debug(info)
        structure= ['ConfigId', 'ConfigName', 'RevisionNumber', 'MethodName', 'CreatedDate', 'Status', 'IsEnabled', 'IsApproved']
        self.assertEqual(info, structure,"Something went wrong")

        #Check information of a random Configuration
        aleat= random.randint(1, len(resDB))
        logger.debug(aleat)
        #ConfigID
        
        """ logger.debug((resDB[aleat-1]['ConfigurationID']))
        logger.debug(resAPI[aleat-1]['ConfigId']) """
        self.assertEqual((resDB[aleat-1]['ConfigurationID']),(resAPI[aleat-1]['ConfigId']))
        #RevisionID
        """ logger.debug((resDB[aleat-1]['RevisionNumber']))
        logger.debug(resAPI[aleat-1]['RevisionNumber']) """
        self.assertEqual((resDB[aleat-1]['RevisionNumber']),(resAPI[aleat-1]['RevisionNumber']),'Revision')
        #Name
        """ logger.debug((resDB2[aleat-1]['name']))
        logger.debug(resAPI[aleat-1]['ConfigName']) """
        self.assertEqual((resDB2[aleat-1]['name']),(resAPI[aleat-1]['ConfigName']))
        #Created
        """ logger.debug(str(resDB[aleat-1]['CreatedDate'])[0:22])
        logger.debug(resAPI[-aleat]['CreatedDate'][0:10]+' '+resAPI[aleat-1]['CreatedDate'][11:22]) """
        self.assertEqual(str(resDB[aleat-1]['CreatedDate'])[0:22],(resAPI[aleat-1]['CreatedDate'][0:10]+' '+resAPI[aleat-1]['CreatedDate'][11:22]))
        #IsEnabled
        """ logger.debug(bool(resDB2[aleat-1]['disabled']))
        logger.debug(resAPI[aleat-1]['IsEnabled']) """
        self.assertFalse(bool(resDB2[aleat-1]['disabled']),resAPI[aleat-1]['IsEnabled'])
        logger.debug((resDB[aleat-1]['MethodInfo']))

    @pytest.mark.vsts787818
    def test_RetrieveListOfConfigurationRuns(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_ConfRunList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ConfRunsList.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts790591
    def test_ReturnCode404(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_code404()
        self.assertEqual(res,res)
    
    @pytest.mark.vsts791785
    def test_ReturnCode401WrongUser(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_code401WrongUser()
        self.assertEqual(res,res)

    @pytest.mark.vsts791965
    def test_ReturnCode401WrongPassword(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_code401WrongPassword()
        self.assertEqual(res,res)

    @pytest.mark.vsts791982
    def test_ReturnCode401WrongAccessToken(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_code401WrongToken()
        self.assertEqual(res,res)
        
    

    @pytest.mark.vsts788343
    def test_RetrieveRawData_ConfigurationRunID(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RawDataID(RevID=1)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataID.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts788347
    def test_RetrieveRawData_OffsetandRows(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDIDOffset(RevID=1,Off=4,Rows=2)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataIDOffset.json')
        self.assertEqual(res, resExp,"Something went wrong")




    @pytest.mark.vsts788346
    def test_MVARawDataFNR(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RawDataFNR()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataFNR.json')
        self.assertEqual(res, resExp,"Something went wrong")


    @pytest.mark.vsts792456
    def test_RetrieveModelMetadatabyModelRevisionID_Batch(self):

        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RModelMetaMRID(RevID=14)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelMetaIDBatch.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792459
    def test_RetrieveModelMetadatabyModelRevisionID_InvalidModelRevisionID(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RModelMetaMRID(RevID=0,expRes=400,empRes=True)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelMetaID.json')
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts788731
    def test_RetrieveModelMetadatabyModelRevisionID_PCA(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RModelMetaMRID(RevID=1)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelMetaIDPCA.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792451
    def test_RetrieveModelMetadatabyModelRevisionID_PCR(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RModelMetaMRID(RevID=9)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelMetaIDPCR.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792452
    def test_RetrieveModelMetadatabyModelRevisionID_MCR(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RModelMetaMRID(RevID=4)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelMetaIDMCR.json')
        self.assertEqual(res, resExp,"Something went wrong")
    
    @pytest.mark.vsts792453
    def test_RetrieveModelMetadatabyModelRevisionID_MLR(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RModelMetaMRID(RevID=5)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelMetaIDMLR.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792454
    def test_RetrieveModelMetadatabyModelRevisionID_SIMCA(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RModelMetaMRID(RevID=11)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelMetaIDSIMCA.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792455
    def test_RetrieveModelMetadatabyModelRevisionID_SVR(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RModelMetaMRID(RevID=12)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelMetaIDSVR.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792460
    def test_RetrieveModelMetadatabyModelRevisionID_NonexistingModelRevisionID(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RModelMetaMRID(RevID=200,expRes=204,empRes=True)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ModelMetaID.json')
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts788736
    def test_RetrieveDataSourceMetadatabyDataSourceRevisionID_ASCII(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId(RevID=1)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSidASCII.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792440
    def test_RetrieveDataSourceMetadatabyDataSourceRevisionID_GRAMS(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId(RevID=2)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSidGRAMS.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792441
    def test_RetrieveDataSourceMetadatabyDataSourceRevisionID_JCAMPDX(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId(RevID=3)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSidJCAMP.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792442
    def test_RetrieveDataSourceMetadatabyDataSourceRevisionID_OPUS(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId(RevID=4)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSidOPUS.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792443
    def test_RetrieveDataSourceMetadatabyDataSourceRevisionID_ZEISS(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId(RevID=5)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSidZEISS.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792444
    def test_RetrieveDataSourceMetadatabyDataSourceRevisionID_Image(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId(RevID=6)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSidImage.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792445
    def test_RetrieveDataSourceMetadatabyDataSourceRevisionID_Empower(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId(RevID=7)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSidEmpower.json')
        self.assertEqual(res, resExp,"Something went wrong")  

    @pytest.mark.vsts792446
    def test_RetrieveDataSourceMetadatabyDataSourceRevisionID_PI(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId(RevID=8)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSidPI.json')
        self.assertEqual(res, resExp,"Something went wrong")    

    @pytest.mark.vsts792447
    def test_RetrieveDataSourceMetadatabyDataSourceRevisionID_Eigen(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId(RevID=9)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSidEigen.json')
        self.assertEqual(res, resExp,"Something went wrong")  

    @pytest.mark.vsts792448
    def test_RetrieveDataSourceMetadatabyDataSourceRevisionID_Batch(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId(RevID=10)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSidBatch.json')
        self.assertEqual(res, resExp,"Something went wrong")   

    @pytest.mark.vsts792449
    def test_RetrieveDataSourceMetadatabyDataSourceRevisionID_InvalidDataSourceID(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId(RevID=0,expRes=400,empRes=True)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSidBatch.json')
        self.assertEqual(res, resExp,"Something went wrong") 

    @pytest.mark.vsts792450
    def test_RetrieveDataSourceMetadatabyDataSourceRevisionID_NonexistingDataSource(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDSMetaDSId(RevID=200,expRes=204,empRes=True)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RDSMbyDSidBatch.json')
        self.assertEqual(res, resExp,"Something went wrong") 

    @pytest.mark.vsts788755
    def test_RetrieveConfigurationMetadatabyRevisionID(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        #Get API response and information from DataBase
        ConfID=1
        resAPI = endpoints.get_RConfMetaConfId(RevID=ConfID)
        dbConex = dbConnection()
        resDB = dbConex.get_DataSet(table = 'ConfigurationRevision')
        resDB2 = dbConex.get_DataSet(table = 'Configurations')

        #Check API response structure
        info=list(resAPI[0].keys())
        logger.debug(info)
        structure= ['Configuration ID', 'Configuration Name', 'Revision Number', 'Method Name', 'Model Name', 'Transformations', 'Online Calculations', 'Output', 'Notifications']
        #self.assertEqual(info, structure,"Structure is different")

        #Check Configuration ID
        logger.debug(resDB[ConfID-1]['ConfigurationID'])
        logger.debug(resAPI[0]['Configuration ID'])
        self.assertEqual((resDB[ConfID-1]['ConfigurationID']),(resAPI[0]['Configuration ID']),"Configuration ID was different")
        #Check Revision ID
        logger.debug(resDB[ConfID-1]['RevisionID'])
        logger.debug(resAPI[0]['Revision Number'])
        self.assertEqual((resDB[ConfID-1]['RevisionID']),(resAPI[0]['Revision Number']),"Revision was different")
        #Check COnfiguration Name
        logger.debug(resDB2[ConfID-1]['name'])
        logger.debug(resAPI[0]['Configuration Name'])
        self.assertEqual((resDB2[ConfID-1]['name']),(resAPI[0]['Configuration Name']),"Name was different")
        







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
        
        
        
        
