import tweepy
import sqlite3 as sql
import credentials
import pandas as pd

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

db_connect = sql.connect('tweets.db')

db_cursor = db_connect.cursor()
# Create table
db_cursor.execute('''CREATE TABLE IF NOT EXISTS tweets
               (tweet_text TEXT)''')


# # Insert a row of data
# db_cursor.execute("INSERT INTO stocks VALUES ({})".format(tweets))

# # Save (commit) the changes
# db_connect.commit()
#
# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# db_connect.close()

# tweets_file = pd.read_csv('tweets_data.csv')


# def create_url(query):
#     url = 'https://api.twitter.com/2/tweets/search/recent?query={}&max_results=100&tweet.fields=created_at,geo,id,lang,public_metrics,source,text&expansions=attachments.poll_ids,attachments.media_keys,author_id,geo.place_id,in_reply_to_user_id,referenced_tweets.id,entities.mentions.username,referenced_tweets.id.author_id&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld'.format(
#         query
#     )
#     return url


def auth():
    return credentials.auth_cred


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.limit = 50

    def on_status(self, status):

        tweet_text = None
        print("_______")

        try:
            if hasattr(status, 'retweeted_status') and hasattr(status.retweeted_status, 'extended_tweet'):
                print('retweeted: ' + status.retweeted_status.extended_tweet['full_text'])
                tweet_text = status.retweeted_status.extended_tweet['full_text']

            if hasattr(status, 'extended_tweet'):
                print('extended_tweet: ' + status.extended_tweet['full_text'])
                tweet_text = status.extended_tweet['full_text']
            else:
                print('text: ' + status.text)
                tweet_text = status.text

            # Insert a row of data
            db_cursor.execute("""INSERT INTO tweets VALUES (?)""",(tweet_text,))
            db_connect.commit()
        except AttributeError:
            print('attribute error: ' + status.text)

        self.counter += 1
        if self.counter < self.limit:
            return True
        else:
            myStream.disconnect()

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


# def create_headers(bearer_token):
#     headers = {"Authorization": "Bearer {}".format(bearer_token)}
#     return headers
#
#
# def connect_to_endpoint(url, headers):
#     response = requests.request("GET", url, headers=headers)
#     print(response.status_code)
#     if response.status_code != 200:
#         raise Exception(response.status_code, response.text)
#     return response.json()
#
#
# def search_tweets_v2(query):
#     bearer_token = auth()
#     url = create_url(query)
#     headers = create_headers(bearer_token)
#     json_response = connect_to_endpoint(url, headers)
#     return json_response
#
#
# def search_tweets(query, count=400):
#     tweets_dum = tweepy.Cursor(api.search, query, count=count,
#                            tweet_mode="extended").items(count)
#     return [tweet._json for tweet in tweets_dum]
#     # return api.search(q=query, count=100, tweet_mode="extended")


if __name__ == '__main__':
    # public_tweets = api.home_timeline()
    # trending_topics = api.trends_available()
    # for tweet in public_tweets:
    #     print(tweet.text)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, tweet_mode='extended')
    live_feed = myStream.filter(track=['#tesla', '#ev', '#electricvehicles'])

    # tweets_dum = search_tweets('covid')
    # print(type(tweets_dum))
    # for tweet in tweets_dum:
    #     print(tweet["full_text"])
