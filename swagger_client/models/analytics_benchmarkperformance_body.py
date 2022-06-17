# coding: utf-8

"""
    Atlas API

    RESTful API for controlling and interacting with Atlas data  # noqa: E501

    OpenAPI spec version: 2.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnalyticsBenchmarkperformanceBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'benchmarks_ids': 'list[int]',
        'start_date': 'date',
        'end_date': 'date'
    }

    attribute_map = {
        'benchmarks_ids': 'benchmarks_ids',
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, benchmarks_ids=None, start_date=None, end_date=None):  # noqa: E501
        """AnalyticsBenchmarkperformanceBody - a model defined in Swagger"""  # noqa: E501
        self._benchmarks_ids = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None
        if benchmarks_ids is not None:
            self.benchmarks_ids = benchmarks_ids
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def benchmarks_ids(self):
        """Gets the benchmarks_ids of this AnalyticsBenchmarkperformanceBody.  # noqa: E501

        List of benchmakr Ids  # noqa: E501

        :return: The benchmarks_ids of this AnalyticsBenchmarkperformanceBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._benchmarks_ids

    @benchmarks_ids.setter
    def benchmarks_ids(self, benchmarks_ids):
        """Sets the benchmarks_ids of this AnalyticsBenchmarkperformanceBody.

        List of benchmakr Ids  # noqa: E501

        :param benchmarks_ids: The benchmarks_ids of this AnalyticsBenchmarkperformanceBody.  # noqa: E501
        :type: list[int]
        """

        self._benchmarks_ids = benchmarks_ids

    @property
    def start_date(self):
        """Gets the start_date of this AnalyticsBenchmarkperformanceBody.  # noqa: E501

        Start date for the household performance calcuation  # noqa: E501

        :return: The start_date of this AnalyticsBenchmarkperformanceBody.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this AnalyticsBenchmarkperformanceBody.

        Start date for the household performance calcuation  # noqa: E501

        :param start_date: The start_date of this AnalyticsBenchmarkperformanceBody.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this AnalyticsBenchmarkperformanceBody.  # noqa: E501

        End date for the household performance calcuation  # noqa: E501

        :return: The end_date of this AnalyticsBenchmarkperformanceBody.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this AnalyticsBenchmarkperformanceBody.

        End date for the household performance calcuation  # noqa: E501

        :param end_date: The end_date of this AnalyticsBenchmarkperformanceBody.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AnalyticsBenchmarkperformanceBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnalyticsBenchmarkperformanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other