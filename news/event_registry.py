from elasticsearch import Elasticsearch
from eventregistry import *


es = Elasticsearch("http://localhost:9200", basic_auth=('elastic', 'changeme'), timeout=60, max_retries=10, retry_on_timeout=True)
es.info().body

MAX_RESULTS = 1000
er = EventRegistry(apiKey="c1798dd5-db16-458e-8b55-8ce6d5a336f1")
iter = QueryArticlesIter(
    keywords=QueryItems.OR(
        ['9q34 deletion syndrome', 'Kleefstra syndrome', 'Syndrome de Kleefstra', 'Kleefstra syndrom',
         'Síndrome de Kleefstra', 'Sindrome di Kleefstra', 'Kleefstra syndroom', 'Kleefstra sindrom',
         'Angelman syndrome', 'Dravet syndrome', 'Syndrome de Dravet', 'Cornelia de Lange syndrome',
         'Cornelia de Lange Syndrome', 'Phelan-McDermid syndrome', 'Fragile X syndrome',
         '[Pitt-Hopkins syndrome', 'Prader-Willi syndrome', 'FOXG1 syndrome', 'Syndrome de FOXG1',
         'FOXG1 syndrom', 'Síndrome de FOXG1', 'Sindrome di FOXG1', 'FOXG1 syndroom', 'FOXG1 sindrom',
         'Koolen-de Vries syndrome', 'Syndrome de Koolen-de Vries','Koolen-de Vries syndrom',
         'Síndrome de Koolen-de Vries', 'Sindrome di Koolen-de Vries', 'Koolen-de Vries syndroom',
         'Koolen-de Vries sindrom','Wiedemann-Steiner syndrome','Kabuki syndrome', 'Rett syndrome',
         'SYNGAP1 syndrome','Syndrome de SYNGAP1','SYNGAP1 syndrom','Síndrome de SYNGAP1','Sindrome di SYNGAP1',
         'SYNGAP1 syndroom','SYNGAP1 sindrom', 'SATB2 syndrome','Syndrome de SATB2',
         'SATB2 syndrom', 'Síndrome de SATB2', 'Sindrome di SATB2','SATB2 syndroom','SATB2 sindrom',
          'CTNNB1 syndrome', 'Syndrome de CTNNB1', 'CTNNB1 syndrom', 'Síndrome de CTNNB1','Sindrome di CTNNB1',
         'CTNNB1 syndroom','CTNNB1 sindrom'
         ]))
#
# [Angelman syndrome]
# [Dravet syndrome] OR [Syndrome de Dravet]
# [Cornelia de Lange syndrome] OR [Cornelia de Lange Syndrome]
# [Phelan-McDermid syndrome]
# [Fragile X syndrome]
# [Pitt-Hopkins syndrome]
# [Prader-Willi syndrome]
# FOXG1 syndrome OR Syndrome de FOXG1 OR FOXG1 syndrom OR Síndrome de FOXG1 OR Sindrome di FOXG1 OR FOXG1 syndroom OR FOXG1 sindrom
# Koolen-de Vries syndrome OR Syndrome de Koolen-de Vries OR Koolen-de Vries syndrom OR Síndrome de Koolen-de Vries OR Sindrome di Koolen-de Vries OR Koolen-de Vries syndroom OR Koolen-de Vries sindrom
# [Wiedemann-Steiner syndrome] OR Wiedemann Steiner syndrome (in text) OR Wiedemann Steiner syndrome (in body)
# [Kabuki syndrome] and keyword??
# [Rett syndrome]
# SYNGAP1 syndrome OR Syndrome de SYNGAP1 OR SYNGAP1 syndrom OR Síndrome de SYNGAP1 OR Sindrome di SYNGAP1 OR SYNGAP1 syndroom OR SYNGAP1 sindrom
# SATB2 syndrome OR Syndrome de SATB2 OR SATB2 syndrom OR Síndrome de SATB2 OR Sindrome di SATB2 OR SATB2 syndroom OR SATB2 sindrom
# CTNNB1 syndrome OR Syndrome de CTNNB1 OR CTNNB1 syndrom OR Síndrome de CTNNB1 OR Sindrome di CTNNB1 OR CTNNB1 syndroom OR CTNNB1 sindrom
for record in iter.execQuery(er,
                          sortBy="date"):
    # do something with the article
    print(record)
    es.index(index="news-er",
             id=record['uri'],
             document=record)
    # break
