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

class InlineResponse20021(object):
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
        'download_link': 'str'
    }

    attribute_map = {
        'download_link': 'download_link'
    }

    def __init__(self, download_link=None):  # noqa: E501
        """InlineResponse20021 - a model defined in Swagger"""  # noqa: E501
        self._download_link = None
        self.discriminator = None
        if download_link is not None:
            self.download_link = download_link

    @property
    def download_link(self):
        """Gets the download_link of this InlineResponse20021.  # noqa: E501

        Download link for a fee upload file  # noqa: E501

        :return: The download_link of this InlineResponse20021.  # noqa: E501
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        """Sets the download_link of this InlineResponse20021.

        Download link for a fee upload file  # noqa: E501

        :param download_link: The download_link of this InlineResponse20021.  # noqa: E501
        :type: str
        """

        self._download_link = download_link

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
        if issubclass(InlineResponse20021, dict):
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
        if not isinstance(other, InlineResponse20021):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
