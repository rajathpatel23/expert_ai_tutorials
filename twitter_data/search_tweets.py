from twitter import api
from twitter.parse_tweet import ParseTweet
from twitter.models import Trend, TwitterModel
import os
import twitter
import pdb
import requests
import json


access_token = os.environ.get("TWEET_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWEET_ACCESS_SECRET")
consumer_key = os.environ.get("TWEET_CONSUMER_KEY")
consumer_secret = os.environ.get("TWEET_CONSUMER_SECRET")
bearer_token_val = os.environ.get("BEARER_TOKEN")


# api = twitter.Api(consumer_key=consumer_key, 
# consumer_secret=consumer_secret,
# access_token_key=access_token,
# access_token_secret=access_token_secret)


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def get_rules(headers, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}):{}".format(response.status_code,
            response.text)
        )
    print(json.dumps(response.json()))
    return response.json()

def delete_all_rules(headers, bearer_token, rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(headers, delete, bearer_token):
    # You can adjust the rules if needed
    sample_rules = [
        {"value": "#APPL -lang:en has:hashtags"
        # "tag": "Apple Stock price"
        }
        # {"value": "cat has:images -grumpy", "tag": "cat pictures"},
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(headers, set, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", headers=headers, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))


def main():
    bearer_token = os.environ.get("BEARER_TOKEN")
    headers = create_headers(bearer_token)
    rules = get_rules(headers, bearer_token)
    delete = delete_all_rules(headers, bearer_token, rules)
    set = set_rules(headers, delete, bearer_token)
    get_stream(headers, set, bearer_token)

if __name__ == '__main__':
    main()

# pdb.set_trace()

# statuses = api.GetSearch(
#     raw_query="q=twitter%20&result_type=recent&since=2021-01-05&count=100"
# )
# for tweet in statuses:
#     print(tweet.text)



