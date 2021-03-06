# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Evaluation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, type_id: int=None, type_name: str=None, value: int=None):  # noqa: E501
        """Evaluation - a model defined in Swagger

        :param type_id: The type_id of this Evaluation.  # noqa: E501
        :type type_id: int
        :param type_name: The type_name of this Evaluation.  # noqa: E501
        :type type_name: str
        :param value: The value of this Evaluation.  # noqa: E501
        :type value: int
        """
        self.swagger_types = {
            'type_id': int,
            'type_name': str,
            'value': int
        }

        self.attribute_map = {
            'type_id': 'type_id',
            'type_name': 'type_name',
            'value': 'value'
        }

        self._type_id = type_id
        self._type_name = type_name
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Evaluation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Evaluation of this Evaluation.  # noqa: E501
        :rtype: Evaluation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type_id(self) -> int:
        """Gets the type_id of this Evaluation.


        :return: The type_id of this Evaluation.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id: int):
        """Sets the type_id of this Evaluation.


        :param type_id: The type_id of this Evaluation.
        :type type_id: int
        """

        self._type_id = type_id

    @property
    def type_name(self) -> str:
        """Gets the type_name of this Evaluation.


        :return: The type_name of this Evaluation.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name: str):
        """Sets the type_name of this Evaluation.


        :param type_name: The type_name of this Evaluation.
        :type type_name: str
        """

        self._type_name = type_name

    @property
    def value(self) -> int:
        """Gets the value of this Evaluation.


        :return: The value of this Evaluation.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value: int):
        """Sets the value of this Evaluation.


        :param value: The value of this Evaluation.
        :type value: int
        """

        self._value = value
