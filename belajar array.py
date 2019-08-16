# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 08:37:51 2019

@author: haidinata
"""

#pandas
import pandas as pd
import numpy as np
data = [['dani', 90], ['cita', 80]]
d = pd.DataFrame(data, columns=['name', 'value'], dtype=float)
print(d)