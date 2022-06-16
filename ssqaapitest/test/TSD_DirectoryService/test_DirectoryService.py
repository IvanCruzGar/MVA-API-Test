from distutils.log import debug
from unicodedata import name
import pytest
import unittest

from ssqaapitest.src.helpers.TSD_DirectoryService.request import Endpoints
from ssqaapitest.src.helpers.TSD_DirectoryService.dbConnection import dbConnection
from ssqaapitest.src.utilities.jsonUtility import JsonUtility
import logging as logger
import random

#13 pass, 
#http://172.22.4.151:8080/Aspentech/APM/TSDDirectoryService/swagger/index.html
#Needs Autorization
@pytest.mark.tsd_DirectoryService
class TestListElements(unittest.TestCase):

    #/CsvFileFormat
    @pytest.mark.vsts633397
    def test_CsvFileFormat(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_CsvFileFormat()
        dbUtil = dbConnection()
        dbData = dbUtil.get_CsvFileFormat()
        dbIdLst = []
        for element in dbData:
            dbIdLst.append(element['Id'])
        resIdLst = []
        for element in res:
            resIdLst.append(element['id'])
        self.assertListEqual(dbIdLst, resIdLst, f"{self.id()}  #/CsvFileFormat, List of ids in Db different response API")

    #Add a CsvFileFormat
    #vsts633398

    #Add modify CsvFileFormat
    #vsts633399
    
    #/CsvFileFormat/{rowId}
    @pytest.mark.vsts633400
    def test_CsvFileFormat_Object(self):
        logger.debug(self.id())
        dbUtil = dbConnection()
        dbData = dbUtil.get_CsvFileFormat()
        i = random.randint(0,len(dbData)-1)
        rowId = dbData[i]['RowId']
        endpoints = Endpoints()
        res = endpoints.get_CsvFileFormat(rowId=rowId)
        logger.debug(res)
        self.assertEqual(res['rowId'], dbData[i]['RowId'], f"{self.id()}  #/CsvFileFormat, List of ids in Db different response API")

    #/CsvFileFormat/Id/{object id}    ?dataSourceProfileRowId=2&exactMatch=false&includeInactive=false
    @pytest.mark.vsts633402
    def test_CsvFileFormat_Object_Object(self):
        logger.debug(self.id())
        dbUtil = dbConnection()
        dbData = dbUtil.get_CsvFileFormat()
        i = random.randint(0,len(dbData)-1)
        id = dbData[i]['Id']
        dsProfileId = dbData[i]['FK_DataSourceProfile']
        reqParams = { 'dataSourceProfileRowId' : dsProfileId,
            'exactMatch' : 'false',
            'includeInactive' : 'false'
        }
        endpoints = Endpoints()
        res = endpoints.get_CsvFileFormat_IdDS(id= id, params=reqParams)
        logger.debug(res)
        self.assertEqual(res[0]['fK_DataSourceProfile'], dsProfileId, f"{self.id()}  #/CsvFileFormat/Id/object id, Data Source Id is different")
        self.assertEqual(res[0]['name'], id, f"{self.id()}  #/CsvFileFormat/Id/object id, Csv Format name is different is different")

    #/DataSourceProfile
    @pytest.mark.vsts633411
    def test_DataSourceProfile(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_DataSourceProfile()
        dbUtil = dbConnection()
        dbData = dbUtil.get_DataSourceProfile()
        dbNameLst = []
        for element in dbData:
            dbNameLst.append(element['DataSourceName'])
        resNameLst = []
        for element in res:
            resNameLst.append(element['dataSourceName'])
        self.assertListEqual(dbNameLst, resNameLst, f"{self.id()}  #/TagSourceProfile, List of Data Source Name in Db different response API")

    #/DataSourceProfile/GetAndIncludeInactive   ?includeInactive=false
    @pytest.mark.vsts633413
    def test_DataSourceProfile_GetAndIncludeInactive(self):
        logger.debug(self.id())
        reqParams = { "includeInactive" : "false"}
        endpoints = Endpoints()
        res = endpoints.get_DataSourceProfile_IncludeInactive(params= reqParams)
        dbUtil = dbConnection()
        dbData = dbUtil.get_DataSourceProfile()
        dbNameLst = []
        for element in dbData:
            dbNameLst.append(element['DataSourceName'])
        resNameLst = []
        for element in res:
            resNameLst.append(element['dataSourceName'])
        self.assertListEqual(dbNameLst, resNameLst, f"{self.id()}  #/TagSourceProfile, List of Data Source Name in Db different response API")

    #/DataSourceProfile/List
    @pytest.mark.vsts633414
    def test_DataSourceProfile_List(self):
        logger.debug(self.id())
        dsLst = [1, 2, 3, 4]
        reqBody = {
            "rowIds": dsLst,
            "includeInactive": False
            }
        logger.debug(reqBody)
        endpoints = Endpoints()
        res = endpoints.post_DataSourceProfile_List(body= reqBody)
        dbUtil = dbConnection()
        dbData = dbUtil.get_DataSourceProfile()
        dbNameLst = []
        for element in dbData:
            dbNameLst.append(element['DataSourceName'])
        resNameLst = []
        redRowIdLst = []
        for element in res:
            resNameLst.append(element['dataSourceName'])
            redRowIdLst.append(element['rowId'])
        self.assertListEqual(dsLst, redRowIdLst, f"{self.id()}  #/DataSourceProfile/List, List of Data Source RowID in response API should match with the request")
        self.assertLessEqual(resNameLst, dbNameLst, f"{self.id()}  #/DataSourceProfile/List, List of Data Source Name in Db different response API")

    #vsts633446 Delete CsvFileFormat
    #vsts633459 add a Data Source
    #vsts633460 PUT

    #/DataSourceProfile/providers
    @pytest.mark.vsts688419
    def test_DataSourceProfile_Provider(self):
        logger.debug(self.id())
        endpoints = Endpoints()
        res = endpoints.get_DataSourceProfile_Provider()
        jsonUtil = JsonUtility('TSD_DirectoryService')
        resExp = jsonUtil.read_Json('DataSourceProfile_Provider_res_get.json')
        self.assertEqual(res, resExp, f"{self.id()}  #/DataSourceProfile/providers, Response different Json")

    #vsts688420 add Data Source list

    #/DataSourceProfile/{Data source id}/byId
    @pytest.mark.vsts688421
    def test_DataSourceProfile_ObjectID(self):
        logger.debug(self.id())
        dbUtil = dbConnection()
        dbData = dbUtil.get_DataSourceProfile()
        i = random.randint(0,len(dbData)-1)
        rowId = dbData[i]['RowId']
        endpoints = Endpoints()
        res = endpoints.get_DataSourceProfile_ObjectID(id=rowId)
        self.assertEqual(res['rowId'], dbData[i]['RowId'], f"{self.id()}  #/DataSourceProfile/Data source id/byId, Row id in Db different response API")
        self.assertEqual(res['dataSourceName'], dbData[i]['DataSourceName'], f"{self.id()}  #/DataSourceProfile/Data source id/byId, Name in Db different response API")

    #/DataSourceProfile/{id}/likeId       ?exactMatch=true&includeInactive=true
    @pytest.mark.vsts688422
    def test_DataSourceProfile_likeID(self):
        logger.debug(self.id())
        dbUtil = dbConnection()
        dbData = dbUtil.get_DataSourceProfile()
        i = random.randint(0,len(dbData)-1)
        id = dbData[i]['DataSourceName']
        reqParams = { "exactMatch" : True,
            "includeInactive" : True
        }
        endpoints = Endpoints()
        res = endpoints.get_DataSourceProfile_likeID(id=id, params=reqParams)
        self.assertEqual(res[0]['rowId'], dbData[i]['RowId'], f"{self.id()}  #/DataSourceProfile/Data source id/byId, Row id in Db different response API")
        self.assertEqual(res[0]['dataSourceName'], dbData[i]['DataSourceName'], f"{self.id()}  #/DataSourceProfile/Data source id/byId, Name in Db different response API")

    #/DataSourceProfile/{name}/byName
    @pytest.mark.vsts688423
    def test_DataSourceProfile_byName(self):
        logger.debug(self.id())
        dbUtil = dbConnection()
        dbData = dbUtil.get_DataSourceProfile()
        i = random.randint(0,len(dbData)-1)
        name = dbData[i]['DataSourceName']
        endpoints = Endpoints()
        res = endpoints.get_DataSourceProfile_byName(name=name)
        self.assertEqual(res['rowId'], dbData[i]['RowId'], f"{self.id()}  #/DataSourceProfile/name/byName source id/byId, Row id in Db different response API")
        self.assertEqual(res['dataSourceName'], dbData[i]['DataSourceName'], f"{self.id()}  #/DataSourceProfile/name/byName source id/byId, Name in Db different response API")

    #vsts688426

    #vsts688428

    #/DataSourceProfile/infoByTagName
    @pytest.mark.vsts688429
    def test_infoByTagName(self):
        logger.debug(self.id())
        dbUtil = dbConnection()
        dbData = dbUtil.get_TagReference()
        randomlist = random.sample(range(0, len(dbData)), len(dbData)//20+1)
        dsName = []
        dsrowId = []
        for i in randomlist:
            dsName.append(dbData[i]['Id'])
            dsrowId.append(dbData[i]['RowId'])
        endpoints = Endpoints()
        res = endpoints.post_infoByTagName(dsName)
        resName = []
        resRowId = []
        for element in res:
            for tag in element['tagNames']:
                resName.append(tag['tagName'])
                resRowId.append(tag['tagId'])
        resName.sort()
        dsName.sort()
        dsrowId.sort()
        resRowId.sort()
        self.assertListEqual(dsName, resName, f"{self.id()}  #/DataSourceProfile/infoByTagName, Name in Db different response API")
        self.assertListEqual(dsrowId, resRowId, f"{self.id()}  #/DataSourceProfile/infoByTagName, Row ID in Db different response API")

    #vsts688456 add tag reference toa DS

    #vsts688457

    #/DataSourceProfile/{dataSourceName}/{tagNameFilter}
    @pytest.mark.vsts688457
    def test_DataSource_DSObject_TagName(self):
        logger.debug(self.id())
        dbUtil = dbConnection()
        dbDataTagDs = dbUtil.get_TagReference_Join_DataSource()
        i = random.randint(0,len(dbDataTagDs)-1)
        data = dbDataTagDs[i]
        endpoints = Endpoints()
        res = endpoints.get_DataSourceProfile_dsName_tagName(data['DataSourceName'], data['Id'])
        self.assertEqual(res[0]['tagId'], data['Tag Id'], f"{self.id()}  #/DataSourceProfile/dataSourceName/tagNameFilter, Tag Id in Db different response API")
        self.assertEqual(res[0]['tagName'], data['Id'], f"{self.id()}  #/DataSourceProfile/dataSourceName/tagNameFilter, Tag Name in Db different response API")

    #/TagReference/{rowId}
    @pytest.mark.vsts688461
    def test_TagReference_RowId(self):
        logger.debug(self.id())
        dbUtil = dbConnection()
        dbData = dbUtil.get_TagReference_Join_DataSource()
        i = random.randint(0,len(dbData)-1)
        rowId = dbData[i]['Tag Id']
        endpoint = Endpoints()
        res = endpoint.get_TagReference_RowId(rowId = rowId)
        self.assertEqual(res['rowId'], dbData[i]['Tag Id'], f"{self.id()}  #/DataSourceProfile/dataSourceName/tagNameFilter, Tag Id in Db different response API")
        self.assertEqual(res['dataSourceProfileName'], dbData[i]['DataSourceName'], f"{self.id()}  #/DataSourceProfile/dataSourceName/tagNameFilter, Data Sporce Name in Db different response API")

