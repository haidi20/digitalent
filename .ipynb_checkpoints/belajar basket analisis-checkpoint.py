# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:40:47 2019

@author: haidinata
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules 
import mlxtend as ml

bread = pd.read_csv("breadbasket.csv")

#sns.countplot(x = 'Item', data = bread, order = bread['Item'].value_counts().iloc[:10].index)
#plt.xticks(rotation=90)

df = bread.groupby(['Transaction','Item']).size().reset_index(name='count')
basket = (df.groupby(['Transaction', 'Item'])['count']
          .sum().unstack().reset_index().fillna(0)
          .set_index('Transaction'))
#The encoding function
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
basket_sets = basket.applymap(encode_units)

basket_sets
