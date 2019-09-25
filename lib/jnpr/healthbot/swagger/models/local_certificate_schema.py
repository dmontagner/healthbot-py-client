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


class LocalCertificateSchema(object):
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
        'client_crt': 'str',
        'client_key': 'str',
        'name': 'str'
    }

    attribute_map = {
        'client_crt': 'client-crt',
        'client_key': 'client-key',
        'name': 'name'
    }

    def __init__(self, client_crt=None, client_key=None, name=None):  # noqa: E501
        """LocalCertificateSchema - a model defined in Swagger"""  # noqa: E501

        self._client_crt = None
        self._client_key = None
        self._name = None
        self.discriminator = None

        self.client_crt = client_crt
        self.client_key = client_key
        self.name = name

    @property
    def client_crt(self):
        """Gets the client_crt of this LocalCertificateSchema.  # noqa: E501

        Client certificate file name. Should be of pattern .+\\.crt  # noqa: E501

        :return: The client_crt of this LocalCertificateSchema.  # noqa: E501
        :rtype: str
        """
        return self._client_crt

    @client_crt.setter
    def client_crt(self, client_crt):
        """Sets the client_crt of this LocalCertificateSchema.

        Client certificate file name. Should be of pattern .+\\.crt  # noqa: E501

        :param client_crt: The client_crt of this LocalCertificateSchema.  # noqa: E501
        :type: str
        """
        if client_crt is None:
            raise ValueError("Invalid value for `client_crt`, must not be `None`")  # noqa: E501
        if client_crt is not None and not re.search('^.+\\.crt$', client_crt):  # noqa: E501
            raise ValueError("Invalid value for `client_crt`, must be a follow pattern or equal to `/^.+\\.crt$/`")  # noqa: E501

        self._client_crt = client_crt

    @property
    def client_key(self):
        """Gets the client_key of this LocalCertificateSchema.  # noqa: E501

        Client Key file name. Should be of pattern .+\\.key  # noqa: E501

        :return: The client_key of this LocalCertificateSchema.  # noqa: E501
        :rtype: str
        """
        return self._client_key

    @client_key.setter
    def client_key(self, client_key):
        """Sets the client_key of this LocalCertificateSchema.

        Client Key file name. Should be of pattern .+\\.key  # noqa: E501

        :param client_key: The client_key of this LocalCertificateSchema.  # noqa: E501
        :type: str
        """
        if client_key is None:
            raise ValueError("Invalid value for `client_key`, must not be `None`")  # noqa: E501
        if client_key is not None and not re.search('^.+\\.key$', client_key):  # noqa: E501
            raise ValueError("Invalid value for `client_key`, must be a follow pattern or equal to `/^.+\\.key$/`")  # noqa: E501

        self._client_key = client_key

    @property
    def name(self):
        """Gets the name of this LocalCertificateSchema.  # noqa: E501

        Local Certificate profile name  # noqa: E501

        :return: The name of this LocalCertificateSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LocalCertificateSchema.

        Local Certificate profile name  # noqa: E501

        :param name: The name of this LocalCertificateSchema.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, LocalCertificateSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
