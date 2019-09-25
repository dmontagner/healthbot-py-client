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


class LicensekeySchemaFeatures(object):
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
        'feature_id': 'int',
        'feature_name': 'str',
        'feature_description': 'str',
        'capacity_value': 'int',
        'capacity_flag': 'bool'
    }

    attribute_map = {
        'feature_id': 'feature-id',
        'feature_name': 'feature-name',
        'feature_description': 'feature-description',
        'capacity_value': 'capacity-value',
        'capacity_flag': 'capacity-flag'
    }

    def __init__(self, feature_id=None, feature_name=None, feature_description=None, capacity_value=None, capacity_flag=None):  # noqa: E501
        """LicensekeySchemaFeatures - a model defined in Swagger"""  # noqa: E501

        self._feature_id = None
        self._feature_name = None
        self._feature_description = None
        self._capacity_value = None
        self._capacity_flag = None
        self.discriminator = None

        self.feature_id = feature_id
        self.feature_name = feature_name
        self.feature_description = feature_description
        self.capacity_value = capacity_value
        self.capacity_flag = capacity_flag

    @property
    def feature_id(self):
        """Gets the feature_id of this LicensekeySchemaFeatures.  # noqa: E501

        Unique ID of the licensed feature  # noqa: E501

        :return: The feature_id of this LicensekeySchemaFeatures.  # noqa: E501
        :rtype: int
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this LicensekeySchemaFeatures.

        Unique ID of the licensed feature  # noqa: E501

        :param feature_id: The feature_id of this LicensekeySchemaFeatures.  # noqa: E501
        :type: int
        """
        if feature_id is None:
            raise ValueError("Invalid value for `feature_id`, must not be `None`")  # noqa: E501
        if feature_id is not None and feature_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `feature_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._feature_id = feature_id

    @property
    def feature_name(self):
        """Gets the feature_name of this LicensekeySchemaFeatures.  # noqa: E501

        Name of the licensed feature  # noqa: E501

        :return: The feature_name of this LicensekeySchemaFeatures.  # noqa: E501
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        """Sets the feature_name of this LicensekeySchemaFeatures.

        Name of the licensed feature  # noqa: E501

        :param feature_name: The feature_name of this LicensekeySchemaFeatures.  # noqa: E501
        :type: str
        """
        if feature_name is None:
            raise ValueError("Invalid value for `feature_name`, must not be `None`")  # noqa: E501

        self._feature_name = feature_name

    @property
    def feature_description(self):
        """Gets the feature_description of this LicensekeySchemaFeatures.  # noqa: E501

        Brief description of the licensed feature  # noqa: E501

        :return: The feature_description of this LicensekeySchemaFeatures.  # noqa: E501
        :rtype: str
        """
        return self._feature_description

    @feature_description.setter
    def feature_description(self, feature_description):
        """Sets the feature_description of this LicensekeySchemaFeatures.

        Brief description of the licensed feature  # noqa: E501

        :param feature_description: The feature_description of this LicensekeySchemaFeatures.  # noqa: E501
        :type: str
        """
        if feature_description is None:
            raise ValueError("Invalid value for `feature_description`, must not be `None`")  # noqa: E501

        self._feature_description = feature_description

    @property
    def capacity_value(self):
        """Gets the capacity_value of this LicensekeySchemaFeatures.  # noqa: E501

        Total capacity of the licensed feature  # noqa: E501

        :return: The capacity_value of this LicensekeySchemaFeatures.  # noqa: E501
        :rtype: int
        """
        return self._capacity_value

    @capacity_value.setter
    def capacity_value(self, capacity_value):
        """Sets the capacity_value of this LicensekeySchemaFeatures.

        Total capacity of the licensed feature  # noqa: E501

        :param capacity_value: The capacity_value of this LicensekeySchemaFeatures.  # noqa: E501
        :type: int
        """
        if capacity_value is None:
            raise ValueError("Invalid value for `capacity_value`, must not be `None`")  # noqa: E501
        if capacity_value is not None and capacity_value < 0:  # noqa: E501
            raise ValueError("Invalid value for `capacity_value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._capacity_value = capacity_value

    @property
    def capacity_flag(self):
        """Gets the capacity_flag of this LicensekeySchemaFeatures.  # noqa: E501

        Flag indicating if the feature is capacity or non-capacity type  # noqa: E501

        :return: The capacity_flag of this LicensekeySchemaFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._capacity_flag

    @capacity_flag.setter
    def capacity_flag(self, capacity_flag):
        """Sets the capacity_flag of this LicensekeySchemaFeatures.

        Flag indicating if the feature is capacity or non-capacity type  # noqa: E501

        :param capacity_flag: The capacity_flag of this LicensekeySchemaFeatures.  # noqa: E501
        :type: bool
        """
        if capacity_flag is None:
            raise ValueError("Invalid value for `capacity_flag`, must not be `None`")  # noqa: E501

        self._capacity_flag = capacity_flag

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
        if not isinstance(other, LicensekeySchemaFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other