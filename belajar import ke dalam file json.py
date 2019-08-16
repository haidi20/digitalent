# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:17:24 2019

@author: haidinata
"""

import tweepy
import csv
import codecs
import json
import pandas as pd

ACCESS_TOKEN = "1152833421753741317-BaJASyd73iTsfdLSwgJAR8zD14b03R"
ACCESS_SECRET = "jS3j6vi7hnew6RDFqlm6MJlNT81oaxqXGfe27SGTiOwjw"
CONSUMER_KEY = "giB9h62VkBjbY2Dd2WHQT1JJB"
CONSUMER_SECRET = "YssKW7sJqSdwV4eiQYssc8nPgaP9qo5Jv16PnQgPlyLvXUaBl0"

def connect_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    
    api = tweepy.API(auth)
    return api


    
api = connect_twitter_OAuth()
public_tweets = api.home_timeline()
f = csv.writer(open("texts.csv", "wb+"))

for tweet in public_tweets:
    text = tweet._json
    text = text['text'],'\n'
    
    try:
        with open('texts.csv', 'a') as f:
            json.dump(text, f)
    
    except BaseException as e:
        print("Error on_data: %s" % str(e))

    
   
        
    #print(data['entities']['url']['urls'][0]['url'])

#for tweet in public_tweets:
    #data = tweet.user._json
    
    #try:
        #with open('tweets.json', 'a') as f:
            #json.dump(data, f)
    
    #except BaseException as e:
        #print("Error on_data: %s" % str(e))
    
    

        
    