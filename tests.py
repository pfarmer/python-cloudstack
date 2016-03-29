# -*- coding: utf-8 -*-
import unittest
import os

from cloudstack import CloudStack
from cloudstack.utils import listvms
from requests.packages import urllib3
urllib3.disable_warnings()


cs = CloudStack(
    api_url=os.environ['API_URL'],
    secret=os.environ['API_SECRET'],
    apiKey=os.environ['API_KEY']
)


class CloudStackAPIMethods(unittest.TestCase):
    def test_listZones(self):
        resp = cs.listZones({})
        self.assertEqual(200, resp.status_code)

    def test_listVolumes(self):
        resp = cs.listVolumes({})
        self.assertEqual(200, resp.status_code)

    def test_listVirtualMachines(self):
        resp = cs.listVirtualMachines({})
        self.assertEqual(200, resp.status_code)

    def test_listNetworks(self):
        resp = cs.listNetworks({})
        self.assertEqual(200, resp.status_code)


class CloudStackUtilsMethods(unittest.TestCase):
    def test_listvms(self):
        resp = listvms(cs)
        self.assertEqual(True, isinstance(resp, list))


if __name__ == '__main__':
    unittest.main()
