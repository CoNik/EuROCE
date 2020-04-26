# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Cluster(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, type: str=None):  # noqa: E501
        """Cluster - a model defined in Swagger

        :param id: The id of this Cluster.  # noqa: E501
        :type id: int
        :param name: The name of this Cluster.  # noqa: E501
        :type name: str
        :param type: The type of this Cluster.  # noqa: E501
        :type type: str
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type'
        }

        self._id = id
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Cluster':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Cluster of this Cluster.  # noqa: E501
        :rtype: Cluster
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Cluster.


        :return: The id of this Cluster.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Cluster.


        :param id: The id of this Cluster.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Cluster.


        :return: The name of this Cluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Cluster.


        :param name: The name of this Cluster.
        :type name: str
        """

        self._name = name

    @property
    def type(self) -> str:
        """Gets the type of this Cluster.


        :return: The type of this Cluster.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Cluster.


        :param type: The type of this Cluster.
        :type type: str
        """
        allowed_values = ["website-stack", "authors"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type