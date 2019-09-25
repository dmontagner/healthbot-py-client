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

from swagger_client.models.scheduler_schema import SchedulerSchema  # noqa: F401,E501
from swagger_client.models.systemsettings_schema_systemsettings_reportgeneration import SystemsettingsSchemaSystemsettingsReportgeneration  # noqa: F401,E501


class SystemsettingsSchemaSystemsettings(object):
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
        'persist_raw_data': 'list[ERRORUNKNOWN]',
        'report_generation': 'SystemsettingsSchemaSystemsettingsReportgeneration',
        'scheduler': 'list[SchedulerSchema]'
    }

    attribute_map = {
        'persist_raw_data': 'persist-raw-data',
        'report_generation': 'report-generation',
        'scheduler': 'scheduler'
    }

    def __init__(self, persist_raw_data=None, report_generation=None, scheduler=None):  # noqa: E501
        """SystemsettingsSchemaSystemsettings - a model defined in Swagger"""  # noqa: E501

        self._persist_raw_data = None
        self._report_generation = None
        self._scheduler = None
        self.discriminator = None

        if persist_raw_data is not None:
            self.persist_raw_data = persist_raw_data
        if report_generation is not None:
            self.report_generation = report_generation
        if scheduler is not None:
            self.scheduler = scheduler

    @property
    def persist_raw_data(self):
        """Gets the persist_raw_data of this SystemsettingsSchemaSystemsettings.  # noqa: E501

        Persist raw data in the database  # noqa: E501

        :return: The persist_raw_data of this SystemsettingsSchemaSystemsettings.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._persist_raw_data

    @persist_raw_data.setter
    def persist_raw_data(self, persist_raw_data):
        """Sets the persist_raw_data of this SystemsettingsSchemaSystemsettings.

        Persist raw data in the database  # noqa: E501

        :param persist_raw_data: The persist_raw_data of this SystemsettingsSchemaSystemsettings.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._persist_raw_data = persist_raw_data

    @property
    def report_generation(self):
        """Gets the report_generation of this SystemsettingsSchemaSystemsettings.  # noqa: E501


        :return: The report_generation of this SystemsettingsSchemaSystemsettings.  # noqa: E501
        :rtype: SystemsettingsSchemaSystemsettingsReportgeneration
        """
        return self._report_generation

    @report_generation.setter
    def report_generation(self, report_generation):
        """Sets the report_generation of this SystemsettingsSchemaSystemsettings.


        :param report_generation: The report_generation of this SystemsettingsSchemaSystemsettings.  # noqa: E501
        :type: SystemsettingsSchemaSystemsettingsReportgeneration
        """

        self._report_generation = report_generation

    @property
    def scheduler(self):
        """Gets the scheduler of this SystemsettingsSchemaSystemsettings.  # noqa: E501


        :return: The scheduler of this SystemsettingsSchemaSystemsettings.  # noqa: E501
        :rtype: list[SchedulerSchema]
        """
        return self._scheduler

    @scheduler.setter
    def scheduler(self, scheduler):
        """Sets the scheduler of this SystemsettingsSchemaSystemsettings.


        :param scheduler: The scheduler of this SystemsettingsSchemaSystemsettings.  # noqa: E501
        :type: list[SchedulerSchema]
        """

        self._scheduler = scheduler

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
        if not isinstance(other, SystemsettingsSchemaSystemsettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
