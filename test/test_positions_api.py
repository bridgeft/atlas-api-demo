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
from swagger_client.api.positions_api import PositionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPositionsApi(unittest.TestCase):
    """PositionsApi unit test stubs"""

    def setUp(self):
        self.api = PositionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_filter_positions(self):
        """Test case for filter_positions

        Filter all Positions records  # noqa: E501
        """
        pass

    def test_get_position(self):
        """Test case for get_position

        Retrieve a Position record  # noqa: E501
        """
        pass

    def test_get_positions(self):
        """Test case for get_positions

        List all Positions records  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
