# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:15:02 2019

@author: haidinata
"""
i = 0
for(i in 5):
    print(i)

# hitung penjumlahan angka genap 1 - 1234
a = 1
total = 0
while(a <= 1234):
    a+= 1
    if(a%2 == 0):
        total += a
        #print(a)

print("total = ", total)