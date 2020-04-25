import urllib.request

covid_blacklist = {}

with urllib.request.urlopen('https://raw.githubusercontent.com/qcri/COVID19-MAL-Blacklist/master/blacklist/covid19mal_latest.csv') as response:
    latest = response.read().decode('utf-8');

    first = True

    for line in latest.split('\n'):
        if first:
            first = False
        else:
            split_line = line.split(' ')

            if len(split_line) == 2:
                covid_blacklist[split_line[0]] = int(float(split_line[1]));
