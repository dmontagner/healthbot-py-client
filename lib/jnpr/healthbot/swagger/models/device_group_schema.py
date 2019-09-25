# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from jnpr.healthbot.swagger.models.devicegroup_schema_authentication import DevicegroupSchemaAuthentication  # noqa: F401,E501
from jnpr.healthbot.swagger.models.devicegroup_schema_logging import DevicegroupSchemaLogging  # noqa: F401,E501
from jnpr.healthbot.swagger.models.devicegroup_schema_nativegpb import DevicegroupSchemaNativegpb  # noqa: F401,E501
from jnpr.healthbot.swagger.models.devicegroup_schema_notification import DevicegroupSchemaNotification  # noqa: F401,E501
from jnpr.healthbot.swagger.models.devicegroup_schema_rawdata import DevicegroupSchemaRawdata  # noqa: F401,E501
from jnpr.healthbot.swagger.models.devicegroup_schema_scheduler import DevicegroupSchemaScheduler  # noqa: F401,E501
from jnpr.healthbot.swagger.models.devicegroup_schema_variable import DevicegroupSchemaVariable  # noqa: F401,E501


class DeviceGroupSchema(object):
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
        'authentication': 'DevicegroupSchemaAuthentication',
        'description': 'str',
        'device_group_name': 'str',
        'devices': 'list[str]',
        'logging': 'DevicegroupSchemaLogging',
        'native_gpb': 'DevicegroupSchemaNativegpb',
        'raw_data': 'DevicegroupSchemaRawdata',
        'notification': 'DevicegroupSchemaNotification',
        'playbooks': 'list[str]',
        'reports': 'list[str]',
        'retention_policy': 'str',
        'scheduler': 'list[DevicegroupSchemaScheduler]',
        'variable': 'list[DevicegroupSchemaVariable]'
    }

    attribute_map = {
        'authentication': 'authentication',
        'description': 'description',
        'device_group_name': 'device-group-name',
        'devices': 'devices',
        'logging': 'logging',
        'native_gpb': 'native-gpb',
        'raw_data': 'raw-data',
        'notification': 'notification',
        'playbooks': 'playbooks',
        'reports': 'reports',
        'retention_policy': 'retention-policy',
        'scheduler': 'scheduler',
        'variable': 'variable'
    }

    def __init__(self, authentication=None, description=None, device_group_name=None, devices=None, logging=None, native_gpb=None, raw_data=None, notification=None, playbooks=None, reports=None, retention_policy=None, scheduler=None, variable=None):  # noqa: E501
        """DeviceGroupSchema - a model defined in Swagger"""  # noqa: E501

        self._authentication = None
        self._description = None
        self._device_group_name = None
        self._devices = None
        self._logging = None
        self._native_gpb = None
        self._raw_data = None
        self._notification = None
        self._playbooks = None
        self._reports = None
        self._retention_policy = None
        self._scheduler = None
        self._variable = None
        self.discriminator = None

        if authentication is not None:
            self.authentication = authentication
        if description is not None:
            self.description = description
        self.device_group_name = device_group_name
        if devices is not None:
            self.devices = devices
        if logging is not None:
            self.logging = logging
        if native_gpb is not None:
            self.native_gpb = native_gpb
        if raw_data is not None:
            self.raw_data = raw_data
        if notification is not None:
            self.notification = notification
        if playbooks is not None:
            self.playbooks = playbooks
        if reports is not None:
            self.reports = reports
        if retention_policy is not None:
            self.retention_policy = retention_policy
        if scheduler is not None:
            self.scheduler = scheduler
        if variable is not None:
            self.variable = variable

    @property
    def authentication(self):
        """Gets the authentication of this DeviceGroupSchema.  # noqa: E501


        :return: The authentication of this DeviceGroupSchema.  # noqa: E501
        :rtype: DevicegroupSchemaAuthentication
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this DeviceGroupSchema.


        :param authentication: The authentication of this DeviceGroupSchema.  # noqa: E501
        :type: DevicegroupSchemaAuthentication
        """

        self._authentication = authentication

    @property
    def description(self):
        """Gets the description of this DeviceGroupSchema.  # noqa: E501

        Description about the device group  # noqa: E501

        :return: The description of this DeviceGroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceGroupSchema.

        Description about the device group  # noqa: E501

        :param description: The description of this DeviceGroupSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def device_group_name(self):
        """Gets the device_group_name of this DeviceGroupSchema.  # noqa: E501

        Name of the group. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The device_group_name of this DeviceGroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._device_group_name

    @device_group_name.setter
    def device_group_name(self, device_group_name):
        """Sets the device_group_name of this DeviceGroupSchema.

        Name of the group. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param device_group_name: The device_group_name of this DeviceGroupSchema.  # noqa: E501
        :type: str
        """
        if device_group_name is None:
            raise ValueError("Invalid value for `device_group_name`, must not be `None`")  # noqa: E501
        if device_group_name is not None and len(device_group_name) > 64:
            raise ValueError("Invalid value for `device_group_name`, length must be less than or equal to `64`")  # noqa: E501
        if device_group_name is not None and not re.search('^[a-zA-Z][a-zA-Z0-9_-]*$', device_group_name):  # noqa: E501
            raise ValueError("Invalid value for `device_group_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._device_group_name = device_group_name

    @property
    def devices(self):
        """Gets the devices of this DeviceGroupSchema.  # noqa: E501


        :return: The devices of this DeviceGroupSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this DeviceGroupSchema.


        :param devices: The devices of this DeviceGroupSchema.  # noqa: E501
        :type: list[str]
        """

        self._devices = devices

    @property
    def logging(self):
        """Gets the logging of this DeviceGroupSchema.  # noqa: E501


        :return: The logging of this DeviceGroupSchema.  # noqa: E501
        :rtype: DevicegroupSchemaLogging
        """
        return self._logging

    @logging.setter
    def logging(self, logging):
        """Sets the logging of this DeviceGroupSchema.


        :param logging: The logging of this DeviceGroupSchema.  # noqa: E501
        :type: DevicegroupSchemaLogging
        """

        self._logging = logging

    @property
    def native_gpb(self):
        """Gets the native_gpb of this DeviceGroupSchema.  # noqa: E501


        :return: The native_gpb of this DeviceGroupSchema.  # noqa: E501
        :rtype: DevicegroupSchemaNativegpb
        """
        return self._native_gpb

    @native_gpb.setter
    def native_gpb(self, native_gpb):
        """Sets the native_gpb of this DeviceGroupSchema.


        :param native_gpb: The native_gpb of this DeviceGroupSchema.  # noqa: E501
        :type: DevicegroupSchemaNativegpb
        """

        self._native_gpb = native_gpb

    @property
    def raw_data(self):
        """Gets the raw_data of this DeviceGroupSchema.  # noqa: E501


        :return: The raw_data of this DeviceGroupSchema.  # noqa: E501
        :rtype: DevicegroupSchemaRawdata
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """Sets the raw_data of this DeviceGroupSchema.


        :param raw_data: The raw_data of this DeviceGroupSchema.  # noqa: E501
        :type: DevicegroupSchemaRawdata
        """

        self._raw_data = raw_data

    @property
    def notification(self):
        """Gets the notification of this DeviceGroupSchema.  # noqa: E501


        :return: The notification of this DeviceGroupSchema.  # noqa: E501
        :rtype: DevicegroupSchemaNotification
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this DeviceGroupSchema.


        :param notification: The notification of this DeviceGroupSchema.  # noqa: E501
        :type: DevicegroupSchemaNotification
        """

        self._notification = notification

    @property
    def playbooks(self):
        """Gets the playbooks of this DeviceGroupSchema.  # noqa: E501


        :return: The playbooks of this DeviceGroupSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._playbooks

    @playbooks.setter
    def playbooks(self, playbooks):
        """Sets the playbooks of this DeviceGroupSchema.


        :param playbooks: The playbooks of this DeviceGroupSchema.  # noqa: E501
        :type: list[str]
        """

        self._playbooks = playbooks

    @property
    def reports(self):
        """Gets the reports of this DeviceGroupSchema.  # noqa: E501


        :return: The reports of this DeviceGroupSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this DeviceGroupSchema.


        :param reports: The reports of this DeviceGroupSchema.  # noqa: E501
        :type: list[str]
        """

        self._reports = reports

    @property
    def retention_policy(self):
        """Gets the retention_policy of this DeviceGroupSchema.  # noqa: E501

        Name of the retention policy to be applied  # noqa: E501

        :return: The retention_policy of this DeviceGroupSchema.  # noqa: E501
        :rtype: str
        """
        return self._retention_policy

    @retention_policy.setter
    def retention_policy(self, retention_policy):
        """Sets the retention_policy of this DeviceGroupSchema.

        Name of the retention policy to be applied  # noqa: E501

        :param retention_policy: The retention_policy of this DeviceGroupSchema.  # noqa: E501
        :type: str
        """
        if retention_policy is not None and len(retention_policy) > 64:
            raise ValueError("Invalid value for `retention_policy`, length must be less than or equal to `64`")  # noqa: E501
        if retention_policy is not None and not re.search('^[a-zA-Z][a-zA-Z0-9_-]*$', retention_policy):  # noqa: E501
            raise ValueError("Invalid value for `retention_policy`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._retention_policy = retention_policy

    @property
    def scheduler(self):
        """Gets the scheduler of this DeviceGroupSchema.  # noqa: E501

        List of schedulers associated with the playbook instances  # noqa: E501

        :return: The scheduler of this DeviceGroupSchema.  # noqa: E501
        :rtype: list[DevicegroupSchemaScheduler]
        """
        return self._scheduler

    @scheduler.setter
    def scheduler(self, scheduler):
        """Sets the scheduler of this DeviceGroupSchema.

        List of schedulers associated with the playbook instances  # noqa: E501

        :param scheduler: The scheduler of this DeviceGroupSchema.  # noqa: E501
        :type: list[DevicegroupSchemaScheduler]
        """

        self._scheduler = scheduler

    @property
    def variable(self):
        """Gets the variable of this DeviceGroupSchema.  # noqa: E501

        Playbook variable configuration  # noqa: E501

        :return: The variable of this DeviceGroupSchema.  # noqa: E501
        :rtype: list[DevicegroupSchemaVariable]
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this DeviceGroupSchema.

        Playbook variable configuration  # noqa: E501

        :param variable: The variable of this DeviceGroupSchema.  # noqa: E501
        :type: list[DevicegroupSchemaVariable]
        """

        self._variable = variable

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceGroupSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other