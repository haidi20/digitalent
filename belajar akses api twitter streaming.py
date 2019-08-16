# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 09:23:04 2019

@author: haidinata
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ACCESS_TOKEN = "1152833421753741317-BaJASyd73iTsfdLSwgJAR8zD14b03R"
ACCESS_SECRET = "jS3j6vi7hnew6RDFqlm6MJlNT81oaxqXGfe27SGTiOwjw"
CONSUMER_KEY = "giB9h62VkBjbY2Dd2WHQT1JJB"
CONSUMER_SECRET = "YssKW7sJqSdwV4eiQYssc8nPgaP9qo5Jv16PnQgPlyLvXUaBl0" 

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

class MyListener(StreamListener):
    
    def on_data(self, data):
        #print(data)
        for item in data:
            print(item.created_at)
        try:
            #with open('laravel.json', 'a') as f:
            print(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    
    def on_error(self, status):
        print(status)
        return True
    
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#laravel'])
print(twitter_stream)