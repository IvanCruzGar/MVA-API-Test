from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
from ssqaapitest.src.utilities.jsonUtility import JsonUtility
import pdb
import logging as logger

#http://172.22.4.151:8080/Aspentech/APM/TSDDataAcquisitionService/swagger/index.html
#Needs Autorization
class Endpoints(object):

    def __init__(self):
        self.__bearerToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBsaWNhdGlvbiI6IkFzcGVuIE10ZWxsIiwiUGVyc2lzdGVuY2UiOiJQcmltYXJ5IiwidW5pcXVlX25hbWUiOiJBZG1pbiIsInByaW1hcnlzaWQiOiIyIiwicm9sZSI6IkFkbWluaXN0cmF0b3IiLCJuYmYiOjE2NTQ1MTk1NzYsImV4cCI6MTY1NDg3OTU3NiwiaWF0IjoxNjU0NTE5NTc2LCJpc3MiOiJBc3BlbnRlY2hNdGVsbCJ9.5rKGAuY-761b3YpceZoomgMbmBSCHj_rFCFbZZswkCM'
        self.requests_utility = RequestsUtility(bearerToken= self.__bearerToken)
        self.json_Utility = JsonUtility('TSD_DataAcquisitionService')
        self.serviceApi = "TSDDataAcquisitionService"

    #vsts633167
    def get_CycleBuilder(self, status):
        api_res = self.requests_utility.get(f"{self.serviceApi}/CycleBuilder", expected_status_code=status)
        return api_res

    #vsts633169
    def post_CycleBuilder(self):
        reqBody = self.json_Utility.read_Json('CycleBuilder_req_post.json')
        api_res = self.requests_utility.post(f"{self.serviceApi}/CycleBuilder", payload=reqBody, expected_status_code=200)
        return api_res

    #vsts633171
    def get_CycleBuilderAfter(self):
        api_res = self.requests_utility.get(f"{self.serviceApi}/CycleBuilder/after/2019-11-10", expected_status_code=200)
        return api_res


    #vsts633174
    def get_CycleBuilder_Object(self):
        api_res = self.requests_utility.get(f"{self.serviceApi}/CycleBuilder/1", expected_status_code=200)
        return api_res

    #vsts633177
    def get_GranularityTypes(self):
        api_res = self.requests_utility.get(f"{self.serviceApi}/GranularityTypes", expected_status_code=200)
        return api_res

    #vsts633178
    def get_GranularityTypes_Object(self):
        api_res = self.requests_utility.get(f"{self.serviceApi}/GranularityTypes/10", expected_status_code=200)
        return api_res

    #vsts633182
    def get_Submision_Object(self):
        api_res = self.requests_utility.get(f"{self.serviceApi}/Submissions/1/2019-11-10/2021-11-10", expected_status_code=200)
        return api_res

    #vsts633183
    def get_Submision(self):
        api_res = self.requests_utility.get(f"{self.serviceApi}/Submissions", expected_status_code=200)
        return api_res

    #vsts633184
    def get_SubmisionDate_Object(self):
        api_res = self.requests_utility.get(f"{self.serviceApi}/Submissions/date/2019-11-10/2021-11-10", expected_status_code=200)
        return api_res
