# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 08:31:23 2019

@author: haidinata
"""

import tweepy
import json

ACCESS_TOKEN = "1152833421753741317-BaJASyd73iTsfdLSwgJAR8zD14b03R"
ACCESS_SECRET = "jS3j6vi7hnew6RDFqlm6MJlNT81oaxqXGfe27SGTiOwjw"
CONSUMER_KEY = "giB9h62VkBjbY2Dd2WHQT1JJB"
CONSUMER_SECRET = "YssKW7sJqSdwV4eiQYssc8nPgaP9qo5Jv16PnQgPlyLvXUaBl0"

def connect_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    
    api = tweepy.API(auth)
    return api

def process_or_store(tweet):
    print(json.dmps(tweet))
    
api = connect_twitter_OAuth()
public_tweets = api.home_timeline()
for tweet in public_tweets:
    location = tweet.user.location
    print(location)
    