import pytest
import unittest
import pdb
from ssqaapitest.src.dao.queries_equipment_set import Apm_Equipment
from ssqaapitest.src.helpers.TSD_ConsumerService.request import Endpoints
from ssqaapitest.lof.keys_equipment import Values_equipment
from ssqaapitest.src.helpers.json_helper import OrderHelper
import logging as logger

from ssqaapitest.src.utilities.jsonUtility import JsonUtility


@pytest.mark.tsd_test
class TestListElements(unittest.TestCase):

    @pytest.mark.vstsTest
    def test_tsd_test(self):

        end = Endpoints()
        resp = end.get_test()
        logger.debug('resp')

        jsonR = JsonUtility('TSD_ConsumerService')
        logger.debug(jsonR.read_Json('Test.json')['test'])
        self.assertEqual(resp, resp)

