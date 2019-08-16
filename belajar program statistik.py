# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:58:01 2019

@author: haidinata
"""

import pandas as pd
import numpy as np
import copy
import scipy.stats as stats


flights = pd.read_csv('mtcars.csv')

print(flights.head())

#flights.boxplot('disp', 'cyl', figsize=(5,6))