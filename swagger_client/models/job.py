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

class Job(object):
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
        'job_type': 'str',
        'created_dt_utc': 'datetime',
        'last_updated_dt_utc': 'datetime',
        'queued_dt_utc': 'datetime',
        'started_dt_utc': 'datetime',
        'finished_dt_utc': 'datetime',
        'failed_dt_utc': 'datetime',
        'created_by_id': 'int',
        'is_finished': 'bool',
        'is_running': 'bool',
        'is_failed': 'bool',
        'is_revoked': 'bool',
        'num_steps': 'int',
        'current_step': 'int',
        'email_notification': 'datetime',
        'email_notification_dt_utc': 'datetime',
        'created_at_utc': 'datetime',
        'updated_at_utc': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'firm_id': 'firm_id',
        'job_type': 'job_type',
        'created_dt_utc': 'created_dt_utc',
        'last_updated_dt_utc': 'last_updated_dt_utc',
        'queued_dt_utc': 'queued_dt_utc',
        'started_dt_utc': 'started_dt_utc',
        'finished_dt_utc': 'finished_dt_utc',
        'failed_dt_utc': 'failed_dt_utc',
        'created_by_id': 'created_by_id',
        'is_finished': 'is_finished',
        'is_running': 'is_running',
        'is_failed': 'is_failed',
        'is_revoked': 'is_revoked',
        'num_steps': 'num_steps',
        'current_step': 'current_step',
        'email_notification': 'email_notification',
        'email_notification_dt_utc': 'email_notification_dt_utc',
        'created_at_utc': 'created_at_utc',
        'updated_at_utc': 'updated_at_utc'
    }

    def __init__(self, id=None, firm_id=None, job_type=None, created_dt_utc=None, last_updated_dt_utc=None, queued_dt_utc=None, started_dt_utc=None, finished_dt_utc=None, failed_dt_utc=None, created_by_id=None, is_finished=None, is_running=None, is_failed=None, is_revoked=None, num_steps=None, current_step=None, email_notification=None, email_notification_dt_utc=None, created_at_utc=None, updated_at_utc=None):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._firm_id = None
        self._job_type = None
        self._created_dt_utc = None
        self._last_updated_dt_utc = None
        self._queued_dt_utc = None
        self._started_dt_utc = None
        self._finished_dt_utc = None
        self._failed_dt_utc = None
        self._created_by_id = None
        self._is_finished = None
        self._is_running = None
        self._is_failed = None
        self._is_revoked = None
        self._num_steps = None
        self._current_step = None
        self._email_notification = None
        self._email_notification_dt_utc = None
        self._created_at_utc = None
        self._updated_at_utc = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if firm_id is not None:
            self.firm_id = firm_id
        if job_type is not None:
            self.job_type = job_type
        if created_dt_utc is not None:
            self.created_dt_utc = created_dt_utc
        if last_updated_dt_utc is not None:
            self.last_updated_dt_utc = last_updated_dt_utc
        if queued_dt_utc is not None:
            self.queued_dt_utc = queued_dt_utc
        if started_dt_utc is not None:
            self.started_dt_utc = started_dt_utc
        if finished_dt_utc is not None:
            self.finished_dt_utc = finished_dt_utc
        if failed_dt_utc is not None:
            self.failed_dt_utc = failed_dt_utc
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if is_finished is not None:
            self.is_finished = is_finished
        if is_running is not None:
            self.is_running = is_running
        if is_failed is not None:
            self.is_failed = is_failed
        if is_revoked is not None:
            self.is_revoked = is_revoked
        if num_steps is not None:
            self.num_steps = num_steps
        if current_step is not None:
            self.current_step = current_step
        if email_notification is not None:
            self.email_notification = email_notification
        if email_notification_dt_utc is not None:
            self.email_notification_dt_utc = email_notification_dt_utc
        if created_at_utc is not None:
            self.created_at_utc = created_at_utc
        if updated_at_utc is not None:
            self.updated_at_utc = updated_at_utc

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501

        Unique ID for this background job object  # noqa: E501

        :return: The id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.

        Unique ID for this background job object  # noqa: E501

        :param id: The id of this Job.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def firm_id(self):
        """Gets the firm_id of this Job.  # noqa: E501

        ID of the owning firm  # noqa: E501

        :return: The firm_id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._firm_id

    @firm_id.setter
    def firm_id(self, firm_id):
        """Sets the firm_id of this Job.

        ID of the owning firm  # noqa: E501

        :param firm_id: The firm_id of this Job.  # noqa: E501
        :type: int
        """

        self._firm_id = firm_id

    @property
    def job_type(self):
        """Gets the job_type of this Job.  # noqa: E501

        The type of this job. Currently either b for a billing report, pdfrp for a PDF report, or bd for a bulk download  # noqa: E501

        :return: The job_type of this Job.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this Job.

        The type of this job. Currently either b for a billing report, pdfrp for a PDF report, or bd for a bulk download  # noqa: E501

        :param job_type: The job_type of this Job.  # noqa: E501
        :type: str
        """
        allowed_values = ["b = Billing report", "pdfrp = PDF report", "db = Bulk download"]  # noqa: E501
        if job_type not in allowed_values:
            raise ValueError(
                "Invalid value for `job_type` ({0}), must be one of {1}"  # noqa: E501
                .format(job_type, allowed_values)
            )

        self._job_type = job_type

    @property
    def created_dt_utc(self):
        """Gets the created_dt_utc of this Job.  # noqa: E501

        Create timestamp in UTC  # noqa: E501

        :return: The created_dt_utc of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt_utc

    @created_dt_utc.setter
    def created_dt_utc(self, created_dt_utc):
        """Sets the created_dt_utc of this Job.

        Create timestamp in UTC  # noqa: E501

        :param created_dt_utc: The created_dt_utc of this Job.  # noqa: E501
        :type: datetime
        """

        self._created_dt_utc = created_dt_utc

    @property
    def last_updated_dt_utc(self):
        """Gets the last_updated_dt_utc of this Job.  # noqa: E501

        The last date and time this Background Job was updated  # noqa: E501

        :return: The last_updated_dt_utc of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_dt_utc

    @last_updated_dt_utc.setter
    def last_updated_dt_utc(self, last_updated_dt_utc):
        """Sets the last_updated_dt_utc of this Job.

        The last date and time this Background Job was updated  # noqa: E501

        :param last_updated_dt_utc: The last_updated_dt_utc of this Job.  # noqa: E501
        :type: datetime
        """

        self._last_updated_dt_utc = last_updated_dt_utc

    @property
    def queued_dt_utc(self):
        """Gets the queued_dt_utc of this Job.  # noqa: E501

        The last date and time this Background Job was queued  # noqa: E501

        :return: The queued_dt_utc of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._queued_dt_utc

    @queued_dt_utc.setter
    def queued_dt_utc(self, queued_dt_utc):
        """Sets the queued_dt_utc of this Job.

        The last date and time this Background Job was queued  # noqa: E501

        :param queued_dt_utc: The queued_dt_utc of this Job.  # noqa: E501
        :type: datetime
        """

        self._queued_dt_utc = queued_dt_utc

    @property
    def started_dt_utc(self):
        """Gets the started_dt_utc of this Job.  # noqa: E501

        The last date and time this Background Job was started  # noqa: E501

        :return: The started_dt_utc of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._started_dt_utc

    @started_dt_utc.setter
    def started_dt_utc(self, started_dt_utc):
        """Sets the started_dt_utc of this Job.

        The last date and time this Background Job was started  # noqa: E501

        :param started_dt_utc: The started_dt_utc of this Job.  # noqa: E501
        :type: datetime
        """

        self._started_dt_utc = started_dt_utc

    @property
    def finished_dt_utc(self):
        """Gets the finished_dt_utc of this Job.  # noqa: E501

        The last date and time this Background Job was finished  # noqa: E501

        :return: The finished_dt_utc of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_dt_utc

    @finished_dt_utc.setter
    def finished_dt_utc(self, finished_dt_utc):
        """Sets the finished_dt_utc of this Job.

        The last date and time this Background Job was finished  # noqa: E501

        :param finished_dt_utc: The finished_dt_utc of this Job.  # noqa: E501
        :type: datetime
        """

        self._finished_dt_utc = finished_dt_utc

    @property
    def failed_dt_utc(self):
        """Gets the failed_dt_utc of this Job.  # noqa: E501

        The last date and time this Background Job was failed  # noqa: E501

        :return: The failed_dt_utc of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._failed_dt_utc

    @failed_dt_utc.setter
    def failed_dt_utc(self, failed_dt_utc):
        """Sets the failed_dt_utc of this Job.

        The last date and time this Background Job was failed  # noqa: E501

        :param failed_dt_utc: The failed_dt_utc of this Job.  # noqa: E501
        :type: datetime
        """

        self._failed_dt_utc = failed_dt_utc

    @property
    def created_by_id(self):
        """Gets the created_by_id of this Job.  # noqa: E501

        The user id for the user who created this Background Job  # noqa: E501

        :return: The created_by_id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this Job.

        The user id for the user who created this Background Job  # noqa: E501

        :param created_by_id: The created_by_id of this Job.  # noqa: E501
        :type: int
        """

        self._created_by_id = created_by_id

    @property
    def is_finished(self):
        """Gets the is_finished of this Job.  # noqa: E501

        Returns true if the job is finished  # noqa: E501

        :return: The is_finished of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._is_finished

    @is_finished.setter
    def is_finished(self, is_finished):
        """Sets the is_finished of this Job.

        Returns true if the job is finished  # noqa: E501

        :param is_finished: The is_finished of this Job.  # noqa: E501
        :type: bool
        """

        self._is_finished = is_finished

    @property
    def is_running(self):
        """Gets the is_running of this Job.  # noqa: E501

        Returns true if the job has been dequeued and is running  # noqa: E501

        :return: The is_running of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._is_running

    @is_running.setter
    def is_running(self, is_running):
        """Sets the is_running of this Job.

        Returns true if the job has been dequeued and is running  # noqa: E501

        :param is_running: The is_running of this Job.  # noqa: E501
        :type: bool
        """

        self._is_running = is_running

    @property
    def is_failed(self):
        """Gets the is_failed of this Job.  # noqa: E501

        Returns true if the job failed due to an exception  # noqa: E501

        :return: The is_failed of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._is_failed

    @is_failed.setter
    def is_failed(self, is_failed):
        """Sets the is_failed of this Job.

        Returns true if the job failed due to an exception  # noqa: E501

        :param is_failed: The is_failed of this Job.  # noqa: E501
        :type: bool
        """

        self._is_failed = is_failed

    @property
    def is_revoked(self):
        """Gets the is_revoked of this Job.  # noqa: E501

        Returns true if the job was cancelled by the user  # noqa: E501

        :return: The is_revoked of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._is_revoked

    @is_revoked.setter
    def is_revoked(self, is_revoked):
        """Sets the is_revoked of this Job.

        Returns true if the job was cancelled by the user  # noqa: E501

        :param is_revoked: The is_revoked of this Job.  # noqa: E501
        :type: bool
        """

        self._is_revoked = is_revoked

    @property
    def num_steps(self):
        """Gets the num_steps of this Job.  # noqa: E501

        The progress of a job. Note that the number of steps might not be known until the job is dequeued.  # noqa: E501

        :return: The num_steps of this Job.  # noqa: E501
        :rtype: int
        """
        return self._num_steps

    @num_steps.setter
    def num_steps(self, num_steps):
        """Sets the num_steps of this Job.

        The progress of a job. Note that the number of steps might not be known until the job is dequeued.  # noqa: E501

        :param num_steps: The num_steps of this Job.  # noqa: E501
        :type: int
        """

        self._num_steps = num_steps

    @property
    def current_step(self):
        """Gets the current_step of this Job.  # noqa: E501

        Zero corresponds to the job waiting to be processed  # noqa: E501

        :return: The current_step of this Job.  # noqa: E501
        :rtype: int
        """
        return self._current_step

    @current_step.setter
    def current_step(self, current_step):
        """Sets the current_step of this Job.

        Zero corresponds to the job waiting to be processed  # noqa: E501

        :param current_step: The current_step of this Job.  # noqa: E501
        :type: int
        """

        self._current_step = current_step

    @property
    def email_notification(self):
        """Gets the email_notification of this Job.  # noqa: E501

        If true, this sends an email notification to the user who created the job  # noqa: E501

        :return: The email_notification of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """Sets the email_notification of this Job.

        If true, this sends an email notification to the user who created the job  # noqa: E501

        :param email_notification: The email_notification of this Job.  # noqa: E501
        :type: datetime
        """

        self._email_notification = email_notification

    @property
    def email_notification_dt_utc(self):
        """Gets the email_notification_dt_utc of this Job.  # noqa: E501

        The timestamp at which the email notification was sent. Only applies when email_notification is enabled  # noqa: E501

        :return: The email_notification_dt_utc of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._email_notification_dt_utc

    @email_notification_dt_utc.setter
    def email_notification_dt_utc(self, email_notification_dt_utc):
        """Sets the email_notification_dt_utc of this Job.

        The timestamp at which the email notification was sent. Only applies when email_notification is enabled  # noqa: E501

        :param email_notification_dt_utc: The email_notification_dt_utc of this Job.  # noqa: E501
        :type: datetime
        """

        self._email_notification_dt_utc = email_notification_dt_utc

    @property
    def created_at_utc(self):
        """Gets the created_at_utc of this Job.  # noqa: E501

        Timestamp for when the record was created  # noqa: E501

        :return: The created_at_utc of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_utc

    @created_at_utc.setter
    def created_at_utc(self, created_at_utc):
        """Sets the created_at_utc of this Job.

        Timestamp for when the record was created  # noqa: E501

        :param created_at_utc: The created_at_utc of this Job.  # noqa: E501
        :type: datetime
        """

        self._created_at_utc = created_at_utc

    @property
    def updated_at_utc(self):
        """Gets the updated_at_utc of this Job.  # noqa: E501

        Timestamp for when the record was updated  # noqa: E501

        :return: The updated_at_utc of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_utc

    @updated_at_utc.setter
    def updated_at_utc(self, updated_at_utc):
        """Sets the updated_at_utc of this Job.

        Timestamp for when the record was updated  # noqa: E501

        :param updated_at_utc: The updated_at_utc of this Job.  # noqa: E501
        :type: datetime
        """

        self._updated_at_utc = updated_at_utc

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
        if issubclass(Job, dict):
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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
