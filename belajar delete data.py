# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:46:38 2019

@author: haidinata
"""

from sqlalchemy import create_engine
from pandas.io import sql

import pandas as pd

data = pd.read_json('data.json')
engine = create_engine('sqlite:///:memory:')
data.to_sql('data_table', engine)

sql.execute('delete from data_table where name= (?)', engine, params=[('Gary')])

res = pd.read_sql_query('select * from data_table', engine)
print(res)