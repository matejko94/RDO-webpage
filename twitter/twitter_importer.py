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
        for d in data['data']:
            print(d)
            es.update(index="twiter",
                      id=d['id'],
                      doc= {'id': d['id'],
                          'text': d['text'],
                          'edit_history_tweet_ids': d['edit_history_tweet_ids'],
                          'conversation_id': d['conversation_id'],
                          'lang': d['lang'],
                          'reply_settings': d['reply_settings'],
                          'author_id': d['author_id'],
                          'created_at': d['created_at'],
                          'public_metrics': d['public_metrics']},
                      doc_as_upsert= True)
