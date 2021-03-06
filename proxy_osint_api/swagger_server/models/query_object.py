# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class QueryObject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, ipv4: str=None, ipv6: str=None, fqdn: str=None, url: str=None):  # noqa: E501
        """QueryObject - a model defined in Swagger

        :param ipv4: The ipv4 of this QueryObject.  # noqa: E501
        :type ipv4: str
        :param ipv6: The ipv6 of this QueryObject.  # noqa: E501
        :type ipv6: str
        :param fqdn: The fqdn of this QueryObject.  # noqa: E501
        :type fqdn: str
        :param url: The url of this QueryObject.  # noqa: E501
        :type url: str
        """
        self.swagger_types = {
            'ipv4': str,
            'ipv6': str,
            'fqdn': str,
            'url': str
        }

        self.attribute_map = {
            'ipv4': 'ipv4',
            'ipv6': 'ipv6',
            'fqdn': 'fqdn',
            'url': 'URL'
        }

        self._ipv4 = ipv4
        self._ipv6 = ipv6
        self._fqdn = fqdn
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'QueryObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QueryObject of this QueryObject.  # noqa: E501
        :rtype: QueryObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ipv4(self) -> str:
        """Gets the ipv4 of this QueryObject.


        :return: The ipv4 of this QueryObject.
        :rtype: str
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4: str):
        """Sets the ipv4 of this QueryObject.


        :param ipv4: The ipv4 of this QueryObject.
        :type ipv4: str
        """

        self._ipv4 = ipv4

    @property
    def ipv6(self) -> str:
        """Gets the ipv6 of this QueryObject.


        :return: The ipv6 of this QueryObject.
        :rtype: str
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6: str):
        """Sets the ipv6 of this QueryObject.


        :param ipv6: The ipv6 of this QueryObject.
        :type ipv6: str
        """

        self._ipv6 = ipv6

    @property
    def fqdn(self) -> str:
        """Gets the fqdn of this QueryObject.


        :return: The fqdn of this QueryObject.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn: str):
        """Sets the fqdn of this QueryObject.


        :param fqdn: The fqdn of this QueryObject.
        :type fqdn: str
        """

        self._fqdn = fqdn

    @property
    def url(self) -> str:
        """Gets the url of this QueryObject.


        :return: The url of this QueryObject.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this QueryObject.


        :param url: The url of this QueryObject.
        :type url: str
        """

        self._url = url
