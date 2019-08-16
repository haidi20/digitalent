# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 08:55:47 2019

@author: haidinata
"""

import pandas as pd
data = pd.read_json("data.json")
print(data)

print()
print(data.loc[[1,3,5], ['Salary', 'Name']])

print()
print(data.to_json(orient="records"))