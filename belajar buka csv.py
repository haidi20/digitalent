# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 08:25:40 2019

@author: haidinata
"""

import pandas as pd
data = pd.read_csv("input.csv", ",")
print(data)

print()
print(data[0:5]['NIM'])

print()
print(data.loc[:, ['NAMA', 'NIM']])

print()
print(data.loc[[1,3,4], ['NAMA', 'NIM']])

print()
print(data.loc[2:11,['NAMA', 'NIM']])