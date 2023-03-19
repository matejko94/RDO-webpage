import json
from os import listdir
from os.path import isfile, join

from elasticsearch import Elasticsearch

# mypath='/home/matejs/rare_desises/twiteer'
mypath = '/home/matej/Desktop/twitter'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

es = Elasticsearch("http://localhost:9200", basic_auth=('elastic', 'changeme'), timeout=60, max_retries=10,
                   retry_on_timeout=True)
es.info().body
for onlyfiles in onlyfiles:
    with open(mypath + '/' + onlyfiles) as f:
        data = json.loads(f.read())
        if 'data' in data:
            for d in data['data']:
                print(d)
                es.update(index="twiter",
                          id=d.get('id'),
                          doc= {'id': d.get('id'),
                              'text': d.get('text'),
                              'edit_history_tweet_ids': d.get('edit_history_tweet_ids'),
                              'conversation_id': d.get('conversation_id'),
                              'lang': d.get('lang'),
                              'reply_settings': d.get('reply_settings'),
                              'author_id': d.get('author_id'),
                              'created_at': d.get('created_at'),
                              'public_metrics': d.get('public_metrics')},
                          doc_as_upsert= True)
