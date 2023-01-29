import base64
import requests
import json


str = '4psiZ6Bef5ZQ80UPhIlrXODa3:d4wMmIwjTrpkrpxnNgquizKsdLedeMV5M56hiw4dKrD5Qbplbh'
b = str.encode("ascii")
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
query = "%23rareDisease"
query = "%23kleefstrasyndrome%20OR%20kleefstrasyndrome"
url = f"https://api.twitter.com/2/tweets/search/all?tweet.fields={tweet_fields}&expansions={expansions}&place.fields={place_fields}&user.fields={user_fields}&query={query}"

payload = {}
headers = {
    'Authorization': f'Bearer {bearer}',
    #  'Cookie': 'guest_id=v1%3A167292706625677604'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)

print(json.loads(response.text)['meta'])
print(json.loads(response.text)['includes'])

for el in json.loads(response.text)['data']:
    print(el)
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
