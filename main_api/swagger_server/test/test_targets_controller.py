# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.target import Target  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTargetsController(BaseTestCase):
    """TargetsController integration test stubs"""

    def test_delete_targets(self):
        """Test case for delete_targets

        Changes the properties of a specific target
        """
        response = self.client.open(
            '/api/targets/{targetID}'.format(targetID=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_target(self):
        """Test case for edit_target

        Changes the properties of a specific target
        """
        body = Target()
        response = self.client.open(
            '/api/targets/{targetID}'.format(targetID=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_target_by_id(self):
        """Test case for get_target_by_id

        Gets the target based on its ID
        """
        response = self.client.open(
            '/api/targets/{targetID}'.format(targetID=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
