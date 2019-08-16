# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:20:24 2019

@author: haidinata
"""

import pandas as pd

array = pd.read_json('tweets.json')
array2 = pd.read_json('data.json')
#file_json = pd.read_json(codecs.open('tweets.json','r','utf-8'))
#file_json = pd.read_json(open("tweets.json", "r", encoding="utf8"), lines=True)

print(array[1])
    
#print(array2)