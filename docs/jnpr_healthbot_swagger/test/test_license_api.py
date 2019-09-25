# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.license_api import LicenseApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLicenseApi(unittest.TestCase):
    """LicenseApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.license_api.LicenseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_iceberg_add_license_from_file(self):
        """Test case for create_iceberg_add_license_from_file

        Add license from file.  # noqa: E501
        """
        pass

    def test_delete_iceberg_delete_all_license(self):
        """Test case for delete_iceberg_delete_all_license

        Delete all licenses.  # noqa: E501
        """
        pass

    def test_delete_iceberg_delete_license_by_id(self):
        """Test case for delete_iceberg_delete_license_by_id

        Delete a license.  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_get_all_license_id(self):
        """Test case for retrieve_iceberg_get_all_license_id

        List of available license id's.  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_license_features_info(self):
        """Test case for retrieve_iceberg_license_features_info

        Status of all the licensed features.  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_license_file_by_license_id(self):
        """Test case for retrieve_iceberg_license_file_by_license_id

        Download license file.  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_license_key_contents(self):
        """Test case for retrieve_iceberg_license_key_contents

        Get the contents of all licenses.  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_license_key_contents_by_id(self):
        """Test case for retrieve_iceberg_license_key_contents_by_id

        Get the contents of a license.  # noqa: E501
        """
        pass

    def test_update_iceberg_replace_license(self):
        """Test case for update_iceberg_replace_license

        Update the license.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
