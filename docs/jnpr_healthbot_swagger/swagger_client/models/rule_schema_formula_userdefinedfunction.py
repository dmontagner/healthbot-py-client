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

from swagger_client.models.rule_schema_formula_userdefinedfunction_argument import RuleSchemaFormulaUserdefinedfunctionArgument  # noqa: F401,E501


class RuleSchemaFormulaUserdefinedfunction(object):
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
        'argument': 'list[RuleSchemaFormulaUserdefinedfunctionArgument]',
        'function_name': 'str'
    }

    attribute_map = {
        'argument': 'argument',
        'function_name': 'function-name'
    }

    def __init__(self, argument=None, function_name=None):  # noqa: E501
        """RuleSchemaFormulaUserdefinedfunction - a model defined in Swagger"""  # noqa: E501

        self._argument = None
        self._function_name = None
        self.discriminator = None

        if argument is not None:
            self.argument = argument
        self.function_name = function_name

    @property
    def argument(self):
        """Gets the argument of this RuleSchemaFormulaUserdefinedfunction.  # noqa: E501


        :return: The argument of this RuleSchemaFormulaUserdefinedfunction.  # noqa: E501
        :rtype: list[RuleSchemaFormulaUserdefinedfunctionArgument]
        """
        return self._argument

    @argument.setter
    def argument(self, argument):
        """Sets the argument of this RuleSchemaFormulaUserdefinedfunction.


        :param argument: The argument of this RuleSchemaFormulaUserdefinedfunction.  # noqa: E501
        :type: list[RuleSchemaFormulaUserdefinedfunctionArgument]
        """

        self._argument = argument

    @property
    def function_name(self):
        """Gets the function_name of this RuleSchemaFormulaUserdefinedfunction.  # noqa: E501

        Function name  # noqa: E501

        :return: The function_name of this RuleSchemaFormulaUserdefinedfunction.  # noqa: E501
        :rtype: str
        """
        return self._function_name

    @function_name.setter
    def function_name(self, function_name):
        """Sets the function_name of this RuleSchemaFormulaUserdefinedfunction.

        Function name  # noqa: E501

        :param function_name: The function_name of this RuleSchemaFormulaUserdefinedfunction.  # noqa: E501
        :type: str
        """
        if function_name is None:
            raise ValueError("Invalid value for `function_name`, must not be `None`")  # noqa: E501
        if function_name is not None and len(function_name) > 64:
            raise ValueError("Invalid value for `function_name`, length must be less than or equal to `64`")  # noqa: E501
        if function_name is not None and not re.search('^[a-zA-Z][a-zA-Z0-9_-]*$', function_name):  # noqa: E501
            raise ValueError("Invalid value for `function_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._function_name = function_name

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
        if not isinstance(other, RuleSchemaFormulaUserdefinedfunction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
