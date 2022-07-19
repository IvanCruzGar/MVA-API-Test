from dataclasses import replace
import requests
import os
from ssqaapitest.src.configs.hosts_config import API_HOSTS
import json
import logging as logger
from requests_ntlm import HttpNtlmAuth
import socket
from ssqaapitest.src.utilities.credentialsUtility import CredentialsUtility
import pdb


class RequestsUtility(object):

    def __init__(self, bearerToken = None, accessToken = None):
        # list_env = ["API_A", "API_B", "API_C"]
        # for envi in list_env:
        # if os.environ.get(envi) is not None:
        # self.env = os.environ.get(envi)
        # break
        # else:

        # print(f"El ambiente: {os.environ.get(envi)}")
        self.env = os.environ.get('API_A', 'API_B') or os.environ.get('API_C')
        self.base_url = API_HOSTS['MVAAut']
        self.bearerToken = bearerToken
        self.accessToken = accessToken

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad Status code." \
                                                              f"Expected {self.expected_status_code}, " \
                                                              f"Actual status code: {self.status_code}," \
                                                              f"URL:{self.url}, Response Json: {self.rs_json} "

    def post(self, endpoint, payload=None, params=None, headers=None, expected_status_code=200, resEmpty=False):
        # if not headers:
        #     headers = {"Content-Type": "application/json"}

        if self.bearerToken:
            headers['Authorization'] = 'Bearer ' + self.bearerToken

        self.url = self.base_url + endpoint
        
        if type(payload) == dict:
            payload = json.dumps(payload)
        else:
            payload = str(payload)
            payload = payload.replace('\'', '"')
        
        
        rs_api = requests.post(url=self.url, data=payload, params=params, headers=headers, verify=False)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        
        
        self.rs_json = rs_api.json() if (resEmpty == False) else {}
        self.assert_status_code()
     

        #logger.debug(f"POST API response: {self.status_code}")
        #logger.debug(f"POST API response: {self.rs_json}")

        return self.rs_json

    def get(self, endpoint, payload=None, params=None, headers=None, expected_status_code=200, resEmpty=False):
        # if not headers:
        #     headers = {"Content-Type": "application/json"}

        if self.bearerToken:
            headers['Authorization'] = 'Bearer ' + self.bearerToken
        
        if self.accessToken:
            headers = {'AccessToken': self.accessToken}
        
        self.url = self.base_url + endpoint
        if type(payload) == dict:
            payload = json.dumps(payload)
        else:
            payload = str(payload)
      
        rs_api = requests.get(url=self.url, data=payload, params=params, headers=headers, verify=False)
        logger.debug(rs_api.headers)
        logger.debug(rs_api)
        
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        
        self.rs_json = rs_api.json() if (resEmpty == False) else {}
        self.assert_status_code()
        

        #logger.debug(f"API GET response: {self.rs_json}")
        return self.rs_json
