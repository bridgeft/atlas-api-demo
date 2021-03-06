# coding: utf-8

"""
    Atlas API

    RESTful API for controlling and interacting with Atlas data  # noqa: E501

    OpenAPI spec version: 2.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.api_keys_api import APIKeysApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAPIKeysApi(unittest.TestCase):
    """APIKeysApi unit test stubs"""

    def setUp(self):
        self.api = APIKeysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_api(self):
        """Test case for create_api

        Create an API Key  # noqa: E501
        """
        pass

    def test_detele_api(self):
        """Test case for detele_api

        Delete an API Key  # noqa: E501
        """
        pass

    def test_get_api(self):
        """Test case for get_api

        Retrieve an API key  # noqa: E501
        """
        pass

    def test_get_apis(self):
        """Test case for get_apis

        Retrieve all API keys  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
