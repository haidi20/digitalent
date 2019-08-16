# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:14:56 2019

@author: haidinata
"""

import bonobo

def generate_data():
    yield 'foo'
    yield 'bar'
    yield 'baz'
    
def uppercase(x: str):
    return x.upper()

def output(x: str):
    print(x)
    
graph = bonobo.Graph(
    generate_data,
    uppercase,
    output,
)

if __name__ == '__main__':
    bonobo.run(graph)