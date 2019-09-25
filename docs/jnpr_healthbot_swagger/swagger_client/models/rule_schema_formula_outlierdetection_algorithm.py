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

from swagger_client.models.rule_schema_formula_outlierdetection_algorithm_dbscan import RuleSchemaFormulaOutlierdetectionAlgorithmDbscan  # noqa: F401,E501
from swagger_client.models.rule_schema_formula_outlierdetection_algorithm_kfold3sigma import RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma  # noqa: F401,E501


class RuleSchemaFormulaOutlierdetectionAlgorithm(object):
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
        'dbscan': 'RuleSchemaFormulaOutlierdetectionAlgorithmDbscan',
        'k_fold_3sigma': 'RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma'
    }

    attribute_map = {
        'dbscan': 'dbscan',
        'k_fold_3sigma': 'k-fold-3sigma'
    }

    def __init__(self, dbscan=None, k_fold_3sigma=None):  # noqa: E501
        """RuleSchemaFormulaOutlierdetectionAlgorithm - a model defined in Swagger"""  # noqa: E501

        self._dbscan = None
        self._k_fold_3sigma = None
        self.discriminator = None

        if dbscan is not None:
            self.dbscan = dbscan
        if k_fold_3sigma is not None:
            self.k_fold_3sigma = k_fold_3sigma

    @property
    def dbscan(self):
        """Gets the dbscan of this RuleSchemaFormulaOutlierdetectionAlgorithm.  # noqa: E501


        :return: The dbscan of this RuleSchemaFormulaOutlierdetectionAlgorithm.  # noqa: E501
        :rtype: RuleSchemaFormulaOutlierdetectionAlgorithmDbscan
        """
        return self._dbscan

    @dbscan.setter
    def dbscan(self, dbscan):
        """Sets the dbscan of this RuleSchemaFormulaOutlierdetectionAlgorithm.


        :param dbscan: The dbscan of this RuleSchemaFormulaOutlierdetectionAlgorithm.  # noqa: E501
        :type: RuleSchemaFormulaOutlierdetectionAlgorithmDbscan
        """

        self._dbscan = dbscan

    @property
    def k_fold_3sigma(self):
        """Gets the k_fold_3sigma of this RuleSchemaFormulaOutlierdetectionAlgorithm.  # noqa: E501


        :return: The k_fold_3sigma of this RuleSchemaFormulaOutlierdetectionAlgorithm.  # noqa: E501
        :rtype: RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma
        """
        return self._k_fold_3sigma

    @k_fold_3sigma.setter
    def k_fold_3sigma(self, k_fold_3sigma):
        """Sets the k_fold_3sigma of this RuleSchemaFormulaOutlierdetectionAlgorithm.


        :param k_fold_3sigma: The k_fold_3sigma of this RuleSchemaFormulaOutlierdetectionAlgorithm.  # noqa: E501
        :type: RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma
        """

        self._k_fold_3sigma = k_fold_3sigma

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
        if not isinstance(other, RuleSchemaFormulaOutlierdetectionAlgorithm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
