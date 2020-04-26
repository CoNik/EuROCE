# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.case_file import CaseFile  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCaseFilesController(BaseTestCase):
    """CaseFilesController integration test stubs"""

    def test_edit_case_file(self):
        """Test case for edit_case_file

        Changes the properties of a specific case file
        """
        body = User()
        response = self.client.open(
            '/api/case-file/uuid/{UUID}'.format(UUID='UUID_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
