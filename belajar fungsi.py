# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:36:05 2019

@author: haidinata
"""

#vriable-legth aruments
#symbol * untuk variable bisa menerima data array
def print_me_again(key1, *keys2):
    "this print a passed string into this function"
    print ("output arguments: ")
    print(key1)
    for row in keys2:
        print(row)
    return;
    
#cal print_me_again
#print_me_again(10)
print_me_again(10, 2, 3, 4, 5, 6, 7)