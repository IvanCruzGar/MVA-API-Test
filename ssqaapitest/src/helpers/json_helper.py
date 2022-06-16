import json
import os


class OrderHelper(object):

    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))

    def create_order(self, additional_args=None, json_file=None):

        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'json_file', json_file)

        with open(payload_template) as f:
            payload = json.load(f)
        # if the user need to add or modiky the JSON
        if additional_args:
            #assert isinstance(additional_args, list), f"The JSON has an error"
            return payload.update(additional_args)
        if additional_args:
            #assert isinstance(additional_args, list), f"The JSON has an error"
            return payload.update(additional_args)
        else:
            return payload



