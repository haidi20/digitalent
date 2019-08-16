# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:40:28 2019

@author: haidinata
"""
from sqlalchemy import create_engine
import pandas as pd

data = pd.read_json('data.json')
# create the db engine
engine = create_engine('sqlite:///:memory:')

# store the dataFrame as a table
data.to_sql('data_table', engine)   

# query1 on the relational table
res1 =  pd.read_sql_query('SELECT * FROM data_table', engine)
print('result1')
print(res1)
print('')

# query2 on the relational table
res2 = pd.read_sql_query('SELECT dept, sum(salary) FROM data_table group by dept', engine)
print('result2')
print(res2)
print('')