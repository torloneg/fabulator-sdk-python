# coding: utf-8

"""
    Fabulator API

    Endpoint Fabulator project  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: torloneg@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.example_api import ExampleApi  # noqa: E501
from swagger_client.rest import ApiException


class TestExampleApi(unittest.TestCase):
    """ExampleApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.example_api.ExampleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_example_v1_iddomain_id(self):
        """Test case for delete_example_v1_iddomain_id

        """
        pass

    def test_get_example_v1_info_iddomain_id(self):
        """Test case for get_example_v1_info_iddomain_id

        """
        pass

    def test_patch_example_v1_update_iddomain_id_field_value(self):
        """Test case for patch_example_v1_update_iddomain_id_field_value

        """
        pass

    def test_post_example_v1_add_iddomain(self):
        """Test case for post_example_v1_add_iddomain

        """
        pass

    def test_post_example_v1_query_iddomain_skip_limit(self):
        """Test case for post_example_v1_query_iddomain_skip_limit

        """
        pass

    def test_put_example_v1_update_iddomain_id(self):
        """Test case for put_example_v1_update_iddomain_id

        """
        pass

    def test_put_example_v1_update_json_iddomain_id(self):
        """Test case for put_example_v1_update_json_iddomain_id

        """
        pass


if __name__ == '__main__':
    unittest.main()
