# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 08:20:34 2019

@author: haidinata
"""

f = open("test.txt")
print(f.read(10))
print(f.read(14))
print(f.read())

#create file and read
print()
with open("test2.txt", "w") as f:
    f.write("this new first line\n")
    f.write("this new second line\n")
    f.write("this new third line\n")
    
f = open("test2.txt")
print(f.read())

#read file gambar
print()
f = open("gambar.gif", "r+b")
print(f.read())

#exception handling
print()
try:
    f = open("test.txt")
    print(f.read(10))
    print(f.read(14))
    print(f.read(2000))
finally:
    f.close()