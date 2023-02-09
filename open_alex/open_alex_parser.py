import json
import random

from elasticsearch import Elasticsearch, helpers
import configparser
import requests
import sys
from datetime import datetime, timedelta

es = Elasticsearch("http://localhost:9200", basic_auth=('elastic', 'changeme'))
es.info().body

DATE_FORMAT = '%Y-%m-%d'

d = '2001-01-01'
cursor = '*'

cursors = ['*']

# Concept: Rare disease
# https://explore.openalex.org/concepts/C2779701055?fbclid=IwAR1XsGpzoDUdNsGQSIvYkZ8tCxPQLM83PURw1IvVth6o0wRx_pp8C-9Q8CM
# Concept: Gene expression
# https://explore.openalex.org/concepts/C150194340
# Concept: Genetic variation
# https://explore.openalex.org/concepts/C68873052
# Concept: Genetics
# https://explore.openalex.org/concepts/C54355233
# Concept: Orphan drug
# https://explore.openalex.org/concepts/C75480439
# Concept: Neurodevelopmental disorder
# https://explore.openalex.org/concepts/C2779388368
# Concept: Congenital disorder
# https://explore.openalex.org/concepts/C2779778371
# Concept: Patient advocacy
# https://explore.openalex.org/concepts/C2777471088
# Concept: Intellectual disability
# https://explore.openalex.org/concepts/C551499885
# Concept: Drug discovery
# https://explore.openalex.org/concepts/C74187038
# rare syndrome # curare # gene # angelsman
concepts = '%7C'.join(['C2779701055', 'C150194340', 'C68873052', 'C54355233', 'C75480439', 'C2779388368',
                       'C2779778371', 'C2777471088', 'C551499885', 'C74187038'])
import time
while cursors != 0:
    c = cursors.pop()
    url = f'https://api.openalex.org/works?filter=concepts.id%3A{concepts}%2Cfrom_publication_date%3A{d}&per_page=200&cursor={c}'
    x = requests.get(url)
    result = x.json()
    records = result['results']
    cursors.append(result['meta']['next_cursor'])
    t = time.time()
    print(cursors)
    t_ms = int(t * 1000)
    time.sleep(0.01)
    with open('./../../openalex/'+str(t_ms)+'_'+str(random.randint(1, 999))+".txt", "x") as f:
        f.write(json.dumps(result))

    for record in records:
        # print(record)
        es.index(index="open-alex-extended",
                 id=record['id'],
                 document={'id': record['id'],
                           'title': record['title'],
                           'display_name': record['display_name']})

config = configparser.ConfigParser()
config.read('example.ini')


def parse_input(args):
    dates = []
    if len(args) == 2 and args[0] == '-date':
        date = args[1]
        d = datetime.strptime(date, DATE_FORMAT)
        dates.append(d.strftime('%Y%m%d'))
    elif len(args) == 3 and args[0] == '-date-range':
        start_date = args[1]
        end_date = args[2]
        base = datetime.strptime(start_date, DATE_FORMAT)
        end_base = datetime.strptime(end_date, DATE_FORMAT)
        numdays = (end_base - base).days + 1
        date_list = [(base + timedelta(days=x)).strftime(DATE_FORMAT) for x in range(numdays)]
        dates.extend(date_list)
    return dates


if __name__ == "__main__":
    args = sys.argv[1:]
    dates = parse_input(args)
