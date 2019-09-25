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

from jnpr.healthbot.swagger.models.rule_schema_then_status import RuleSchemaThenStatus  # noqa: F401,E501
from jnpr.healthbot.swagger.models.rule_schema_then_userdefinedaction import RuleSchemaThenUserdefinedaction  # noqa: F401,E501


class RuleSchemaThen(object):
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
        'next': 'list[ERRORUNKNOWN]',
        'status': 'RuleSchemaThenStatus',
        'user_defined_action': 'list[RuleSchemaThenUserdefinedaction]'
    }

    attribute_map = {
        'next': 'next',
        'status': 'status',
        'user_defined_action': 'user-defined-action'
    }

    def __init__(self, next=None, status=None, user_defined_action=None):  # noqa: E501
        """RuleSchemaThen - a model defined in Swagger"""  # noqa: E501

        self._next = None
        self._status = None
        self._user_defined_action = None
        self.discriminator = None

        if next is not None:
            self.next = next
        if status is not None:
            self.status = status
        if user_defined_action is not None:
            self.user_defined_action = user_defined_action

    @property
    def next(self):
        """Gets the next of this RuleSchemaThen.  # noqa: E501

        Continue evaluating next term in a trigger  # noqa: E501

        :return: The next of this RuleSchemaThen.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this RuleSchemaThen.

        Continue evaluating next term in a trigger  # noqa: E501

        :param next: The next of this RuleSchemaThen.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._next = next

    @property
    def status(self):
        """Gets the status of this RuleSchemaThen.  # noqa: E501


        :return: The status of this RuleSchemaThen.  # noqa: E501
        :rtype: RuleSchemaThenStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RuleSchemaThen.


        :param status: The status of this RuleSchemaThen.  # noqa: E501
        :type: RuleSchemaThenStatus
        """

        self._status = status

    @property
    def user_defined_action(self):
        """Gets the user_defined_action of this RuleSchemaThen.  # noqa: E501


        :return: The user_defined_action of this RuleSchemaThen.  # noqa: E501
        :rtype: list[RuleSchemaThenUserdefinedaction]
        """
        return self._user_defined_action

    @user_defined_action.setter
    def user_defined_action(self, user_defined_action):
        """Sets the user_defined_action of this RuleSchemaThen.


        :param user_defined_action: The user_defined_action of this RuleSchemaThen.  # noqa: E501
        :type: list[RuleSchemaThenUserdefinedaction]
        """

        self._user_defined_action = user_defined_action

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
        if not isinstance(other, RuleSchemaThen):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other