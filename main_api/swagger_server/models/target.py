# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Target(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, website: str=None, strategy: str=None, reload: str=None):  # noqa: E501
        """Target - a model defined in Swagger

        :param id: The id of this Target.  # noqa: E501
        :type id: int
        :param website: The website of this Target.  # noqa: E501
        :type website: str
        :param strategy: The strategy of this Target.  # noqa: E501
        :type strategy: str
        :param reload: The reload of this Target.  # noqa: E501
        :type reload: str
        """
        self.swagger_types = {
            'id': int,
            'website': str,
            'strategy': str,
            'reload': str
        }

        self.attribute_map = {
            'id': 'id',
            'website': 'website',
            'strategy': 'strategy',
            'reload': 'reload'
        }

        self._id = id
        self._website = website
        self._strategy = strategy
        self._reload = reload

    @classmethod
    def from_dict(cls, dikt) -> 'Target':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Target of this Target.  # noqa: E501
        :rtype: Target
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Target.


        :return: The id of this Target.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Target.


        :param id: The id of this Target.
        :type id: int
        """

        self._id = id

    @property
    def website(self) -> str:
        """Gets the website of this Target.


        :return: The website of this Target.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website: str):
        """Sets the website of this Target.


        :param website: The website of this Target.
        :type website: str
        """

        self._website = website

    @property
    def strategy(self) -> str:
        """Gets the strategy of this Target.


        :return: The strategy of this Target.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: str):
        """Sets the strategy of this Target.


        :param strategy: The strategy of this Target.
        :type strategy: str
        """

        self._strategy = strategy

    @property
    def reload(self) -> str:
        """Gets the reload of this Target.

        How often to reload this  # noqa: E501

        :return: The reload of this Target.
        :rtype: str
        """
        return self._reload

    @reload.setter
    def reload(self, reload: str):
        """Sets the reload of this Target.

        How often to reload this  # noqa: E501

        :param reload: The reload of this Target.
        :type reload: str
        """
        allowed_values = ["daily", "hourly", "weekly"]  # noqa: E501
        if reload not in allowed_values:
            raise ValueError(
                "Invalid value for `reload` ({0}), must be one of {1}"
                .format(reload, allowed_values)
            )

        self._reload = reload
