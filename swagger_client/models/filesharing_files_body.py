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

class FilesharingFilesBody(object):
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
        'key_hashvalue': 'str',
        'firm_id': 'int',
        'uploaded_by_user_id': 'int',
        'sharing_scope': 'str',
        'shared_household_id': 'int',
        'size_bytes': 'int',
        'filename': 'str',
        'file_type': 'str',
        'content_type': 'str'
    }

    attribute_map = {
        'key_hashvalue': 'key_hashvalue',
        'firm_id': 'firm_id',
        'uploaded_by_user_id': 'uploaded_by_user_id',
        'sharing_scope': 'sharing_scope',
        'shared_household_id': 'shared_household_id',
        'size_bytes': 'size_bytes',
        'filename': 'filename',
        'file_type': 'file_type',
        'content_type': 'content_type'
    }

    def __init__(self, key_hashvalue=None, firm_id=None, uploaded_by_user_id=None, sharing_scope=None, shared_household_id=None, size_bytes=None, filename=None, file_type=None, content_type=None):  # noqa: E501
        """FilesharingFilesBody - a model defined in Swagger"""  # noqa: E501
        self._key_hashvalue = None
        self._firm_id = None
        self._uploaded_by_user_id = None
        self._sharing_scope = None
        self._shared_household_id = None
        self._size_bytes = None
        self._filename = None
        self._file_type = None
        self._content_type = None
        self.discriminator = None
        if key_hashvalue is not None:
            self.key_hashvalue = key_hashvalue
        if firm_id is not None:
            self.firm_id = firm_id
        if uploaded_by_user_id is not None:
            self.uploaded_by_user_id = uploaded_by_user_id
        if sharing_scope is not None:
            self.sharing_scope = sharing_scope
        if shared_household_id is not None:
            self.shared_household_id = shared_household_id
        if size_bytes is not None:
            self.size_bytes = size_bytes
        if filename is not None:
            self.filename = filename
        if file_type is not None:
            self.file_type = file_type
        if content_type is not None:
            self.content_type = content_type

    @property
    def key_hashvalue(self):
        """Gets the key_hashvalue of this FilesharingFilesBody.  # noqa: E501

        Hashkey for this shared file  # noqa: E501

        :return: The key_hashvalue of this FilesharingFilesBody.  # noqa: E501
        :rtype: str
        """
        return self._key_hashvalue

    @key_hashvalue.setter
    def key_hashvalue(self, key_hashvalue):
        """Sets the key_hashvalue of this FilesharingFilesBody.

        Hashkey for this shared file  # noqa: E501

        :param key_hashvalue: The key_hashvalue of this FilesharingFilesBody.  # noqa: E501
        :type: str
        """

        self._key_hashvalue = key_hashvalue

    @property
    def firm_id(self):
        """Gets the firm_id of this FilesharingFilesBody.  # noqa: E501

        The firm id assigned to this Shared File  # noqa: E501

        :return: The firm_id of this FilesharingFilesBody.  # noqa: E501
        :rtype: int
        """
        return self._firm_id

    @firm_id.setter
    def firm_id(self, firm_id):
        """Sets the firm_id of this FilesharingFilesBody.

        The firm id assigned to this Shared File  # noqa: E501

        :param firm_id: The firm_id of this FilesharingFilesBody.  # noqa: E501
        :type: int
        """

        self._firm_id = firm_id

    @property
    def uploaded_by_user_id(self):
        """Gets the uploaded_by_user_id of this FilesharingFilesBody.  # noqa: E501

        The id of the User that created this Shared File  # noqa: E501

        :return: The uploaded_by_user_id of this FilesharingFilesBody.  # noqa: E501
        :rtype: int
        """
        return self._uploaded_by_user_id

    @uploaded_by_user_id.setter
    def uploaded_by_user_id(self, uploaded_by_user_id):
        """Sets the uploaded_by_user_id of this FilesharingFilesBody.

        The id of the User that created this Shared File  # noqa: E501

        :param uploaded_by_user_id: The uploaded_by_user_id of this FilesharingFilesBody.  # noqa: E501
        :type: int
        """

        self._uploaded_by_user_id = uploaded_by_user_id

    @property
    def sharing_scope(self):
        """Gets the sharing_scope of this FilesharingFilesBody.  # noqa: E501

        Determines whether the sharing of this file is firm-wide (a) or restricted to households (h). See Entity ID Prefixes.  # noqa: E501

        :return: The sharing_scope of this FilesharingFilesBody.  # noqa: E501
        :rtype: str
        """
        return self._sharing_scope

    @sharing_scope.setter
    def sharing_scope(self, sharing_scope):
        """Sets the sharing_scope of this FilesharingFilesBody.

        Determines whether the sharing of this file is firm-wide (a) or restricted to households (h). See Entity ID Prefixes.  # noqa: E501

        :param sharing_scope: The sharing_scope of this FilesharingFilesBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["a = firm-wide", "h = restricted to household"]  # noqa: E501
        if sharing_scope not in allowed_values:
            raise ValueError(
                "Invalid value for `sharing_scope` ({0}), must be one of {1}"  # noqa: E501
                .format(sharing_scope, allowed_values)
            )

        self._sharing_scope = sharing_scope

    @property
    def shared_household_id(self):
        """Gets the shared_household_id of this FilesharingFilesBody.  # noqa: E501

        Set when the file is sharing with the household scope  # noqa: E501

        :return: The shared_household_id of this FilesharingFilesBody.  # noqa: E501
        :rtype: int
        """
        return self._shared_household_id

    @shared_household_id.setter
    def shared_household_id(self, shared_household_id):
        """Sets the shared_household_id of this FilesharingFilesBody.

        Set when the file is sharing with the household scope  # noqa: E501

        :param shared_household_id: The shared_household_id of this FilesharingFilesBody.  # noqa: E501
        :type: int
        """

        self._shared_household_id = shared_household_id

    @property
    def size_bytes(self):
        """Gets the size_bytes of this FilesharingFilesBody.  # noqa: E501

        The size in bytes of this Shared File  # noqa: E501

        :return: The size_bytes of this FilesharingFilesBody.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this FilesharingFilesBody.

        The size in bytes of this Shared File  # noqa: E501

        :param size_bytes: The size_bytes of this FilesharingFilesBody.  # noqa: E501
        :type: int
        """

        self._size_bytes = size_bytes

    @property
    def filename(self):
        """Gets the filename of this FilesharingFilesBody.  # noqa: E501

        The S3 filename for this Shared File  # noqa: E501

        :return: The filename of this FilesharingFilesBody.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this FilesharingFilesBody.

        The S3 filename for this Shared File  # noqa: E501

        :param filename: The filename of this FilesharingFilesBody.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def file_type(self):
        """Gets the file_type of this FilesharingFilesBody.  # noqa: E501

        See Shared File Types  # noqa: E501

        :return: The file_type of this FilesharingFilesBody.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this FilesharingFilesBody.

        See Shared File Types  # noqa: E501

        :param file_type: The file_type of this FilesharingFilesBody.  # noqa: E501
        :type: str
        """

        self._file_type = file_type

    @property
    def content_type(self):
        """Gets the content_type of this FilesharingFilesBody.  # noqa: E501

        The content type for this Shared File  # noqa: E501

        :return: The content_type of this FilesharingFilesBody.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this FilesharingFilesBody.

        The content type for this Shared File  # noqa: E501

        :param content_type: The content_type of this FilesharingFilesBody.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

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
        if issubclass(FilesharingFilesBody, dict):
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
        if not isinstance(other, FilesharingFilesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
