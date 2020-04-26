import connexion
import six

from swagger_server.models.case_file import CaseFile  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def edit_case_file(UUID, body):  # noqa: E501
    """Changes the properties of a specific case file

     # noqa: E501

    :param UUID: The case file UUID
    :type UUID: str
    :param body: Updated user object
    :type body: dict | bytes

    :rtype: CaseFile
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return flask.Response(status=403)
