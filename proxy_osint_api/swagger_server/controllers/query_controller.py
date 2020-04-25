import connexion
import six

from swagger_server.models.query_object import QueryObject  # noqa: E501
from swagger_server.models.query_response import QueryResponse  # noqa: E501
from swagger_server import util


def quary(body):  # noqa: E501
    """Queries an external service to build information about a case file

     # noqa: E501

    :param body: The query object
    :type body: dict | bytes

    :rtype: QueryResponse
    """
    if connexion.request.is_json:
        body = QueryObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
