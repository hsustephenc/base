import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
# bearer_token = os.environ.get("BEARER_TOKEN")

# twitter API explorer is here
# https://developer.twitter.com/apitools/api

bearer_token = "AAAAAAAAAAAAAAAAAAAAAG7TeQEAAAAAyv840LrguvhtqsE3hlE1J9Q9atg%3DSLIwYB3hamejVpgd0d8RHypxeGVuFBdzhg16zYtecASFHbIJPe"
search_url = "https://api.twitter.com/2/tweets/search/recent"
 
# search_url = "https://api.twitter.com/2/tweets/search/all?max_results=25" 
 
# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields

query_params = {'query': '(from:hsustephenc is:retweet)','tweet.fields':['created_at']}

def bearer_oauth(r):

    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"

    return r


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
#    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()