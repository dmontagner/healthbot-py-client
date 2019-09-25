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


class RuleSchemaRulepropertiesSupporteddevicesJuniperReleases(object):
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
        'platform': 'list[str]',
        'release_name': 'str',
        'release_support': 'str'
    }

    attribute_map = {
        'platform': 'platform',
        'release_name': 'release-name',
        'release_support': 'release-support'
    }

    def __init__(self, platform=None, release_name=None, release_support=None):  # noqa: E501
        """RuleSchemaRulepropertiesSupporteddevicesJuniperReleases - a model defined in Swagger"""  # noqa: E501

        self._platform = None
        self._release_name = None
        self._release_support = None
        self.discriminator = None

        if platform is not None:
            self.platform = platform
        self.release_name = release_name
        if release_support is not None:
            self.release_support = release_support

    @property
    def platform(self):
        """Gets the platform of this RuleSchemaRulepropertiesSupporteddevicesJuniperReleases.  # noqa: E501


        :return: The platform of this RuleSchemaRulepropertiesSupporteddevicesJuniperReleases.  # noqa: E501
        :rtype: list[str]
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this RuleSchemaRulepropertiesSupporteddevicesJuniperReleases.


        :param platform: The platform of this RuleSchemaRulepropertiesSupporteddevicesJuniperReleases.  # noqa: E501
        :type: list[str]
        """

        self._platform = platform

    @property
    def release_name(self):
        """Gets the release_name of this RuleSchemaRulepropertiesSupporteddevicesJuniperReleases.  # noqa: E501

        Release name  # noqa: E501

        :return: The release_name of this RuleSchemaRulepropertiesSupporteddevicesJuniperReleases.  # noqa: E501
        :rtype: str
        """
        return self._release_name

    @release_name.setter
    def release_name(self, release_name):
        """Sets the release_name of this RuleSchemaRulepropertiesSupporteddevicesJuniperReleases.

        Release name  # noqa: E501

        :param release_name: The release_name of this RuleSchemaRulepropertiesSupporteddevicesJuniperReleases.  # noqa: E501
        :type: str
        """
        if release_name is None:
            raise ValueError("Invalid value for `release_name`, must not be `None`")  # noqa: E501
        if release_name is not None and not re.search('^(\\d){1,2}[.](\\d){1}([\\w\\-_\\.]*)$', release_name):  # noqa: E501
            raise ValueError("Invalid value for `release_name`, must be a follow pattern or equal to `/^(\\d){1,2}[.](\\d){1}([\\w\\-_\\.]*)$/`")  # noqa: E501

        self._release_name = release_name

    @property
    def release_support(self):
        """Gets the release_support of this RuleSchemaRulepropertiesSupporteddevicesJuniperReleases.  # noqa: E501

        Specifies the min/max support for this release  # noqa: E501

        :return: The release_support of this RuleSchemaRulepropertiesSupporteddevicesJuniperReleases.  # noqa: E501
        :rtype: str
        """
        return self._release_support

    @release_support.setter
    def release_support(self, release_support):
        """Sets the release_support of this RuleSchemaRulepropertiesSupporteddevicesJuniperReleases.

        Specifies the min/max support for this release  # noqa: E501

        :param release_support: The release_support of this RuleSchemaRulepropertiesSupporteddevicesJuniperReleases.  # noqa: E501
        :type: str
        """
        allowed_values = ["max-supported-release", "only-on-this-release", "min-supported-release"]  # noqa: E501
        if release_support not in allowed_values:
            raise ValueError(
                "Invalid value for `release_support` ({0}), must be one of {1}"  # noqa: E501
                .format(release_support, allowed_values)
            )

        self._release_support = release_support

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
        if not isinstance(other, RuleSchemaRulepropertiesSupporteddevicesJuniperReleases):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other