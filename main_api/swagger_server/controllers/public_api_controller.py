import connexion
import six
import datetime
import random
import flask
from swagger_server.models.case_file import CaseFile  # noqa: E501
from swagger_server.models.dashboard_statistics import DashboardStatistics  # noqa: E501
from swagger_server.models.cluster import Cluster  # noqa: E501
from swagger_server.models.tag import Tag  # noqa: E501
from swagger_server import util

queries=0;
queue=0;

def get_random_casefile(random_int):
    gen=random.Random(random_int);

    random_urls=['maskanti-covid19.com', 'coronaviruschina.ml', 'anticovid-19.it', 'staysafecovid19.xyz', 'business-resource-facebook-covid-19.com', 'desinfectantes-covid19.com', 'zendesk-covid19.com', 'anticovid-19.co.uk', 'coronavirusprotection.io', 'covid19-medecinechinoise.ch', 'coronaviruspreventionkits.com', 'strongerthancoronavirus.com', 'covid19safety.shop', 'covid19taxreward.com', 'coronavirus-guidelines.online', 'covid19instatest.com', 'uberdoctorcoronavirus.com', 'ubercoronavirusprotection.com', 'againstcovid-19.com', 'coronavirusbeschermset.nl', 'cdc-gov.org', 'anti-covid19.fr', 'nocoronavirus.info', 'zendesk-covid19.net', 'stopcoronavirus.nl', 'byebyecoronavirus.com', 'coronavirusnewsnetwork.com', 'maskforcoronavirus.com', 'anticorona-virus.com', 'coronavirusfog.com', 'coronaviruspreppers.buzz', 'kabylie-stopcovid-19.com', 'zendesk-covid19.org', 'coronavirusconquerer.com', 'update-covid19.com', 'coronavirusgummy.com', 'aggiornadecretocovid19.online', 'coronaviruskingofbeers.com', 'covid19-products2020.com', 'covid19-testkit.net', 'coronavirusmaskpro.com.co', 'covid19.me.uk', 'bestmaskscoronavirus.com', 'anti-corona-virus.com', 'coronavirus-cure.store', 'terminixcovid19.com', 'coronavirus-total.ru', 'coronavirus-informations.online', 'covid-19-news.ru', 'coronavirusgen.com', 'italycovid-19.site', 'coronavirus2019.site', 'protectioncoronavirus.co.uk', 'runescape-covid-19.info', 'hmrc-refund-covid-19.com', 'coronavirushumano.org', 'n95coronavirusmaske.com', 'covid19-mask.com', 'securitycovid19.online', 'corona-virus-cure.xyz', 'covid19-symptoms.com', 'corona-virus-news.xyz', 'testcoronavirus.shop', 'covid19supply.ca', 'coronavirusmaskco.com', 'ent-covid19-gouv.info', 'coronavirusrations.co.uk', 'covid-19throatswab.com', 'anticovid19supply.com', 'examencoronavirus.cl', 'beatcovid19.co.uk', 'ameli-coronavirus.fr', 'recoverrryasitalycovid-19.xyz', 'netflix-coronavirus.com', 'desinfectantes-coronavirus.com', 'coronavirushealth.co', 'ameli-covid19.fr', 'promo-covid19-neftlix.ml', 'examencoronavirusadomicilio.cl', 'covid19-tests.info', 'bescherming-coronavirus.nl', 'coronavirusmart.com', 'safefromcovid-19.com', 'coronavirusrelief.net', 'cdc-coronavirus.com', 'coronavirusn95ppe.com', 'epidomacovid19.com', 'coronavirusapp.site', 'anticoronavirus.at', 'anti-covid19.shop', 'fuckcoronavirus.com', 'examenadomiciliocoronavirus.cl', 'theglobalcoronavirus.com', 'handsoapforcoronavirus.com', 'covid19tester.eu', 'covid-19comcast.org', 'covid19response.fund', 'thecovid19mask.co.za', 'coronavirusquicktests.com', 'facemask-coronavirus.com', 'covid-19donor.com', 'examencovid19.cl', 'coronavirusmasksuk.com', 'coronaviruspharma.com', 'mapacovid19.cl', 'covid-19comcast.com', 'united-kingdom-covid-19.com', 'coronavirustestkit.life', 'buycoronavirusfacemasks.com', 'coronavirus-19.lv', 'covid19crisis2020.com', 'sicurezza-covid19.com', 'bestmask-coronavirus.com', 'securitycovid19info.com', 'covid19masks.shop', 'covid-19cover.com', 'corona-virussafetymasks.com', 'covid-19facts.online', 'corona-virusss.com', 'viabcp-covid19.xyz', 'coronavirusinfor.world', 'coronavirus.uk', 'coronavirus19tests.com', 'hmrc-refund-covid19.com', 'coronavirus-apps.com', 'bell-covid19.com', 'coronacovid19information.online', 'coronavirusstatus.space', 'coronaviruspandemicessentials.com', 'shopcovid-19.com', 'verizoncovid-19.com', 'covid19-info.online', 'corona-virusapps.com', 'rogers-covid19.com', 'idscovid19.com', 'virys-covid19.ru', 'onavirus.cl']

    random_paths=['news?article=%s', 'explore/%s/link.html?update=1', 'link/referrer?hl=en&trk=%s', 'corona-exposed.html#link-%s', 'art/2020-04-23-%s.html', 'COVID/news?art=%s,fn=10387', 't/%s']

    random_clusters=[Cluster(id=4, name='fake-news-site', type='covid-misinformation'), Cluster(id=15, name='crypto-miner', type='malware-websites'), Cluster(id=12, name='extreme-content', type='covid-fake-cure'), Cluster(id=19, name='hidden-publisher', type='publicher-information')]

    random_tags=[Tag(name='miracolous-cure',id=193), Tag(name='malvertising',id=29), Tag(name='onlineshop-promotion',id=98), Tag(name='promoting_hatred',id=25), Tag(name='discrimination',id=23), Tag(name='institution-distrust',id=29), Tag(name='conspiracy-theory',id=27), Tag(name='extreme-content',id=100)]

    url="http://%s/%s" % (gen.choice(random_urls), gen.choice(random_paths) % gen.randint(1297,2804434));
    name="Case file #%s" % random_int
    clusters=gen.choices(random_clusters,k=gen.randint(0,2))
    tags=gen.choices(random_tags,k=gen.randint(2,5))

    return CaseFile(id=random_int, name=name, url=url, clusters=clusters, tags=tags);

def get_case_file(UUID):  # noqa: E501
    """Retrieves a specific case file from its UUID

     # noqa: E501

    :param UUID: The case file UUID
    :type UUID: str

    :rtype: CaseFile
    """
    global queries;
    queries = queries + 1;

    id_int=len(UUID)+102937

    try:
        id_int = int(UUID)
    except ValueError:
        id_int=sum(UUID.encode('utf-8'))+100000;

    return get_random_casefile(id_int);


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

    num=0;
    num = num + (len(tags) if tags != None else 0)
    num = num + (len(hostnames) if hostnames != None else 0)
    num = num + (len(geos) if geos != None else 0)

    gen=random.Random(num);
    found = 57 if num==0 else gen.randint(1,32)

    result=[]
    for item in range(found):
        num=num+1;
        result.append(get_random_casefile(num));

    return result


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
