# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.case_file import CaseFile  # noqa: E501
from swagger_server.models.dashboard_statistics import DashboardStatistics  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPublicAPIController(BaseTestCase):
    """PublicAPIController integration test stubs"""

    def test_find_case_files(self):
        """Test case for find_case_files

        Request opening a case file based on a website URL
        """
        data = dict(url='url_example')
        response = self.client.open(
            '/api/targets/requestNew',
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_case_file(self):
        """Test case for get_case_file

        Retrieves a specific case file from its UUID
        """
        response = self.client.open(
            '/api/case-file/uuid/{UUID}'.format(UUID='UUID_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dashboard_stats(self):
        """Test case for get_dashboard_stats

        Returns the dashboard statistics
        """
        response = self.client.open(
            '/api/dashboard/stats',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_case_files(self):
        """Test case for search_case_files

        Search existing case files based on a specific parameter
        """
        query_string = [('tags', 'tags_example'),
                        ('hostnames', 'hostnames_example'),
                        ('geos', 'geos_example')]
        response = self.client.open(
            '/api/case-file/search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
