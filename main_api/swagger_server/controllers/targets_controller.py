import connexion
import six

from swagger_server.models.target import Target  # noqa: E501
from swagger_server import util


def delete_targets(targetID):  # noqa: E501
    """Changes the properties of a specific target

     # noqa: E501

    :param targetID: ID of target to delete
    :type targetID: int

    :rtype: None
    """
    return flask.Response(status=403)


def edit_target(targetID, body):  # noqa: E501
    """Changes the properties of a specific target

     # noqa: E501

    :param targetID: ID of target to change
    :type targetID: int
    :param body: Updated target object
    :type body: dict | bytes

    :rtype: Target
    """
    if connexion.request.is_json:
        body = Target.from_dict(connexion.request.get_json())  # noqa: E501
    return flask.Response(status=403)


def get_target_by_id(targetID):  # noqa: E501
    """Gets the target based on its ID

     # noqa: E501

    :param targetID: ID of target to return
    :type targetID: int

    :rtype: Target
    """
    return flask.Response(status=403)
