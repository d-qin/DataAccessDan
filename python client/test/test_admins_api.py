# coding: utf-8

"""
    Simple Inventory API

    This is a simple API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: you@your-company.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.admins_api import AdminsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAdminsApi(unittest.TestCase):
    """AdminsApi unit test stubs"""

    def setUp(self):
        self.api = AdminsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_inventory(self):
        """Test case for add_inventory

        adds an inventory item  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
