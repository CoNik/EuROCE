# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.query_object import QueryObject  # noqa: E501
from swagger_server.models.query_response import QueryResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestQueryController(BaseTestCase):
    """QueryController integration test stubs"""

    def test_quary(self):
        """Test case for quary

        Queries an external service to build information about a case file
        """
        body = QueryObject()
        response = self.client.open(
            '/query',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
