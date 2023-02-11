import base64
import random
import time

import requests
import json

str_token = '4psiZ6Bef5ZQ80UPhIlrXODa3:d4wMmIwjTrpkrpxnNgquizKsdLedeMV5M56hiw4dKrD5Qbplbh'
b = str_token.encode("ascii")
basic = base64.b64encode(b).decode('ascii')
url = f"https://api.twitter.com/oauth2/token?grant_type=client_credentials"
headers = {
    'Authorization': f'Basic {basic}'
}
print(headers)
response = requests.request("POST", url, headers=headers)
print(response.status_code)
print(response.text)
if response.status_code != 200:
    raise Exception("Status code of autentication is not 200")
bearer = json.loads(response.text)['access_token']

tweet_fields = "attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld"
expansions = "geo.place_id,author_id,referenced_tweets.id,in_reply_to_user_id,referenced_tweets.id.author_id"
place_fields = "contained_within,country,country_code,full_name,geo,id,name,place_type"
user_fields = "created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username"
# query = "%23rareDisease"
start_time = '2006-05-01T00:00:01Z'
#"%20OR%20".join(
query_parms = ["%23RareDisease", "%23raredisorder", "%23neurodevelopmentaldisorder", "%23NDD", "%23developmentaldisability",
     "%23intellectualdisability",
     "%23intellectualdisorder", "%23kleefstra", "%23kleefstrasyndrome", "%23EHMT1", "%23SETD1A", "%23STXBP1", "%23SYT1",
     "%23KMT2D",
     "%23KAT6A", "%23KAT6Asyndrome", "%23foxg1", "%23FOXG1", "%23KBGSyndrome", "%23KdVS", "%23KoolendeVriesSyndrome",
     "%23WSS",
     "%23WiedemannSteinersyndrome", "%23kabuki", "%23KabukiSyndrome", "%23kabukisyndrome", "%23Rettsyndrome",
     "%23Angelman",
     "%23AngelmanSyndrome", "%23PhelanLucky", "%23phelanmcdermid", "%23PhelanMcDermid", "%23FragileX", "%23FX",
     "%23PittHopkins",
     "%23PraderWilliSyndrome", "%23PraderWilli", "%23PWS", "%23geneticdisease", "%23genetics", "%23genetherapy",
     "%23GeneTherapy",
     "%23cellandgenetherapy", "%23biotech", "%23clinicaltrials", "%23Clinical", "%23Therapeutics", "%23mRNA",
     "%23genome", "%23IPSC",
     "%23OrphanDrug", "%23RareMedicine", "%23RareDrug", "%23drugdiscovery", "%23rarediseasetreatment",
     "%23RareChampions", "%23ChampionsInRare",
     "%23CareAboutRare", "%23RareAsOne", "%23RareBarometer", "%23DareToThinkRare", "%23rarediseaseeducation",
     "%23rareadvocacy",
     "%23patientadvocacy", "%23RareAdvocacy", "%23WeareRARE", "%23WeAreRare", "%23LivingRare", "%23livingrare",
     "%23rare360", "%23RareActivists",
     "%23CommunityBased", "%23RareAction", "%23rarediseaseawareness", "%23patientstory", "%23rarestories",
     "Rare Disease",
     "rare disorder", "neurodevelopmental disorder", "NDD", "developmental disability", "intellectual disability",
     "intellectual disorder", "Kleefstra", "Kleefstra syndrome", "EHMT1", "SETD1A", "STXBP1", "SYT1", "KMT2D", "KAT6A",
     "KAT6A syndrome",
     "foxg1", "FOXG1", "KBG Syndrome", "KdVS", "Koolen-de Vries syndrome", "WSS", "Wiedemann Steiner syndrome",
     "kabuki",
     "Kabuki Syndrome", "Rett Syndrome", "Angelman", "Angelman syndrome", "Phelan-McDermid Syndrome", "Fragile X",
     "Pitt Hopkins syndrome",
     "Prader-Willi Syndrome", "genetic disease", "genetics", "gene therapy", "biotech",
     "clinical trials",
     "mRNA", "genome", "IPSC", "orphan drug", "rare medicine", "rare drug", "drug discovery", "rare disease treatment"]

# query = "%23kleefstrasyndrome%20OR%20kleefstra syndrome"
# query = "%23kleefstrasyndrome"
for query_parm in query_parms:
    url = f"https://api.twitter.com/2/tweets/search/all?tweet.fields={tweet_fields}&expansions={expansions}&place.fields={place_fields}&user.fields={user_fields}&start_time={start_time}&query={query_parm}&max_results=100"

    next_tokens = [None]

    while len(next_tokens) != 0:
        next_token = next_tokens.pop()
        payload = {}
        headers = {
            'Authorization': f'Bearer {bearer}',
            #  'Cookie': 'guest_id=v1%3A167292706625677604'
        }
        print(query_parm)
        if next_token is not None:
            url = f"https://api.twitter.com/2/tweets/search/all?tweet.fields={tweet_fields}&expansions={expansions}&place.fields=" \
                  f"{place_fields}&user.fields={user_fields}&start_time={start_time}&query={query_parm}&max_results=100&next_token={next_token}"
        response = requests.request("GET", url, headers=headers, data=payload)
        print(url)
        print(next_tokens)
        time.sleep(random.randint(2, 5))

        data = response.json()

        if 'next_token' in data['meta']:
            next_tokens.append(data['meta']['next_token'])
        t = time.time()
        t_ms = int(t * 1000)
        time.sleep(0.01)
        with open('./../../twiteer/' + str(query_parm) + '_' + str(t_ms) + '_' + str(random.randint(1, 999)) + ".txt", "x") as f:
            f.write(json.dumps(data))

    # for el in data['data']:
    #    print(el)
    # print(json.loads(response.text)['meta'])
    # print(json.loads(response.text)['includes'])

# print(response.text)


# import tweepy
#
# # API credentials here
# consumer_key = 'zjI7NAsQ9rSbkR1xjbK8zhgrq'
# consumer_secret = 'Npd0NbD8SaSPDGSo9Bdi2tMpRnBIgoY4TMEXFPWPf5issYlXpn'
# access_token = '2190052255-xEnWT5Ej0VMKCaHv4fvcQAHSdxYUsTWqv4Iz3mi'
# access_token_secret = 'HJQ6YHjSIOXOAtUAX2QpujjG7FSHA2FQqgpcUsiXorJ8D'
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth,wait_on_rate_limit=True)
#
# searchString = "iPhone"
#
# cursor = tweepy.Cursor(api.search_full_archive, q=searchString, count=20, lang="en", tweet_mode='extended')
#
# maxCount = 1
# count = 0
# for tweet in cursor.items():
#     print()
#     print("Tweet Information")
#     print("================================")
#     print("Text: ", tweet.full_text)
#     print("Geo: ", tweet.geo)
#     print("Coordinates: ", tweet.coordinates)
#     print("Place: ", tweet.place)
#     print()
#
#     print("User Information")
#     print("================================")
#     print("Location: ", tweet.user.location)
#     print("Geo Enabled? ", tweet.user.geo_enabled)
#
#     count = count + 1
#     if count == maxCount:
#         break;
