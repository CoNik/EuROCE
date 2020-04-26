import connexion
import six
import datetime
from swagger_server.models.case_file import CaseFile  # noqa: E501
from swagger_server.models.dashboard_statistics import DashboardStatistics  # noqa: E501
from swagger_server import util

queries=0;
queue=0;

def get_case_file(UUID):  # noqa: E501
    """Retrieves a specific case file from its UUID

     # noqa: E501

    :param UUID: The case file UUID
    :type UUID: str

    :rtype: CaseFile
    """
    global queries;
    queries = queries + 1;

    return str(queries)


def get_dashboard_stats():  # noqa: E501
    """Returns the dashboard statistics

     # noqa: E501


    :rtype: DashboardStatistics
    """
    
    global queries;
    queries = queries + 1;

    last_monday = datetime.datetime.now()-datetime.timedelta(days=datetime.datetime.now().weekday());
    last_monday_at_nine = datetime.datetime(last_monday.year, last_monday.month, last_monday.day, 9, 0);

    passed_time = datetime.datetime.now() - last_monday_at_nine;
    passed_seconds = passed_time.total_seconds();

    social_media_links=182+int(passed_seconds*20000/604800);
    social_media_links_diff=2+int(passed_seconds*10/604800);

    article_links=783+int(passed_seconds*30000/604800);
    article_links_diff=3+int(passed_seconds*7/604800);

    content_rewiew_tasks=15+int(passed_seconds*1000/604800)+queue;
    content_rewiew_tasks_diff=2+int(passed_seconds*5/604800);

    potential_fake_news_sites=87+int(passed_seconds*1000/604800)+queue;
    potential_fake_news_sites_diff=10+int(passed_seconds*14/604800);

    indexed_sites=145+int(passed_seconds*2000/604800)+queue;
    indexed_sites_diff=5+int(passed_seconds*10/604800);

    indexed_articles_month=7830+int(passed_seconds*50000/604800)+queue;
    indexed_articles_month_diff=15+int(passed_seconds*20/604800);

    stats = DashboardStatistics(time=datetime.datetime.now(), social_media_links=social_media_links, social_media_links_diff=social_media_links_diff, article_links=article_links, article_links_diff=article_links_diff, content_rewiew_tasks=content_rewiew_tasks, content_rewiew_tasks_diff=content_rewiew_tasks_diff, potential_fake_news_sites=potential_fake_news_sites, potential_fake_news_sites_diff=potential_fake_news_sites_diff, indexed_sites=indexed_sites, indexed_sites_diff=indexed_sites_diff, indexed_articles_month=indexed_articles_month, indexed_articles_month_diff=indexed_articles_month_diff);

    return stats;


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

    global queries;
    queries = queries + 1;

    return 'do some magic!'


def find_case_files(url):  # noqa: E501
    """Request opening a case file based on a website URL

     # noqa: E501

    :param url: URL to submit
    :type url: str

    :rtype: None
    """

    global queries;
    queries = queries + 1;

    global queue;
    queue = queue + 1;

    return "We have currently %s case files in queue" % queue
