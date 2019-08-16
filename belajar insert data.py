# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:43:47 2019

@author: haidinata
"""

from sqlalchemy import create_engine
from pandas.io import sql
import pandas as pd

data = pd.read_json('data.json')
# create the db engine
engine = create_engine('sqlite:///:memory:')

# store the dataFrame as a table
data.to_sql('data_table', engine)   

sql.execute('INSERT INTO data_table VALUES(?,?,?,?,?,?)', engine, params=[('id',9,'Ruby',711.20,'2015-03-27','IT')])

res = pd.read_sql_query('SELECT * FROM data_table', engine)
print(res)