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

class FeeuploadfilesFilterBody(object):
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
        'end_date': 'datetime',
        'num_files': 'int',
        'num_custodians': 'int',
        'num_accounts': 'int',
        'num_households': 'int',
        'total_annual_debit': 'float',
        'total_period_debit': 'float'
    }

    attribute_map = {
        'id': 'id',
        'firm_id': 'firm_id',
        'end_date': 'end_date',
        'num_files': 'num_files',
        'num_custodians': 'num_custodians',
        'num_accounts': 'num_accounts',
        'num_households': 'num_households',
        'total_annual_debit': 'total_annual_debit',
        'total_period_debit': 'total_period_debit'
    }

    def __init__(self, id=None, firm_id=None, end_date=None, num_files=None, num_custodians=None, num_accounts=None, num_households=None, total_annual_debit=None, total_period_debit=None):  # noqa: E501
        """FeeuploadfilesFilterBody - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._firm_id = None
        self._end_date = None
        self._num_files = None
        self._num_custodians = None
        self._num_accounts = None
        self._num_households = None
        self._total_annual_debit = None
        self._total_period_debit = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if firm_id is not None:
            self.firm_id = firm_id
        if end_date is not None:
            self.end_date = end_date
        if num_files is not None:
            self.num_files = num_files
        if num_custodians is not None:
            self.num_custodians = num_custodians
        if num_accounts is not None:
            self.num_accounts = num_accounts
        if num_households is not None:
            self.num_households = num_households
        if total_annual_debit is not None:
            self.total_annual_debit = total_annual_debit
        if total_period_debit is not None:
            self.total_period_debit = total_period_debit

    @property
    def id(self):
        """Gets the id of this FeeuploadfilesFilterBody.  # noqa: E501

        The unique resource ID for this Fee Upload File  # noqa: E501

        :return: The id of this FeeuploadfilesFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeeuploadfilesFilterBody.

        The unique resource ID for this Fee Upload File  # noqa: E501

        :param id: The id of this FeeuploadfilesFilterBody.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def firm_id(self):
        """Gets the firm_id of this FeeuploadfilesFilterBody.  # noqa: E501

        The firm ID of the managing firm  # noqa: E501

        :return: The firm_id of this FeeuploadfilesFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._firm_id

    @firm_id.setter
    def firm_id(self, firm_id):
        """Sets the firm_id of this FeeuploadfilesFilterBody.

        The firm ID of the managing firm  # noqa: E501

        :param firm_id: The firm_id of this FeeuploadfilesFilterBody.  # noqa: E501
        :type: int
        """

        self._firm_id = firm_id

    @property
    def end_date(self):
        """Gets the end_date of this FeeuploadfilesFilterBody.  # noqa: E501

        The date that this Fee Upload File ends  # noqa: E501

        :return: The end_date of this FeeuploadfilesFilterBody.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this FeeuploadfilesFilterBody.

        The date that this Fee Upload File ends  # noqa: E501

        :param end_date: The end_date of this FeeuploadfilesFilterBody.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def num_files(self):
        """Gets the num_files of this FeeuploadfilesFilterBody.  # noqa: E501

        The number of files for this Fee Upload File  # noqa: E501

        :return: The num_files of this FeeuploadfilesFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._num_files

    @num_files.setter
    def num_files(self, num_files):
        """Sets the num_files of this FeeuploadfilesFilterBody.

        The number of files for this Fee Upload File  # noqa: E501

        :param num_files: The num_files of this FeeuploadfilesFilterBody.  # noqa: E501
        :type: int
        """

        self._num_files = num_files

    @property
    def num_custodians(self):
        """Gets the num_custodians of this FeeuploadfilesFilterBody.  # noqa: E501

        The number of custodians for this Fee Upload File  # noqa: E501

        :return: The num_custodians of this FeeuploadfilesFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._num_custodians

    @num_custodians.setter
    def num_custodians(self, num_custodians):
        """Sets the num_custodians of this FeeuploadfilesFilterBody.

        The number of custodians for this Fee Upload File  # noqa: E501

        :param num_custodians: The num_custodians of this FeeuploadfilesFilterBody.  # noqa: E501
        :type: int
        """

        self._num_custodians = num_custodians

    @property
    def num_accounts(self):
        """Gets the num_accounts of this FeeuploadfilesFilterBody.  # noqa: E501

        The number of accounts for this Fee Upload File  # noqa: E501

        :return: The num_accounts of this FeeuploadfilesFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._num_accounts

    @num_accounts.setter
    def num_accounts(self, num_accounts):
        """Sets the num_accounts of this FeeuploadfilesFilterBody.

        The number of accounts for this Fee Upload File  # noqa: E501

        :param num_accounts: The num_accounts of this FeeuploadfilesFilterBody.  # noqa: E501
        :type: int
        """

        self._num_accounts = num_accounts

    @property
    def num_households(self):
        """Gets the num_households of this FeeuploadfilesFilterBody.  # noqa: E501

        The number of households for this Fee Upload File  # noqa: E501

        :return: The num_households of this FeeuploadfilesFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._num_households

    @num_households.setter
    def num_households(self, num_households):
        """Sets the num_households of this FeeuploadfilesFilterBody.

        The number of households for this Fee Upload File  # noqa: E501

        :param num_households: The num_households of this FeeuploadfilesFilterBody.  # noqa: E501
        :type: int
        """

        self._num_households = num_households

    @property
    def total_annual_debit(self):
        """Gets the total_annual_debit of this FeeuploadfilesFilterBody.  # noqa: E501

        The total annual debit for this Fee Upload File  # noqa: E501

        :return: The total_annual_debit of this FeeuploadfilesFilterBody.  # noqa: E501
        :rtype: float
        """
        return self._total_annual_debit

    @total_annual_debit.setter
    def total_annual_debit(self, total_annual_debit):
        """Sets the total_annual_debit of this FeeuploadfilesFilterBody.

        The total annual debit for this Fee Upload File  # noqa: E501

        :param total_annual_debit: The total_annual_debit of this FeeuploadfilesFilterBody.  # noqa: E501
        :type: float
        """

        self._total_annual_debit = total_annual_debit

    @property
    def total_period_debit(self):
        """Gets the total_period_debit of this FeeuploadfilesFilterBody.  # noqa: E501

        The total period debit for this Fee Upload File  # noqa: E501

        :return: The total_period_debit of this FeeuploadfilesFilterBody.  # noqa: E501
        :rtype: float
        """
        return self._total_period_debit

    @total_period_debit.setter
    def total_period_debit(self, total_period_debit):
        """Sets the total_period_debit of this FeeuploadfilesFilterBody.

        The total period debit for this Fee Upload File  # noqa: E501

        :param total_period_debit: The total_period_debit of this FeeuploadfilesFilterBody.  # noqa: E501
        :type: float
        """

        self._total_period_debit = total_period_debit

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
        if issubclass(FeeuploadfilesFilterBody, dict):
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
        if not isinstance(other, FeeuploadfilesFilterBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
