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

class AumFilterBody(object):
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
        'id': 'int',
        'firm_id': 'int',
        'as_of_date': 'datetime',
        'frequency': 'str',
        'total': 'float'
    }

    attribute_map = {
        'id': 'id',
        'firm_id': 'firm_id',
        'as_of_date': 'as_of_date',
        'frequency': 'frequency',
        'total': 'total'
    }

    def __init__(self, id=None, firm_id=None, as_of_date=None, frequency=None, total=None):  # noqa: E501
        """AumFilterBody - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._firm_id = None
        self._as_of_date = None
        self._frequency = None
        self._total = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if firm_id is not None:
            self.firm_id = firm_id
        if as_of_date is not None:
            self.as_of_date = as_of_date
        if frequency is not None:
            self.frequency = frequency
        if total is not None:
            self.total = total

    @property
    def id(self):
        """Gets the id of this AumFilterBody.  # noqa: E501

        The unique resource ID for this AUM  # noqa: E501

        :return: The id of this AumFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AumFilterBody.

        The unique resource ID for this AUM  # noqa: E501

        :param id: The id of this AumFilterBody.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def firm_id(self):
        """Gets the firm_id of this AumFilterBody.  # noqa: E501

        The firm ID of the managing firm  # noqa: E501

        :return: The firm_id of this AumFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._firm_id

    @firm_id.setter
    def firm_id(self, firm_id):
        """Sets the firm_id of this AumFilterBody.

        The firm ID of the managing firm  # noqa: E501

        :param firm_id: The firm_id of this AumFilterBody.  # noqa: E501
        :type: int
        """

        self._firm_id = firm_id

    @property
    def as_of_date(self):
        """Gets the as_of_date of this AumFilterBody.  # noqa: E501

        The current date of the AUM  # noqa: E501

        :return: The as_of_date of this AumFilterBody.  # noqa: E501
        :rtype: datetime
        """
        return self._as_of_date

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this AumFilterBody.

        The current date of the AUM  # noqa: E501

        :param as_of_date: The as_of_date of this AumFilterBody.  # noqa: E501
        :type: datetime
        """

        self._as_of_date = as_of_date

    @property
    def frequency(self):
        """Gets the frequency of this AumFilterBody.  # noqa: E501

        See Frequency Codes  # noqa: E501

        :return: The frequency of this AumFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this AumFilterBody.

        See Frequency Codes  # noqa: E501

        :param frequency: The frequency of this AumFilterBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["D = Daily", "W = Weekly", "M = Monthly", "Q = Quarterly", "Y = Yearly"]  # noqa: E501
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

    @property
    def total(self):
        """Gets the total of this AumFilterBody.  # noqa: E501

        The total assets under management for the AUM  # noqa: E501

        :return: The total of this AumFilterBody.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this AumFilterBody.

        The total assets under management for the AUM  # noqa: E501

        :param total: The total of this AumFilterBody.  # noqa: E501
        :type: float
        """

        self._total = total

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
        if issubclass(AumFilterBody, dict):
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
        if not isinstance(other, AumFilterBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
