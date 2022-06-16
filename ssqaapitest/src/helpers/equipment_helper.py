from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import pdb
import logging as logger


class Endpoints_equipment(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_equipment(self):
        return self.requests_utility.get(f"EquipmentSets")

    def get_tag_references(self, tag_id):
        return self.requests_utility.get(f"EquipmentSets/{tag_id}/AssetsWithTagReferences")
