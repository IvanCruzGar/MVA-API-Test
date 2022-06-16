from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
from ssqaapitest.src.utilities.jsonUtility import JsonUtility
import pdb
import logging as logger

#http://172.22.4.151:8080/Aspentech/APM/TSDDirectoryService/swagger/index.html
#Needs Autorization
class Endpoints(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.json_Utility = JsonUtility('TSD_ConsumerService')
        self.__bearerToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBsaWNhdGlvbiI6IkFzcGVuIE10ZWxsIiwiUGVyc2lzdGVuY2UiOiJQcmltYXJ5IiwidW5pcXVlX25hbWUiOiJBZG1pbiIsInByaW1hcnlzaWQiOiIyIiwicm9sZSI6IkFkbWluaXN0cmF0b3IiLCJuYmYiOjE2NTQ1MTk1NzYsImV4cCI6MTY1NDg3OTU3NiwiaWF0IjoxNjU0NTE5NTc2LCJpc3MiOiJBc3BlbnRlY2hNdGVsbCJ9.5rKGAuY-761b3YpceZoomgMbmBSCHj_rFCFbZZswkCM'
        self.requests_utility = RequestsUtility(bearerToken= self.__bearerToken)
        self.serviceApi = "TSDDirectoryService/Api"


    #vsts633167
    #vsts633400
    def get_CsvFileFormat(self, rowId = ""):
        api_res = self.requests_utility.get(f"{self.serviceApi}/CsvFileFormat/{rowId}", expected_status_code=200)
        return api_res

    #vsts633402
    def get_CsvFileFormat_IdDS(self, id = "", params = None):
        api_res = self.requests_utility.get(f"{self.serviceApi}/CsvFileFormat/Id/{id}", params=params ,expected_status_code=200)
        return api_res
    
    #vsts633402
    def get_DataSourceProfile(self):
        api_res = self.requests_utility.get(f"{self.serviceApi}/DataSourceProfile", expected_status_code=200)
        return api_res

    #vsts633413
    def get_DataSourceProfile_IncludeInactive(self, params):
        api_res = self.requests_utility.get(f"{self.serviceApi}/DataSourceProfile/GetAndIncludeInactive", params=params ,expected_status_code=200)
        return api_res

    #vsts633414
    def post_DataSourceProfile_List(self, body):
        api_res = self.requests_utility.post(f"{self.serviceApi}/DataSourceProfile/List", payload=body, expected_status_code=200)
        return api_res

    #vsts688419
    def get_DataSourceProfile_Provider(self):
        api_res = self.requests_utility.get(f"{self.serviceApi}/DataSourceProfile/Providers", expected_status_code=200)
        return api_res

    #vsts688421
    def get_DataSourceProfile_ObjectID(self, id = ''):
        api_res = self.requests_utility.get(f"{self.serviceApi}/DataSourceProfile/{id}/byId", expected_status_code=200)
        return api_res


    #vsts688422
    def get_DataSourceProfile_likeID(self, id = '', params = None):
        api_res = self.requests_utility.get(f"{self.serviceApi}/DataSourceProfile/{id}/likeId", params=params, expected_status_code=200)
        return api_res

    #vsts688423
    def get_DataSourceProfile_byName(self, name = ''):
        api_res = self.requests_utility.get(f"{self.serviceApi}/DataSourceProfile/{name}/byName", expected_status_code=200)
        return api_res

    #vsts688429
    def post_infoByTagName(self, body = None):
        api_res = self.requests_utility.post(f"{self.serviceApi}/DataSourceProfile/infoByTagName", payload=body ,expected_status_code=200)
        return api_res

    #vsts688457
    def get_DataSourceProfile_dsName_tagName(self, dsName = '', tagName = ''):
        api_res = self.requests_utility.get(f"{self.serviceApi}/DataSourceProfile/{dsName}/{tagName}", expected_status_code=200)
        return api_res

    #vsts688461
    def get_TagReference_RowId(self, rowId = ''):
        api_res = self.requests_utility.get(f"{self.serviceApi}/TagReference/{rowId}", expected_status_code=200)
        return api_res
