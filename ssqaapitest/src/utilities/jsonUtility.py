import json
import os

class JsonUtility(object):

    def __init__(self, service):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.join(self.cur_file_dir, '..', 'data', 'json_file', service)

    def read_Json(self, json_file=None):

        jPath = os.path.join(self.path, json_file)

        with open(jPath) as f:
            jsonFile = json.load(f)

        return jsonFile