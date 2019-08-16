# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 09:16:20 2019

@author: haidinata
"""

import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
df = pd.read_csv('property_data.csv')

print(df)
print()

print(df['ST_NUM'])
print(df['ST_NUM'].isnull())
print(df.isnull().sum().sum())


missing_values = ["n/a", "na", "--"]
df1 = pd.read_csv('property_data.csv', na_values = missing_values)
#print(df1)
