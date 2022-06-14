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
from swagger_client.api.benchmarks_api import BenchmarksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBenchmarksApi(unittest.TestCase):
    """BenchmarksApi unit test stubs"""

    def setUp(self):
        self.api = BenchmarksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_benchmarks(self):
        """Test case for create_benchmarks

        Create a Benchmark  # noqa: E501
        """
        pass

    def test_create_many_benchmarks(self):
        """Test case for create_many_benchmarks

        Create Benchmarks  # noqa: E501
        """
        pass

    def test_detele_benchmark(self):
        """Test case for detele_benchmark

        Delete a Benchmark  # noqa: E501
        """
        pass

    def test_detele_many_benchmarks(self):
        """Test case for detele_many_benchmarks

        Delete many Benchmarks  # noqa: E501
        """
        pass

    def test_filter_benchmarks(self):
        """Test case for filter_benchmarks

        Filter all Benchmarks  # noqa: E501
        """
        pass

    def test_get_benchmark(self):
        """Test case for get_benchmark

        Retrieve a Benchmark  # noqa: E501
        """
        pass

    def test_get_benchmarks(self):
        """Test case for get_benchmarks

        List all Benchmarks  # noqa: E501
        """
        pass

    def test_update_benchmark(self):
        """Test case for update_benchmark

        Update a Benchmark  # noqa: E501
        """
        pass

    def test_update_benchmarks(self):
        """Test case for update_benchmarks

        Bulk Update Benchmarks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
