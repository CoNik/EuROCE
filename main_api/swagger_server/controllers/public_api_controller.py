import connexion
import six

from swagger_server.models.case_file import CaseFile  # noqa: E501
from swagger_server.models.dashboard_statistics import DashboardStatistics  # noqa: E501
from swagger_server import util


def find_case_files(url):  # noqa: E501
    """Request opening a case file based on a website URL

     # noqa: E501

    :param url: URL to submit
    :type url: str

    :rtype: None
    """
    return 'do some magic!'


def get_case_file(UUID):  # noqa: E501
    """Retrieves a specific case file from its UUID

     # noqa: E501

    :param UUID: The case file UUID
    :type UUID: str

    :rtype: CaseFile
    """
    return 'do some magic!'


def get_dashboard_stats():  # noqa: E501
    """Returns the dashboard statistics

     # noqa: E501


    :rtype: DashboardStatistics
    """
    return 'do some magic!'


def search_case_files(tags=None, hostnames=None, geos=None):  # noqa: E501
    """Search existing case files based on a specific parameter

     # noqa: E501

    :param tags: Tags to filter by
    :type tags: List[str]
    :param hostnames: Hostnames to filter by
    :type hostnames: List[str]
    :param geos: Geography to filter by
    :type geos: List[str]

    :rtype: List[CaseFile]
    """
    return 'do some magic!'
