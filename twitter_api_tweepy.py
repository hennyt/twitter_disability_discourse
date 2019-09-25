import os
import tweepy as tw
import pandas as pd
import csv
import re

"""
NAME: HENNY TASKER
COLLABORATOR: DENNY STARKS
"""
#read https://www.earthdatascience.org/courses/earth-analytics-python/using-apis-natural-language-processing-twitter/get-and-use-twitter-data-in-python/

consumer_key = 'yourkeyhere'
consumer_secret = 'yourkeyhere
access_token = 'yourkeyhere'
acces_token_secret = 'yourkeyhere'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_token_secret)
api = tw.API(auth, wait_on_rate_limit = True)

#Define the search term and the date_since date as variables
search_words = "disability OR everydaydisablism OR chronicpain OR fibromyalgia"
date_since = "2019-09-15"

#collect tweets
tweets = tw.Cursor(api.search,
                tweet_mode = "extended",
                q = search_words + "-filter:retweets",
                lang = "en",
                since = date_since).items(1000)

all_tweets = [[tweet.user.screen_name, tweet.user.location, tweet.full_text] for tweet in tweets]

tweet_text = pd.DataFrame(data=all_tweets,
                     columns=['user', "location", "text"])

export_csv = tweet_text.to_csv(r'tweepy_api_raw_tweets.csv', index = None, header = True)
