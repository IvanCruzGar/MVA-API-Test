from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
from ssqaapitest.src.utilities.jsonUtility import JsonUtility
import pdb
import logging as logger

#http://172.22.4.151:8080/Aspentech/APM/TSDConsumerService/swagger/index.html
class Endpoints(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.json_Utility = JsonUtility('TSD_ConsumerService')
        self.serviceApi = "TSDconsumerservice/api"

    def get_test(self):
        api_res = self.requests_utility.get(f"{self.serviceApi}/PDR/GetDataSet", expected_status_code=204)
        logger.debug(f"get test {api_res}")
        return api_res

    #vsts632117
    def post_QueryTsd(self):
        reqBody = self.json_Utility.read_Json('QueryTsd_req_post.json')
        api_res = self.requests_utility.post(f"{self.serviceApi}/TSDRetrieval/QueryTsd", payload=reqBody, expected_status_code=200)
        return api_res

    #vsts632118  
    def post_GetTsd(self):
        reqBody = self.json_Utility.read_Json('GetTds_req_post.json')
        api_res = self.requests_utility.post(f"{self.serviceApi}/TSDRetrieval/GetTsd", payload=reqBody, expected_status_code=200)
        return api_res

    #vsts633099
    def post_GetAvailableGranularitiesForTag(self):
        reqBody = self.json_Utility.read_Json('GetAvailableGranularitiesForTag_req_post.json')
        api_res = self.requests_utility.post(f"{self.serviceApi}/TSDRetrieval/GetAvailableGranularitiesForTag", payload=reqBody, expected_status_code=200)
        return api_res

    #vsts633108 
    def get_GetGranularityListing(self):
        api_res = self.requests_utility.get(f"{self.serviceApi}/TSDRetrieval/GetGranularityListing", expected_status_code=200)
        return api_res

    #vsts633112
    def post_GetTrainingDataSet(self):
        reqBody = self.json_Utility.read_Json('GetAvailableGranularitiesForTag_req_post.json')
        api_res = self.requests_utility.post(f"{self.serviceApi}/Custom/GetTrainingDataSet", expected_status_code=200)
        pass

    #vsts633135
    def post_GetRangeOfExistingData(self):
        reqBody = self.json_Utility.read_Json('GetRangeOfExistingData_req_post.json')
        reqParams = {'granularityId' : 21}
        api_res = self.requests_utility.post(f"{self.serviceApi}/TSDRetrieval/GetRangeOfExistingData", params=reqParams, payload=reqBody, expected_status_code=200)
        return api_res

    #vsts633140
    #/PDR/GetDataSet
    def get_GetDataSet(self, reqParams, status):
        api_res = self.requests_utility.get(f"{self.serviceApi}/PDR/GetDataSet", params=reqParams, expected_status_code=status)
        return api_res

    #vsts633142
    def get_GetDataSetById(self, reqParams):
        api_res = self.requests_utility.get(f"{self.serviceApi}/PDR/GetDataSetById", params=reqParams, expected_status_code=200)
        return api_res

    #vsts6633152
    #/PDR/SaveDataSet
    def post_SaveDataSet(self):
        pass
