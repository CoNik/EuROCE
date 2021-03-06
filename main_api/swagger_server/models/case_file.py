# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util
from swagger_server.models.cluster import Cluster
from swagger_server.models.tag import Tag

class CaseFile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, clusters: List[Cluster]=None, name: str=None, url: str=None, tags: List[Tag]=None):  # noqa: E501
        """CaseFile - a model defined in Swagger

        :param id: The id of this CaseFile.  # noqa: E501
        :type id: int
        :param clusters: The clusters of this CaseFile.  # noqa: E501
        :type clusters: List[Cluster]
        :param name: The name of this CaseFile.  # noqa: E501
        :type name: str
        :param url: The url of this CaseFile.  # noqa: E501
        :type url: str
        :param tags: The tags of this CaseFile.  # noqa: E501
        :type tags: List[Tag]
        """
        self.swagger_types = {
            'id': int,
            'clusters': List[Cluster],
            'name': str,
            'url': str,
            'tags': List[Tag]
        }

        self.attribute_map = {
            'id': 'id',
            'clusters': 'clusters',
            'name': 'name',
            'url': 'url',
            'tags': 'tags'
        }

        self._id = id
        self._clusters = clusters
        self._name = name
        self._url = url
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt) -> 'CaseFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Case-File of this CaseFile.  # noqa: E501
        :rtype: CaseFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this CaseFile.


        :return: The id of this CaseFile.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this CaseFile.


        :param id: The id of this CaseFile.
        :type id: int
        """

        self._id = id

    @property
    def clusters(self) -> List[Cluster]:
        """Gets the clusters of this CaseFile.


        :return: The clusters of this CaseFile.
        :rtype: List[Cluster]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters: List[Cluster]):
        """Sets the clusters of this CaseFile.


        :param clusters: The clusters of this CaseFile.
        :type clusters: List[Cluster]
        """

        self._clusters = clusters

    @property
    def name(self) -> str:
        """Gets the name of this CaseFile.


        :return: The name of this CaseFile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this CaseFile.


        :param name: The name of this CaseFile.
        :type name: str
        """

        self._name = name

    @property
    def url(self) -> str:
        """Gets the url of this CaseFile.


        :return: The url of this CaseFile.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this CaseFile.


        :param url: The url of this CaseFile.
        :type url: str
        """

        self._url = url

    @property
    def tags(self) -> List[Tag]:
        """Gets the tags of this CaseFile.


        :return: The tags of this CaseFile.
        :rtype: List[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags: List[Tag]):
        """Sets the tags of this CaseFile.


        :param tags: The tags of this CaseFile.
        :type tags: List[Tag]
        """

        self._tags = tags
