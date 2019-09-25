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

from swagger_client.models.rule_schema_then import RuleSchemaThen  # noqa: F401,E501
from swagger_client.models.rule_schema_when import RuleSchemaWhen  # noqa: F401,E501


class RuleSchemaTerm(object):
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
        'term_name': 'str',
        'then': 'RuleSchemaThen',
        'when': 'RuleSchemaWhen'
    }

    attribute_map = {
        'term_name': 'term-name',
        'then': 'then',
        'when': 'when'
    }

    def __init__(self, term_name=None, then=None, when=None):  # noqa: E501
        """RuleSchemaTerm - a model defined in Swagger"""  # noqa: E501

        self._term_name = None
        self._then = None
        self._when = None
        self.discriminator = None

        self.term_name = term_name
        if then is not None:
            self.then = then
        if when is not None:
            self.when = when

    @property
    def term_name(self):
        """Gets the term_name of this RuleSchemaTerm.  # noqa: E501

        Term name. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The term_name of this RuleSchemaTerm.  # noqa: E501
        :rtype: str
        """
        return self._term_name

    @term_name.setter
    def term_name(self, term_name):
        """Sets the term_name of this RuleSchemaTerm.

        Term name. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param term_name: The term_name of this RuleSchemaTerm.  # noqa: E501
        :type: str
        """
        if term_name is None:
            raise ValueError("Invalid value for `term_name`, must not be `None`")  # noqa: E501
        if term_name is not None and len(term_name) > 64:
            raise ValueError("Invalid value for `term_name`, length must be less than or equal to `64`")  # noqa: E501
        if term_name is not None and not re.search('^[a-zA-Z][a-zA-Z0-9_-]*$', term_name):  # noqa: E501
            raise ValueError("Invalid value for `term_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._term_name = term_name

    @property
    def then(self):
        """Gets the then of this RuleSchemaTerm.  # noqa: E501


        :return: The then of this RuleSchemaTerm.  # noqa: E501
        :rtype: RuleSchemaThen
        """
        return self._then

    @then.setter
    def then(self, then):
        """Sets the then of this RuleSchemaTerm.


        :param then: The then of this RuleSchemaTerm.  # noqa: E501
        :type: RuleSchemaThen
        """

        self._then = then

    @property
    def when(self):
        """Gets the when of this RuleSchemaTerm.  # noqa: E501


        :return: The when of this RuleSchemaTerm.  # noqa: E501
        :rtype: RuleSchemaWhen
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this RuleSchemaTerm.


        :param when: The when of this RuleSchemaTerm.  # noqa: E501
        :type: RuleSchemaWhen
        """

        self._when = when

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
        if not isinstance(other, RuleSchemaTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
