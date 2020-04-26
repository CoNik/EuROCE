import connexion
import six
import datetime
import flask
from swagger_server.models.query_object import QueryObject  # noqa: E501
from swagger_server.models.query_response import QueryResponse  # noqa: E501
from swagger_server.models.evaluation import Evaluation
from typing import List, Dict  # noqa: F401
from swagger_server import util

from swagger_server.github_downloader import covid_blacklist

def query(body):  # noqa: E501
    """Queries an external service to build information about a case file

     # noqa: E501

    :param body: The query object
    :type body: dict | bytes

    :rtype: QueryResponse
    """
    if connexion.request.is_json:
        query = QueryObject.from_dict(connexion.request.get_json())  # noqa: E501

        if not query.fqdn or query.fqdn == '':
            return flask.Response(status=400)
        elif query.fqdn in covid_blacklist:
            evaluations = [Evaluation(type_id=1, type_name='malware-classification', value=covid_blacklist[query.fqdn])]
            response = QueryResponse(datetime.datetime.now(), source_api='https://github.com/qcri/COVID19-MAL-Blacklist', evaluations=evaluations)

            return response
        else:
            return flask.Response(status=404)
    else:
        return flask.Response(status=400)
