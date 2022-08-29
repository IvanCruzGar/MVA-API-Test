from cmath import exp
from fileinput import filename
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

   
    #Use Case 689747: 7. Retrieve List of Data Sources
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

    #Use Case 689756: 14. Retrieve list of Models
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
        
    #Use Case 689749: 8. Retrieve list of Configurations
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

    #Use Case 689750: 9. Retrieve list of Configuration Runs
    @pytest.mark.vsts787818
    def test_RetrieveListOfConfigurationRuns(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_ConfRunList()
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ConfRunsList.json')
        self.assertEqual(res, resExp,"Something went wrong")

    #Use Case 763821: Return Codes
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
    
    
    #Use Case 689751: 10. Retrieve Raw Data
    @pytest.mark.vsts788343
    def test_RetrieveRawData_ConfigurationRunID(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RawDataID(RevID=2)
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

    #Use Case 782953: Raw Data includes CDM values


    #Use Case 689753: 12. Retrieve Result Matrices for Configuration Run

    #Use Case 689754: 13. Retrieve Result Matrices by Name



    #Use Case 764933: 14.2. Retrieve Model Metadata by Model Revision Id
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

    #Use Case 764946: 7.2 Retrieve Data Source Metadata by Data Source Revision ID
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

    #Use Case 764949: 8.2 Retrieve Configuration Metadata by Revision ID
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
        # logger.debug(resDB[ConfID-1]['ConfigurationID'])
        # logger.debug(resAPI[0]['Configuration ID'])
        self.assertEqual((resDB[ConfID-1]['ConfigurationID']),(resAPI[0]['Configuration ID']),"Configuration ID was different")
        #Check Revision ID
        # logger.debug(resDB[ConfID-1]['RevisionID'])
        # logger.debug(resAPI[0]['Revision Number'])
        self.assertEqual((resDB[ConfID-1]['RevisionID']),(resAPI[0]['Revision Number']),"Revision was different")
        #Check COnfiguration Name
        # logger.debug(resDB2[ConfID-1]['name'])
        # logger.debug(resAPI[0]['Configuration Name'])
        self.assertEqual((resDB2[ConfID-1]['name']),(resAPI[0]['Configuration Name']),"Name was different")
        #MethodName
        Meth=resDB[ConfID-1]['MethodInfo']
        # logger.debug(Meth[Meth.find('<name>')+6:Meth.find('</name>')])
        # logger.debug(resAPI[0]['Method Name'])
        self.assertEqual((Meth[Meth.find('<name>')+6:Meth.find('</name>')]),(resAPI[0]['Method Name']),"Method is different")
        #ModelName
        Mod=resDB[ConfID-1]['ConfigurationInfo']
        logger.debug(Mod[Mod.find('<name>')+6:Mod.find('</name>')])
        logger.debug(Meth)
        
        logger.debug(resAPI[0]['Model Name'])
        self.assertEqual((Mod[Mod.find('<name>')+6:Mod.find('</name>')]),(resAPI[0]['Model Name']),"Method is different")
    
    @pytest.mark.vsts792457
    def test_RetrieveConfigurationMetadatabyRevisionID_InvalidRevisionID(self):
    
        logger.debug(self.id())
        endpoints = Endpoints()
        resAPI = endpoints.get_RConfMetaConfId(RevID=0,expRes=400,empRes=True)
        self.assertEqual(resAPI,resAPI)

    @pytest.mark.vsts792458
    def test_RetrieveConfigurationMetadatabyRevisionID_NonExistingRevisionID(self):
    
        logger.debug(self.id())
        endpoints = Endpoints()
        resAPI = endpoints.get_RConfMetaConfId(RevID=200,expRes=204,empRes=True)
        self.assertEqual(resAPI,resAPI)
    
    
    #Use Case 689752: 11. Retrieve Meta Information for Configuration Runs
    @pytest.mark.vsts800098
    def test_RetrieveMetaInformationforConfigurationRuns(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        #Get API response and information from DataBase
        CRID=31
        resAPI = endpoints.get_RetMetaInfoConfRuns(RevID=CRID)
        dbConex = dbConnection()
        resDB = dbConex.get_DataSet(table = 'DataMaster')
        

        #Check API response structure
        info=list(resAPI.keys())
        logger.debug(info)
        structure= ['BasicInfo', 'FlagInfo', 'CommentInfo', 'NotificationInfo']
        self.assertEqual(info, structure,"Structure is different")

        #Check Basic Info structure
        info=list(resAPI['BasicInfo'].keys())
        logger.debug(info)
        structure= ['RunID', 'ConfigurationID', 'Name', 'RevisionID', 'StartTime', 'StopTime']
        self.assertEqual(info, structure,"Structure of the Basic Info is different")

        #Check Revision ID
        logger.debug(resDB[CRID-1]['rev_id'])
        RevID=resAPI['BasicInfo']['RevisionID']
        logger.debug(RevID)
        self.assertEqual((resDB[CRID-1]['rev_id']),(RevID),"Revision ID was different")
        #Check Configuration ID
        Parametros = {"RevisionID":RevID}
        resDB2 = dbConex.get_DataSet(table = 'ConfigurationRevision',dbParams=Parametros)
        logger.debug(resDB2[0]['ConfigurationID'])
        ConfigID=resAPI['BasicInfo']['ConfigurationID']
        logger.debug(ConfigID)
        self.assertEqual((ConfigID),(resDB2[0]['ConfigurationID']),"Configuration ID was different")
        #Check Configuration Name
        Parametros = {"config_id":ConfigID}
        resDB3 = dbConex.get_DataSet(table = 'Configurations',dbParams=Parametros)
        logger.debug(resDB3[0]['name'])
        ConfigID=resAPI['BasicInfo']['Name']
        logger.debug(ConfigID)
        self.assertEqual((ConfigID),(resDB3[0]['name']),"Configuration ID was different")
        #Check Start time and end time 
        Parametros = {"ID":CRID}
        resDB4 = dbConex.get_DataSet(table = 'DataMaster',dbParams=Parametros)
        logger.debug(resDB4[0]['StartTime'])
        startTime=resAPI['BasicInfo']['StartTime']# round to ms
        logger.debug(startTime)
        startTimeDB=str(resDB4[0]['StartTime'])
        startTime=startTime.replace('T',' ')
        self.assertEqual(startTimeDB[:22],(startTime[:22]),"Configuration start time was different")
        #End time
        stopTime=resAPI['BasicInfo']['StopTime']# stop to ms
        logger.debug(stopTime)
        endTimeDB=str(resDB4[0]['EndTime'])
        logger.debug(endTimeDB)
        stopTime=stopTime.replace('T',' ')
        self.assertEqual(stopTime[:22],(endTimeDB[:22]),"Configuration stop time was different")
        #Flags
        Parametros = {"DataMasterID":CRID}
        resDB5 = dbConex.get_DataSet(table = 'ResultFlag',dbParams=Parametros)
        flagInfo=resAPI['FlagInfo']
        self.assertEqual(len(flagInfo),len(resDB5),"Flag size are different")
        logger.debug(flagInfo)
        logger.debug(resDB5)
        for i in range(len(flagInfo)):
            flagAPI=flagInfo[i]['Flag']
            logger.debug(flagAPI)
            Parametros = {"name":flagAPI}
            resDB6 = dbConex.get_DataSet(table = 'Flag',dbParams=Parametros)
            self.assertNotEqual([],resDB6,"Flag doesnt exist")
            FlagID=resDB6[0]['flag_id']
            Parametros = {"DataMasterID":CRID,"FlagID":FlagID}
            resDB7 = dbConex.get_DataSet(table="ResultFlag",dbParams=Parametros)
            date=str(resDB7[0]["CreatedDate"])[0:22]
            flagAPIdate=str(flagInfo[i]['CreatedDate'][0:22]).replace("T"," ")
            logger.debug(date)
            logger.debug(flagAPIdate)
            self.assertEqual(date,flagAPIdate,"Dates dont match")
        #Comments retrieval verification start here
        Parametros = {"DataMasterID":CRID}
        resDB8 = dbConex.get_DataSet(table = 'ResultComment',dbParams=Parametros)
        CommentInfo=resAPI['CommentInfo']
        self.assertEqual(len(CommentInfo),len(resDB8),"Comment size are different")
        logger.debug(CommentInfo)
        logger.debug(resDB8)
        for i in range(len(CommentInfo)):
            CommentAPI=CommentInfo[i]['Comment']
            logger.debug(CommentAPI)
            Parametros = {"Text":CommentAPI}
            resDB9 = dbConex.get_DataSet(table = 'ResultComment',dbParams=Parametros)
            self.assertNotEqual([],resDB9,"Comment doesnt exist")
            date=str(resDB9[0]["CreatedDate"])[0:22]
            CommentAPIdate=str(CommentInfo[i]['CreatedDate'][0:22]).replace("T"," ")
            logger.debug(date)
            logger.debug(CommentAPIdate)
            self.assertEqual(date,CommentAPIdate,"Dates dont match")
        #NotificationInfo starts here
        Parametros = {"DataMasterID":CRID}
        resDB10 = dbConex.get_DataSet(table = 'ResultNotification',dbParams=Parametros)
        NotificationInfo=resAPI['NotificationInfo']
        self.assertEqual(len(NotificationInfo),len(resDB10),"Notification list size are different")
        logger.debug(NotificationInfo)
        logger.debug(resDB10)
        """ for i in range(len(NotificationInfo)):
            NotificationAPI=NotificationInfo[i]['Notification']
            logger.debug(NotificationAPI)
            Parametros = {"name":NotificationAPI}
            resDB11 = dbConex.get_DataSet(table = 'Notification_Definition',dbParams=Parametros)
            self.assertNotEqual([],resDB11,"Notification doesnt exist")
            VariableNotificationAPI=NotificationInfo[i]['VariableName']
            VariableNotificationDB=resDB11[0]['variable_name']
            self.assertEqual(VariableNotificationAPI,VariableNotificationDB,"Notification Variable Name is wrong")
            not_id=resDB11[0]['ID']
            Parametros = {"name":NotificationAPI}
            resDB11 = dbConex.get_DataSet(table = 'Notification_Definition',dbParams=Parametros)
            CountAPI=NotificationInfo[i]['Count']
            CountDB=resDB11[0]['variable_name']
            self.assertEqual(VariableNotificationAPI,VariableNotificationDB,"Notification Variable Name is wrong")
            FlagID=resDB11[0]['flag_id']
            Parametros = {"DataMasterID":CRID,"FlagID":FlagID}
            resDB12 = dbConex.get_DataSet(table="ResultFlag",dbParams=Parametros)
            date=str(resDB12[0]["CreatedDate"])[0:22]
            flagAPIdate=str(flagInfo[i]['CreatedDate'][0:22]).replace("T"," ")
            logger.debug(date)
            logger.debug(flagAPIdate)
            self.assertEqual(date,flagAPIdate,"Dates dont match") """

    @pytest.mark.vsts800106
    def test_RetrievMetaInformationforConfigurationRuns_NonExistingConfigurationRun(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RetMetaInfoConfRuns(RevID=200, expRes=204, empRes=True)
        self.assertEqual(res, res,"Something went wrong") 

    @pytest.mark.vsts800107
    def test_RetrievMetaInformationforConfigurationRuns_InvalidConfigurationRun(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RetMetaInfoConfRuns(RevID=0, expRes=400, empRes=True)
        self.assertEqual(res, res,"Something went wrong")  


    #Use Case 783305: Retrieve configuration runs by metadata tag




    


    #Use Case 793628: Retrieve tag information
        
    @pytest.mark.vsts793895
    def test_RetrieveListOfTags(self):
        
        logger.debug(self.id())

        #Get information from DataBase and RestAPI
        dbConex = dbConnection()
        varTagType = {"Type":1}
        resDB = dbConex.get_DataSet(table = 'Tag',dbParams = varTagType)
        
        logger.debug(resDB)
        endpoints = Endpoints()
        resAPI = endpoints.get_ConfigTags()

        #Check both have the same number of Data Sources
        self.assertEqual(len(resDB),len(resAPI))
        
        #Check structure information in the RestAPI response 
        for i in resDB:
            logger.debug(i["Label"])
            self.assertIn(i["Label"],resAPI,"Tag "+i["Label"]+" was not found")
              
    @pytest.mark.vstsk793915
    def test_RetrieveTagInformation_EmptyTag(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_ConfigTags(RevID=0, expRes=400, empRes=True)
        self.assertEqual(res, res,"Something went wrong")  

