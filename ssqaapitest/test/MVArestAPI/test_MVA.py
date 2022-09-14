from ast import Param
from cmath import exp
from fileinput import filename
from xml.etree.ElementTree import ElementTree
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
        aleat= random.randint(1, len(resAPI))
        logger.debug(aleat)
        #ModelID
        """ 
        logger.debug((resDB[aleat-1]['DataSourceID']))
        logger.debug(resAPI[-aleat]['Id']) """
        self.assertEqual((resDB[aleat-1]['ModelID']),(resAPI[aleat-1]['ModelId']))
        #ModelID
        """ logger.debug((resDB[aleat-1]['RevisionID']))
        logger.debug(resAPI[-aleat]['RevisionId']) """
        Parametros={'RevisionID':resAPI[aleat-1]['RevisionID']}
        resDBnew = dbConex.get_DataSet(table = 'ModelRevision',dbParams=Parametros)
        self.assertEqual((resDBnew[0]['ModelID']),(resAPI[aleat-1]['ModelId']),'Revision')
        #Name
        #logger.debug(resAPI[aleat-1]['Name']) 
        Name=resDB[aleat-1]['ModelInfo']
        #logger.debug(Name[Name.find('name="')+6:Name.find('" modelsoftware')])
        self.assertEqual((Name[Name.find('name="')+6:Name.find('" modelsoftware')]),(resAPI[aleat-1]['Name']))
        #Created
        """ logger.debug(str(resDB[aleat-1]['UploadDate'])[0:22])
        logger.debug(resAPI[-aleat]['UploadedDate'][0:10]+' '+resAPI[aleat-1]['UploadedDate'][11:22]) """
        Parametros={'RevisionID':resAPI[aleat-1]['RevisionID']}
        resDBnew = dbConex.get_DataSet(table = 'ModelRevision',dbParams=Parametros)
        self.assertEqual(str(resDBnew[0]['UploadDate'])[0:22],(resAPI[aleat-1]['UploadedDate'][0:10]+' '+resAPI[aleat-1]['UploadedDate'][11:22]))
        #IsEnabled
        """ logger.debug(bool(resDB2[aleat-1]['Disabled']))
        logger.debug(resAPI[-aleat]['IsEnabled']) """
        Parametros={'ModelId':resDB[aleat-1]['ModelID']}
        resDBen = dbConex.get_DataSet(table = 'Model',dbParams=Parametros)
        self.assertFalse(bool(resDBen[0]['Disabled']),resAPI[aleat-1]['IsEnabled'])
        #IsEnabled
        
        logger.debug((resDB[aleat-1]['UploadedBy']))
        logger.debug(resAPI[aleat-1]['UploadedBy'])
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

    @pytest.mark.vsts791782
    def test_RetrieveRawData_ConfigurationRunWithoutRawData(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RawDataID(RevID=33,Titulo='WithoutRawData',expRes=204,empRes=True)
        self.assertEqual(res, res,"Something went wrong")
    
    @pytest.mark.vsts791780
    def test_RetrieveRawData_InvalidConfigurationRunID(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RawDataID(RevID=0,Titulo='InvalidConfigurationRUn',expRes=400,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts791781
    def test_RetrieveRawData_NonExistingConfigurationRun(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RawDataID(RevID=200,Titulo='NonexistingConfigurationRUn',expRes=204,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts797976
    def test_RetrieveRawData_LastNRows(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RawDataLastNRows(RevID=1,Rows=3)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataIDLastNRows.json')
        self.assertEqual(res, resExp,"Something went wrong")
    
    @pytest.mark.vsts797978
    def test_RetrieveRawData_LastNRowsInvalidNumberOfRows(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RawDataLastNRows(RevID=1,Rows=0,expRes=400,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts788347
    def test_RetrieveRawData_OffsetAndRows(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDIDOffset(RevID=1,Rows=2,Off=109)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataIDOffsetandRows.json')
        self.assertEqual(res, resExp,"Something went wrong")

    

    @pytest.mark.vsts791778
    def test_RetrieveRawData_OffsetAndRows_IncorrectQuery(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDIDOffset(RevID=1,Rows=5,Off=0,Titulo='IncorrectQuery',expRes=400,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts791775
    def test_RetrieveRawData_OffsetAndRows_LowerLimit(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDIDOffset(RevID=1,Rows=3,Off=1,Titulo='LowerLimit')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataIDOffsetandRowsLowerLimit.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts791779
    def test_RetrieveRawData_OffsetAndRows_RequestRowsoutOfLimits(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDIDOffset(RevID=1,Rows=5,Off=11,Titulo='OutofLimits',expRes=204,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts791777
    def test_RetrieveRawData_OffsetAndRows_UpperLimit(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDIDOffset(RevID=1,Rows=1,Off=10,Titulo='UpperLimit')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataIDOffsetandRowsUpperLimit.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792162
    def test_RetrieveRawData_OffsetAndRows_RawDataPartiallyOutOfScope(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDIDOffset(RevID=1,Rows=5,Off=114,Titulo='PartiallyOutOfScope')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataIDOffsetandRowsPartiallyOutOfScope.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts797965
    def test_RetrieveRawData_Recent_NonexistingDataforSelectedTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDRecent(RevID=1,Time=5,Titulo='NonexistingDataforSelectedTime',expRes=204,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts797975
    def test_RetrieveRawData_Recent_NotValidRecentTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDRecent(RevID=1,Time=-1,Titulo='NotValidRecentTime',expRes=400,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts797778
    def test_RetrieveRawData_StartandStopTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDStartStopTime(RevID=1,Start="2022-07-06 16:30:32.7003273",Stop="2022-07-06 16:33:11.1126355")
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataStartStopTime.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts797793
    def test_RetrieveRawData_StartandStopTime_NoConfigurationRunExistsWithSpecifiedStopTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDStartStopTime(RevID=1,Start="2022-07-06 16:25:00.00",Stop="2022-07-06T16:32:36.04",expRes=204,empRes=True,Titulo="NoconfigurationExistswithspecifeidstoptime")
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts797792
    def test_RetrieveRawData_StartandStopTime_NoConfigurationRunExistsWithSpecifiedStartTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDStartStopTime(RevID=1,Start="2022-07-06T16:32:38.00",Stop="2022-07-06T16:32:38.50",expRes=204,empRes=True,Titulo="NoconfigurationExistswithspecifeidsarttime")
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts797931
    def test_RetrieveRawData_StartandStopTime_NotvalidStartTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDStartStopTime(RevID=1,Start="-2022-07-06 15:20:16.30",Stop="2022-07-06 16:33:11.1126355",expRes=400,empRes=True,Titulo="NotValidStartTime")
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts797934
    def test_RetrieveRawData_StartandStopTime_NotvalidStopTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDStartStopTime(RevID=1,Start="2022-07-06 16:30:32.7003273",Stop="2022-07-06 16:15:32.7003273",expRes=400,empRes=True,Titulo="NotValidStopTime")
        self.assertEqual(res, res,"Something went wrong")
    
    @pytest.mark.vsts797944
    def test_RetrieveRawData_StartTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDStartTime(RevID=1,Start="2022-07-06T16:32:36.0523491")
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataStartTime.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts797957
    def test_RetrieveRawData_StartTime_InvalidStartTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDStartTime(RevID=1,Start="-2022-07-06 16:30:32.7003273",Titulo="Notvalid",expRes=400,empRes=True)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataStartTime.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts797956
    def test_RetrieveRawData_StartTime_NonExistingConfigurationRunWithSelectedStartTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RDStartTime(RevID=1,Start="2022-07-06 00:00:00.00",Titulo="Notvalid",expRes=204,empRes=True)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataStartTime.json')
        self.assertEqual(res, resExp,"Something went wrong")


    #Use Case 782953: Raw Data includes CDM values

    @pytest.mark.vsts800049
    def test_RetrieveRawData_CDMValues(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RawDataID(RevID=27,Titulo="CDMValues")
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RawDataIDCDMValues.json')
        self.assertEqual(res, resExp,"Something went wrong")

    #Use Case 689753: 12. Retrieve Result Matrices for Configuration Run
    @pytest.mark.vsts792977
    def test_RetrieveResultMatricesForConfigurationRun_ClassificationTable_SampleDistances(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMConfRun(RevID=14,Titulo='ClassificationTable_SampleDistances')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ResMatConfRunClassificationTable_SampleDistances.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792984
    def test_RetrieveResultMatricesForConfigurationRun_Concentration(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMConfRun(RevID=18,Titulo='Concentration')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ResMatConfRunConcentration.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts788391
    def test_RetrieveResultMatricesForConfigurationRun_Scores_HotellingsT2_Residuals_FResiduals(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMConfRun(RevID=13,Titulo='Scores_HotellingsT2_Residuals_FResiduals')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ResMatConfRunConcentration_Scores_HotellingsT2_Residuals_FResiduals.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792978
    def test_RetrieveResultMatricesForConfigurationRun_YPrediction_YCorrected(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMConfRun(RevID=19,Titulo='YPrediction_YCorrected')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('ResMatConfRunConcentration_YPrediction_YCorrected.json')
        self.assertEqual(res, resExp,"Something went wrong")



        
    #Use Case 689754: 13. Retrieve Result Matrices by Name

    @pytest.mark.vsts788393
    def test_RetrieveResultMatricesByName_FullList(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameFullList(RevID=14,MatrixName='Scores')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RetResMatbyName.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792196
    def test_RetrieveResultMatricesByName_MatrixNonexistentfortheConfigurationRun(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameFullList(RevID=1,MatrixName='Scores',Titulo='MatrixNonexistentfortheCOnfigurationRun',expRes=204,empRes=True)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RetResMatbyName.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792197
    def test_RetrieveResultMatricesByName_NonExistingResultMatrix(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameFullList(RevID=14,MatrixName='NonExistingMatrix',Titulo='MatrixNonexistentMatrix',expRes=400,empRes=True)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RetResMatbyName.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts788392
    def test_RetrieveResultMatricesByName_NotValidConfigurationID(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameFullList(RevID=0,MatrixName='Scores',expRes=400,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts792193
    def test_RetrieveResultMatricesByName_NonexistingConfigurationRun(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameFullList(RevID=99,MatrixName='Scores',expRes=204,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts788398
    def test_RetrieveResultMatricesByName_OffsetandRows(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameOffsetAndRows(RevID=14,MatrixName='Scores',Titulo='OffsetNRows',Offset='2',Rows='2')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RetResMatbyNameOffsetNRows.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792191
    def test_RetrieveResultMatricesByName_OffsetandRows_InvalidRow(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameOffsetAndRows(RevID=14,MatrixName='Scores',Offset='0',Rows='2',expRes=400,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts792189
    def test_RetrieveResultMatricesByName_OffsetandRows_RowsPartiallyOutOfScope(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameOffsetAndRows(RevID=14,MatrixName='Scores',Titulo='OffsetNRowsRowsPartiallyOutOfScope',Offset='3',Rows='20')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RetResMatbyNameOffsetNRowsRowsPartiallyOutOfScope.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792190
    def test_RetrieveResultMatricesByName_OffsetandRows_SpecifiedRowsOutOfScope(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameOffsetAndRows(RevID=14,MatrixName='Scores',Titulo='OffsetNRowsSpecifiedRowsOutOfScope',Offset='20',Rows='5')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RetResMatbyNameOffsetNRowsSpecifiedRowsOutOfScope.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792188
    def test_RetrieveResultMatricesByName_OffsetandRows_UpperLimit(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameOffsetAndRows(RevID=14,MatrixName='Scores',Titulo='OffsetNRowsUpperLimit',Offset='10',Rows='1')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RetResMatbyNameOffsetNRowsUpperLimit.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792187
    def test_RetrieveResultMatricesByName_OffsetandRows_LowerLimit(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameOffsetAndRows(RevID=14,MatrixName='Scores',Titulo='OffsetNRowsLowerLimit',Offset='1',Rows='1')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RetResMatbyNameOffsetNRowsLowerLimit.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts788415
    def test_RetrieveResultMatricesByName_StartandStopTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameStartnStop(RevID=1,StartTime="2022-07-06 16:30:32.7003273",StopTime="2022-07-06 16:33:11.1126355",RevID=14,MatrixName='Scores',Titulo='StartnStop')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RetResMatbyNameStartnStop.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792939
    def test_RetrieveResultMatricesByName_StartandStopTime_NoConfigurationRunExistwithSpecifiedStartTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameStartnStop(RevID=1,StartTime="2022-07-06T16:32:38.00",StopTime="2022-07-06T16:32:38.50",RevID=14,MatrixName='Scores',expRes=204,empRes=True)
        self.assertEqual(res, res,"Something went wrong")
    
    @pytest.mark.vsts792940
    def test_RetrieveResultMatricesByName_StartandStopTime_NoConfigurationRunExistwithSpecifiedStopTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameStartnStop(RevID=1,StartTime="2022-07-06 16:25:00.00",StopTime="2022-07-06T16:32:36.04",RevID=14,MatrixName='Scores',expRes=204,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts792936
    def test_RetrieveResultMatricesByName_StartandStopTime_NotValidStartTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameStartnStop(RevID=1,StartTime="2022-07-06 16:30:32.7003273",StopTime="2022-07-06 16:15:32.7003273",RevID=14,MatrixName='Scores',expRes=400,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts792937
    def test_RetrieveResultMatricesByName_StartandStopTime_NotValidStopTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameStartnStop(RevID=1,StartTime="-2022-07-06 15:20:16.30",StopTime="2022-07-06 16:33:11.1126355",RevID=14,MatrixName='Scores',expRes=400,empRes=True)
        self.assertEqual(res, res,"Something went wrong")
    
    @pytest.mark.vsts788413
    def test_RetrieveResultMatricesByName_StartTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameStartnStop(RevID=1,StartTime="2022-07-06 16:30:32.7003273",RevID=14,MatrixName='Scores',Titulo='StartnStop')
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RetResMatbyNameStartnStop.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts792944
    def test_RetrieveResultMatricesByName_StartTime_NoConfigurationRunExistwithSpecifiedStartTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameStartTime(RevID=1,StartTime="2022-07-06T16:32:38.00",RevID=14,MatrixName='Scores',expRes=204,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts792942
    def test_RetrieveResultMatricesByName_StartTime_NotValidStartTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameStartTime(RevID=1,StartTime="2022-07-06 16:30:-32.7003273",RevID=14,MatrixName='Scores',expRes=400,empRes=True)
        self.assertEqual(res, res,"Something went wrong")


    @pytest.mark.vsts797606
    def test_RetrieveResultMatricesByName_LastN(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameLastN(RevID=14,MatrixName='Scores',Titulo='LastNRows',LRows=2)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RetResMatbyNameLastNRows.json')
        self.assertEqual(res, resExp,"Something went wrong")

    @pytest.mark.vsts798155
    def test_RetrieveResultMatricesByName_LastN_InvalidNumberOfRows(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameLastN(RevID=14,MatrixName='Scores',Titulo='LastNRows',LRows=0,expRes=400,empRes=True)
        jsonUtil = JsonUtility('MVArestAPI')
        resExp = jsonUtil.read_Json('RetResMatbyNameLastNRows.json')
        self.assertEqual(res, resExp,"Something went wrong")


    @pytest.mark.vsts798158
    def test_RetrieveResultMatricesByName_Recent_InvalidRecentTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameRecent(RevID=14,MatrixName='Scores',Titulo='InvalidRecentTime',RTime=-500,expRes=400,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts798160
    def test_RetrieveResultMatricesByName_Recent_NoConfigurationRunExistintheSpecifiedRecentTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameRecent(RevID=14,MatrixName='Scores',RTime=500,expRes=204,empRes=True)
        self.assertEqual(res, res,"Something went wrong")

    @pytest.mark.vsts798160
    def test_RetrieveResultMatricesByName_Recent_NoConfigurationRunExistintheSpecifiedRecentTime(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_RRMatricesNameRecent(RevID=14,MatrixName='Scores',RTime=500,expRes=204,empRes=True)
        self.assertEqual(res, res,"Something went wrong")


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
        structure= ['Configuration ID', 'Configuration Name', 'Revision Number', 'Data Source Name', 'Data Source ID', 'Data Source Revision Number', 'Data Source Revision ID', 'Method Name', 'Model Name', 'Model ID', 'Model Revision Number', 'Model Revision ID', 'Transformations', 'Online Calculations', 'Output', 'Notifications', 'Users With Access']
        self.assertEqual(info, structure,"Structure is different")

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


        Parametros = {"DataMasterID":CRID}
            
        resDB11 = dbConex.get_DataSet(table = 'ResultNotification',dbParams=Parametros)
        i=0
        logger.debug(resDB11)
        for element in resDB11:
            logger.debug(element)
            definitionID=element['DefinitionID']
            count=element['Count']
            firstResultID=element['FirstResultID']
            lastResultID=element['LastResultID']

            CountAPI=NotificationInfo[i]['Count']
            self.assertEqual(count,CountAPI,"Notification count  are different")
            logger.debug(count)
            logger.debug(CountAPI)
            Parametros = {"ID":definitionID}
            resDB12 = dbConex.get_DataSet(table = 'Notification_Definition',dbParams=Parametros)
            
            nameDB=resDB12[0]['name']
            variableNameDB=resDB12[0]['variable_name']
            nameApi=NotificationInfo[i]['Notification']
            variableNameAPi=NotificationInfo[i]['VariableName']
            logger.debug(nameDB)
            logger.debug(nameApi)
            logger.debug(variableNameDB)
            logger.debug(variableNameAPi)


            self.assertEqual(nameDB,nameApi,"Notification name are different")
            self.assertEqual(variableNameDB,variableNameAPi,"Notification variable name  are different")
            
            #First result
            Parametros = {"ResultID":firstResultID}
            resDB13=dbConex.get_DataSet(table = 'ResultData',dbParams=Parametros)
            fristSampleTimeDB=str(resDB13[0]['SampleTimeStamp'])[0:21]
            fristSampleTimeAPI=str(NotificationInfo[i]['FirstSample']['SampleTime'])[0:21].replace("T"," ")
            self.assertEqual(fristSampleTimeDB,fristSampleTimeAPI,"Notification first sample time  are different")
            rawDataIDDB=resDB13[0]['RawDataID']
            rawDataIDAPI=NotificationInfo[i]['FirstSample']['SampleID']
            self.assertEqual(rawDataIDDB,rawDataIDAPI,"Notification first sample ID  are different")

            #Last Sample
            Parametros = {"ResultID":lastResultID}
            resDB13=dbConex.get_DataSet(table = 'ResultData',dbParams=Parametros)
            lastSampleTimeDB=str(resDB13[0]['SampleTimeStamp'])[0:21]
            lasttSampleTimeAPI=str(NotificationInfo[i]['LastSample']['SampleTime'])[0:21].replace("T"," ")
            self.assertEqual(lastSampleTimeDB,lasttSampleTimeAPI,"Notification last sample time  are different")
            rawDataIDDB=resDB13[0]['RawDataID']
            rawDataIDAPI=NotificationInfo[i]['LastSample']['SampleID']
            self.assertEqual(rawDataIDDB,rawDataIDAPI,"Notification last sample ID  are different")

            i+=1

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

    @pytest.mark.vsts793677
    def test_RetrieveConfigurationRunsbyMetadataTag_MandatoryPhaseTag(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        #Get API response and information from DataBase
        dbConex = dbConnection()
        TName='Product'
        TValue='Fases2'
        resAPI = endpoints.get_RetConfRunbyMetaTag(Titulo='MandatoryPhaseTag',TagName=TName,TagValue=TValue)
        #Check structure of the response
        logger.debug(resAPI[5].keys())
        Structure=['ConfigurationInfo', 'TagsInfo']
        StrucAPI=list(resAPI[5].keys())
        self.assertEqual(Structure,StrucAPI,'The information structure is diferent')
        #Check structure of the Tags information
        logger.debug(resAPI[5]['TagsInfo'].keys())
        Structure=['MetadataTags', 'PhaseTags']
        StrucAPI=list(resAPI[5]['TagsInfo'].keys())
        self.assertEqual(Structure,StrucAPI,'The Tags information structure is diferent')
        #Check if the same number of runs are in the DB and in the RestAPI
        Parametros={'Type':1,'Label':TName}
        resDB = dbConex.get_DataSet(table = 'Tag', dbParams=Parametros)
        logger.debug(resDB)
        TagID=resDB[0]['ID']
        Parametros={'TagID':TagID,'Value':TValue,'IsLatest':1}
        resDB = dbConex.get_DataSet(table = 'DataMasterTag', dbParams=Parametros)
        logger.debug(resDB)
        TagModID=[]
        for element in resDB:
            TagModID.append(element['DataMasterTagModification'])
        logger.debug(TagModID)
        Expe=[]
        for element in TagModID:
            Parametros={'ID':element}
            resDB=dbConex.get_DataSet(table = 'DataMasterTagModification',dbParams= Parametros)
            Expe.append(resDB[0]['DataMasterID'])
        logger.debug(Expe)
        self.assertEqual(len(Expe),len(resAPI),"They dont have the sam enumber of Configuration Runs")
        #Create a Dictionary to assosiate Label Tag with TagID
        Tags={}
        Parametros={'Type':1}
        resDB = dbConex.get_DataSet(table = 'Tag', dbParams=Parametros)
        for element in resDB:
            Tags[element["ID"]]=element["Label"] 

        #Verify Information of every ConfigurationRun in the RestAPI
        for element in resAPI:
            #Check ConfigurationInfo
            Parametros={'ID':element['ConfigurationInfo']['RunID']}
            resDB=dbConex.get_DataSet(table = 'DataMaster',dbParams= Parametros)
            logger.debug(element['ConfigurationInfo']['RevisionID'])
            logger.debug(resDB[0]['rev_id'])
            revID=resDB[0]['rev_id']
            self.assertEqual(element['ConfigurationInfo']['RevisionID'],revID,'Revision ID is not the same')
            logger.debug(str(resDB[0]['StartTime'])[:22])
            logger.debug(((element['ConfigurationInfo']['StartTime']).replace('T',' '))[:22])
            self.assertEqual(str(resDB[0]['StartTime'])[:22],((element['ConfigurationInfo']['StartTime']).replace('T',' '))[:22],'StartTime is diferent in this experiment')
            logger.debug(str(resDB[0]['EndTime'])[:22])
            logger.debug(((element['ConfigurationInfo']['StopTime']).replace('T',' '))[:22])
            self.assertEqual(str(resDB[0]['EndTime'])[:22],((element['ConfigurationInfo']['StopTime']).replace('T',' '))[:22],'StopTime is diferent in this experiment')
            Parametros={'RevisionID':revID}
            resDB=dbConex.get_DataSet(table = 'ConfigurationRevision',dbParams= Parametros)
            logger.debug(resDB[0]['ConfigurationID'])
            confID=resDB[0]['ConfigurationID']
            logger.debug(element['ConfigurationInfo']['ConfigurationID'])
            self.assertEqual(element['ConfigurationInfo']['ConfigurationID'],confID,'Configuration ID is not the same')
            Parametros={'config_id':confID}
            resDB=dbConex.get_DataSet(table = 'Configurations',dbParams= Parametros)
            logger.debug(resDB[0]['name'])
            logger.debug(element['ConfigurationInfo']['Name'])
            self.assertEqual(element['ConfigurationInfo']['Name'],resDB[0]['name'],'Configuration Name is not the same')
            #Check all the DataMasterModificationID that the experiment has
            Parametros={'DataMasterID':element['ConfigurationInfo']['RunID']}
            resDBnew=dbConex.get_DataSet(table = 'DataMasterTagModification',dbParams= Parametros)
            for ModID in resDBnew:
                Parametros2={'DataMasterTagModification':ModID['ID'],'IsLatest':1}
                resDBothernew=dbConex.get_DataSet(table = 'DataMasterTag',dbParams= Parametros2)
                
                for stuff in resDBothernew:
                    if stuff['PhaseId'] == None:
                        logger.debug(stuff['Value'])
                        logger.debug(element['TagsInfo']['MetadataTags'][Tags[stuff['TagID']]])
                        ValueTagDB=stuff['Value']
                        ValueTagAPI=element['TagsInfo']['MetadataTags'][Tags[stuff['TagID']]]
                        if ValueTagAPI=='':
                            ValueTagAPI=None
                        self.assertEqual(ValueTagDB,ValueTagAPI,'This Tag has a different value')
                    else:
                        logger.debug(stuff['Value'])
                        ValueDB=stuff['Value']
                        logger.debug(element['TagsInfo']['PhaseTags'][stuff['PhaseId']-1]['PhaseTags'][Tags[stuff['TagID']]])
                        ValueAPI=element['TagsInfo']['PhaseTags'][stuff['PhaseId']-1]['PhaseTags'][Tags[stuff['TagID']]]
                        if ValueAPI=='':
                            ValueAPI=None
                        self.assertEqual(ValueDB,ValueAPI,'This Tag has not the same value')
    
    @pytest.mark.vsts793499
    def test_RetrieveConfigurationRunsbyMetadataTag_EmptyTag(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        #Get API response and information from DataBase
        dbConex = dbConnection()
        TName='Tag3'
        TValue='someVale'
        resAPI = endpoints.get_RetConfRunbyMetaTag(Titulo='EmptyTag',TagName=TName,TagValue=TValue, expRes=204, empRes=True)
        logger.debug(resAPI)

    @pytest.mark.vsts793496
    def test_RetrieveConfigurationRunsbyMetadataTag_MandatoryTag(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        #Get API response and information from DataBase
        dbConex = dbConnection()
        TName='Experiment ID'
        TValue='OtroExp1'
        resAPI = endpoints.get_RetConfRunbyMetaTag(Titulo='MandatoryTag',TagName=TName,TagValue=TValue)
        #Check structure of the response
        logger.debug(resAPI[1].keys())
        Structure=['ConfigurationInfo', 'TagsInfo']
        StrucAPI=list(resAPI[1].keys())
        self.assertEqual(Structure,StrucAPI,'The information structure is diferent')
        #Check structure of the Tags information
        logger.debug(resAPI[1]['TagsInfo'].keys())
        Structure=['MetadataTags', 'PhaseTags']
        StrucAPI=list(resAPI[1]['TagsInfo'].keys())
        self.assertEqual(Structure,StrucAPI,'The Tags information structure is diferent')
        #Check if the same number of runs are in the DB and in the RestAPI
        Parametros={'Type':1,'Label':TName}
        resDB = dbConex.get_DataSet(table = 'Tag', dbParams=Parametros)
        logger.debug(resDB)
        TagID=resDB[0]['ID']
        Parametros={'TagID':TagID,'Value':TValue,'IsLatest':1}
        resDB = dbConex.get_DataSet(table = 'DataMasterTag', dbParams=Parametros)
        logger.debug(resDB)
        TagModID=[]
        for element in resDB:
            TagModID.append(element['DataMasterTagModification'])
        logger.debug(TagModID)
        Expe=[]
        for element in TagModID:
            Parametros={'ID':element}
            resDB=dbConex.get_DataSet(table = 'DataMasterTagModification',dbParams= Parametros)
            Expe.append(resDB[0]['DataMasterID'])
        logger.debug(Expe)
        self.assertEqual(len(Expe),len(resAPI),"They dont have the sam enumber of Configuration Runs")
        #Create a Dictionary to assosiate Label Tag with TagID
        Tags={}
        Parametros={'Type':1}
        resDB = dbConex.get_DataSet(table = 'Tag', dbParams=Parametros)
        for element in resDB:
            Tags[element["ID"]]=element["Label"] 

        #Verify Information of every ConfigurationRun in the RestAPI
        for element in resAPI:
            #Check ConfigurationInfo
            Parametros={'ID':element['ConfigurationInfo']['RunID']}
            resDB=dbConex.get_DataSet(table = 'DataMaster',dbParams= Parametros)
            logger.debug(element['ConfigurationInfo']['RevisionID'])
            logger.debug(resDB[0]['rev_id'])
            revID=resDB[0]['rev_id']
            self.assertEqual(element['ConfigurationInfo']['RevisionID'],revID,'Revision ID is not the same')
            logger.debug(str(resDB[0]['StartTime'])[:22])
            logger.debug(((element['ConfigurationInfo']['StartTime']).replace('T',' '))[:22])
            self.assertEqual(str(resDB[0]['StartTime'])[:22],((element['ConfigurationInfo']['StartTime']).replace('T',' '))[:22],'StartTime is diferent in this experiment')
            logger.debug(str(resDB[0]['EndTime'])[:22])
            logger.debug(((element['ConfigurationInfo']['StopTime']).replace('T',' '))[:22])
            self.assertEqual(str(resDB[0]['EndTime'])[:22],((element['ConfigurationInfo']['StopTime']).replace('T',' '))[:22],'StopTime is diferent in this experiment')
            Parametros={'RevisionID':revID}
            resDB=dbConex.get_DataSet(table = 'ConfigurationRevision',dbParams= Parametros)
            logger.debug(resDB[0]['ConfigurationID'])
            confID=resDB[0]['ConfigurationID']
            logger.debug(element['ConfigurationInfo']['ConfigurationID'])
            self.assertEqual(element['ConfigurationInfo']['ConfigurationID'],confID,'Configuration ID is not the same')
            Parametros={'config_id':confID}
            resDB=dbConex.get_DataSet(table = 'Configurations',dbParams= Parametros)
            logger.debug(resDB[0]['name'])
            logger.debug(element['ConfigurationInfo']['Name'])
            self.assertEqual(element['ConfigurationInfo']['Name'],resDB[0]['name'],'Configuration Name is not the same')
            #Check all the DataMasterModificationID that the experiment has
            Parametros={'DataMasterID':element['ConfigurationInfo']['RunID']}
            resDBnew=dbConex.get_DataSet(table = 'DataMasterTagModification',dbParams= Parametros)
            for ModID in resDBnew:
                Parametros2={'DataMasterTagModification':ModID['ID'],'IsLatest':1}
                resDBothernew=dbConex.get_DataSet(table = 'DataMasterTag',dbParams= Parametros2)
                
                for stuff in resDBothernew:
                    if stuff['PhaseId'] == None:
                        logger.debug(stuff['Value'])
                        logger.debug(element['TagsInfo']['MetadataTags'][Tags[stuff['TagID']]])
                        ValueTagDB=stuff['Value']
                        ValueTagAPI=element['TagsInfo']['MetadataTags'][Tags[stuff['TagID']]]
                        if ValueTagAPI=='':
                            ValueTagAPI=None
                        self.assertEqual(ValueTagDB,ValueTagAPI,'This Tag has a different value')
                    else:
                        logger.debug(stuff['Value'])
                        ValueDB=stuff['Value']
                        logger.debug(element['TagsInfo']['PhaseTags'][stuff['PhaseId']-1]['PhaseTags'][Tags[stuff['TagID']]])
                        ValueAPI=element['TagsInfo']['PhaseTags'][stuff['PhaseId']-1]['PhaseTags'][Tags[stuff['TagID']]]
                        if ValueAPI=='':
                            ValueAPI=None
                        self.assertEqual(ValueDB,ValueAPI,'This Tag has not the same value')
    
    @pytest.mark.vsts793498
    def test_RetrieveConfigurationRunsbyMetadataTag_NonexistingTag(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        #Get API response and information from DataBase
        dbConex = dbConnection()
        TName='NonExistingTag'
        TValue='Testing'
        resAPI = endpoints.get_RetConfRunbyMetaTag(Titulo='NonexistingTag',TagName=TName,TagValue=TValue, expRes=400, empRes=True)
        logger.debug(resAPI)

    @pytest.mark.vsts793497
    def test_RetrieveConfigurationRunsbyMetadataTag_PhaseTag(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        #Get API response and information from DataBase
        dbConex = dbConnection()
        TName='Tag2'
        TValue='PhaseTest2'
        resAPI = endpoints.get_RetConfRunbyMetaTag(Titulo='PhaseTag',TagName=TName,TagValue=TValue)
        #Check structure of the response
        logger.debug(resAPI[1].keys())
        Structure=['ConfigurationInfo', 'TagsInfo']
        StrucAPI=list(resAPI[1].keys())
        self.assertEqual(Structure,StrucAPI,'The information structure is diferent')
        #Check structure of the Tags information
        logger.debug(resAPI[1]['TagsInfo'].keys())
        Structure=['MetadataTags', 'PhaseTags']
        StrucAPI=list(resAPI[1]['TagsInfo'].keys())
        self.assertEqual(Structure,StrucAPI,'The Tags information structure is diferent')
        #Check if the same number of runs are in the DB and in the RestAPI
        Parametros={'Type':1,'Label':TName}
        resDB = dbConex.get_DataSet(table = 'Tag', dbParams=Parametros)
        logger.debug(resDB)
        TagID=resDB[0]['ID']
        Parametros={'TagID':TagID,'Value':TValue,'IsLatest':1}
        resDB = dbConex.get_DataSet(table = 'DataMasterTag', dbParams=Parametros)
        logger.debug(resDB)
        TagModID=[]
        for element in resDB:
            TagModID.append(element['DataMasterTagModification'])
        logger.debug(TagModID)
        Expe=[]
        for element in TagModID:
            Parametros={'ID':element}
            resDB=dbConex.get_DataSet(table = 'DataMasterTagModification',dbParams= Parametros)
            Expe.append(resDB[0]['DataMasterID'])
        logger.debug(Expe)
        self.assertEqual(len(Expe),len(resAPI),"They dont have the sam enumber of Configuration Runs")
        #Create a Dictionary to assosiate Label Tag with TagID
        Tags={}
        Parametros={'Type':1}
        resDB = dbConex.get_DataSet(table = 'Tag', dbParams=Parametros)
        for element in resDB:
            Tags[element["ID"]]=element["Label"] 

        #Verify Information of every ConfigurationRun in the RestAPI
        for element in resAPI:
            #Check ConfigurationInfo
            Parametros={'ID':element['ConfigurationInfo']['RunID']}
            resDB=dbConex.get_DataSet(table = 'DataMaster',dbParams= Parametros)
            logger.debug(element['ConfigurationInfo']['RevisionID'])
            logger.debug(resDB[0]['rev_id'])
            revID=resDB[0]['rev_id']
            self.assertEqual(element['ConfigurationInfo']['RevisionID'],revID,'Revision ID is not the same')
            logger.debug(str(resDB[0]['StartTime'])[:22])
            logger.debug(((element['ConfigurationInfo']['StartTime']).replace('T',' '))[:22])
            self.assertEqual(str(resDB[0]['StartTime'])[:22],((element['ConfigurationInfo']['StartTime']).replace('T',' '))[:22],'StartTime is diferent in this experiment')
            logger.debug(str(resDB[0]['EndTime'])[:22])
            logger.debug(((element['ConfigurationInfo']['StopTime']).replace('T',' '))[:22])
            self.assertEqual(str(resDB[0]['EndTime'])[:22],((element['ConfigurationInfo']['StopTime']).replace('T',' '))[:22],'StopTime is diferent in this experiment')
            Parametros={'RevisionID':revID}
            resDB=dbConex.get_DataSet(table = 'ConfigurationRevision',dbParams= Parametros)
            logger.debug(resDB[0]['ConfigurationID'])
            confID=resDB[0]['ConfigurationID']
            logger.debug(element['ConfigurationInfo']['ConfigurationID'])
            self.assertEqual(element['ConfigurationInfo']['ConfigurationID'],confID,'Configuration ID is not the same')
            Parametros={'config_id':confID}
            resDB=dbConex.get_DataSet(table = 'Configurations',dbParams= Parametros)
            logger.debug(resDB[0]['name'])
            logger.debug(element['ConfigurationInfo']['Name'])
            self.assertEqual(element['ConfigurationInfo']['Name'],resDB[0]['name'],'Configuration Name is not the same')
            #Check all the DataMasterModificationID that the experiment has
            Parametros={'DataMasterID':element['ConfigurationInfo']['RunID']}
            resDBnew=dbConex.get_DataSet(table = 'DataMasterTagModification',dbParams= Parametros)
            for ModID in resDBnew:
                Parametros2={'DataMasterTagModification':ModID['ID'],'IsLatest':1}
                resDBothernew=dbConex.get_DataSet(table = 'DataMasterTag',dbParams= Parametros2)
                
                for stuff in resDBothernew:
                    if stuff['PhaseId'] == None:
                        logger.debug(stuff['Value'])
                        logger.debug(element['TagsInfo']['MetadataTags'][Tags[stuff['TagID']]])
                        ValueTagDB=stuff['Value']
                        ValueTagAPI=element['TagsInfo']['MetadataTags'][Tags[stuff['TagID']]]
                        if ValueTagAPI=='':
                            ValueTagAPI=None
                        self.assertEqual(ValueTagDB,ValueTagAPI,'This Tag has a different value')
                    else:
                        logger.debug(stuff['Value'])
                        ValueDB=stuff['Value']
                        logger.debug(element['TagsInfo']['PhaseTags'][stuff['PhaseId']-1]['PhaseTags'][Tags[stuff['TagID']]])
                        ValueAPI=element['TagsInfo']['PhaseTags'][stuff['PhaseId']-1]['PhaseTags'][Tags[stuff['TagID']]]
                        if ValueAPI=='':
                            ValueAPI=None
                        self.assertEqual(ValueDB,ValueAPI,'This Tag has not the same value')

    @pytest.mark.vsts793495
    def test_RetrieveConfigurationRunsbyMetadataTag_Tag(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        #Get API response and information from DataBase
        dbConex = dbConnection()
        TName='Project Name'
        TValue='Prueba1'
        resAPI = endpoints.get_RetConfRunbyMetaTag(Titulo='Tag',TagName=TName,TagValue=TValue)
        #Check structure of the response
        logger.debug(resAPI[1].keys())
        Structure=['ConfigurationInfo', 'TagsInfo']
        StrucAPI=list(resAPI[1].keys())
        self.assertEqual(Structure,StrucAPI,'The information structure is diferent')
        #Check structure of the Tags information
        logger.debug(resAPI[1]['TagsInfo'].keys())
        Structure=['MetadataTags', 'PhaseTags']
        StrucAPI=list(resAPI[1]['TagsInfo'].keys())
        self.assertEqual(Structure,StrucAPI,'The Tags information structure is diferent')
        #Check if the same number of runs are in the DB and in the RestAPI
        Parametros={'Type':1,'Label':TName}
        resDB = dbConex.get_DataSet(table = 'Tag', dbParams=Parametros)
        logger.debug(resDB)
        TagID=resDB[0]['ID']
        Parametros={'TagID':TagID,'Value':TValue,'IsLatest':1}
        resDB = dbConex.get_DataSet(table = 'DataMasterTag', dbParams=Parametros)
        logger.debug(resDB)
        TagModID=[]
        for element in resDB:
            TagModID.append(element['DataMasterTagModification'])
        logger.debug(TagModID)
        Expe=[]
        for element in TagModID:
            Parametros={'ID':element}
            resDB=dbConex.get_DataSet(table = 'DataMasterTagModification',dbParams= Parametros)
            Expe.append(resDB[0]['DataMasterID'])
        logger.debug(Expe)
        self.assertEqual(len(Expe),len(resAPI),"They dont have the sam enumber of Configuration Runs")
        #Create a Dictionary to assosiate Label Tag with TagID
        Tags={}
        Parametros={'Type':1}
        resDB = dbConex.get_DataSet(table = 'Tag', dbParams=Parametros)
        for element in resDB:
            Tags[element["ID"]]=element["Label"] 

        #Verify Information of every ConfigurationRun in the RestAPI
        for element in resAPI:
            #Check ConfigurationInfo
            Parametros={'ID':element['ConfigurationInfo']['RunID']}
            resDB=dbConex.get_DataSet(table = 'DataMaster',dbParams= Parametros)
            logger.debug(element['ConfigurationInfo']['RevisionID'])
            logger.debug(resDB[0]['rev_id'])
            revID=resDB[0]['rev_id']
            self.assertEqual(element['ConfigurationInfo']['RevisionID'],revID,'Revision ID is not the same')
            logger.debug(str(resDB[0]['StartTime'])[:22])
            logger.debug(((element['ConfigurationInfo']['StartTime']).replace('T',' '))[:22])
            self.assertEqual(str(resDB[0]['StartTime'])[:22],((element['ConfigurationInfo']['StartTime']).replace('T',' '))[:22],'StartTime is diferent in this experiment')
            logger.debug(str(resDB[0]['EndTime'])[:22])
            logger.debug(((element['ConfigurationInfo']['StopTime']).replace('T',' '))[:22])
            self.assertEqual(str(resDB[0]['EndTime'])[:22],((element['ConfigurationInfo']['StopTime']).replace('T',' '))[:22],'StopTime is diferent in this experiment')
            Parametros={'RevisionID':revID}
            resDB=dbConex.get_DataSet(table = 'ConfigurationRevision',dbParams= Parametros)
            logger.debug(resDB[0]['ConfigurationID'])
            confID=resDB[0]['ConfigurationID']
            logger.debug(element['ConfigurationInfo']['ConfigurationID'])
            self.assertEqual(element['ConfigurationInfo']['ConfigurationID'],confID,'Configuration ID is not the same')
            Parametros={'config_id':confID}
            resDB=dbConex.get_DataSet(table = 'Configurations',dbParams= Parametros)
            logger.debug(resDB[0]['name'])
            logger.debug(element['ConfigurationInfo']['Name'])
            self.assertEqual(element['ConfigurationInfo']['Name'],resDB[0]['name'],'Configuration Name is not the same')
            #Check all the DataMasterModificationID that the experiment has
            Parametros={'DataMasterID':element['ConfigurationInfo']['RunID']}
            resDBnew=dbConex.get_DataSet(table = 'DataMasterTagModification',dbParams= Parametros)
            for ModID in resDBnew:
                Parametros2={'DataMasterTagModification':ModID['ID'],'IsLatest':1}
                resDBothernew=dbConex.get_DataSet(table = 'DataMasterTag',dbParams= Parametros2)
                
                for stuff in resDBothernew:
                    if stuff['PhaseId'] == None:
                        logger.debug(stuff['Value'])
                        logger.debug(element['TagsInfo']['MetadataTags'][Tags[stuff['TagID']]])
                        ValueTagDB=stuff['Value']
                        ValueTagAPI=element['TagsInfo']['MetadataTags'][Tags[stuff['TagID']]]
                        if ValueTagAPI=='':
                            ValueTagAPI=None
                        self.assertEqual(ValueTagDB,ValueTagAPI,'This Tag has a different value')
                    else:
                        logger.debug(stuff['Value'])
                        ValueDB=stuff['Value']
                        logger.debug(element['TagsInfo']['PhaseTags'][stuff['PhaseId']-1]['PhaseTags'][Tags[stuff['TagID']]])
                        ValueAPI=element['TagsInfo']['PhaseTags'][stuff['PhaseId']-1]['PhaseTags'][Tags[stuff['TagID']]]
                        if ValueAPI=='':
                            ValueAPI=None
                        self.assertEqual(ValueDB,ValueAPI,'This Tag has not the same value')

    @pytest.mark.vsts793676
    def test_RetrieveConfigurationRunsbyMetadataTag_WrongValue(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        #Get API response and information from DataBase
        dbConex = dbConnection()
        TName='Project Name'
        TValue='WrongValue'
        resAPI = endpoints.get_RetConfRunbyMetaTag(Titulo='WrongValue',TagName=TName,TagValue=TValue,expRes=400,empRes=True)
        

    #Use Case 793628: Retrieve tag information
        
    @pytest.mark.vsts793895
    def test_RetrieveTagInformation_ListOfTags(self):
        
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
              
    @pytest.mark.vsts793915
    def test_RetrieveTagInformation_EmptyTag(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_ConfigTags(Titulo='EmptyTag',LabelName='EmpTag', expRes=204, empRes=True)
        self.assertEqual(res, res,"Something went wrong")  

    @pytest.mark.vsts793880
    def test_RetrieveTagInformation_ListofValuesforaTag(self):
        
        #Get information from DataBase and RestAPI
        logger.debug(self.id())
        endpoints = Endpoints()
        Tag='Tag2'
        resAPI = endpoints.get_ConfigTags(Titulo='ListOfValues',LabelName=Tag)
        dbConex = dbConnection()
        varTagType = {"Type":1,"Label":Tag}
        resDB = dbConex.get_DataSet(table = 'Tag',dbParams = varTagType)
        logger.debug(resDB)
        TagID=resDB[0]['ID']
        logger.debug(TagID)
        Parametros = {"TagID":TagID}
        resDB = dbConex.get_DataSet(table = 'DataMasterTag',dbParams = Parametros)
        #logger.debug(resDB)
        #Check both have the same number of Data Sources
        TagValues=[]
        for element in resDB:
            TagValues.append(element['Value'])
        logger.debug('Estos values salieron')
        logger.debug(TagValues)
        for element in resAPI:
            logger.debug(element)
            self.assertIn(element,TagValues)
        
    @pytest.mark.vsts793904
    def test_RetrieveTagInformation_NonExistentTag(self):
        
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_ConfigTags(Titulo='NonExistingTag',LabelName='NonexistentTag', expRes=400, empRes=True)
        self.assertEqual(res, res,"Something went wrong")  