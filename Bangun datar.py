# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:44:00 2019

@author: USER
"""

def luaspersegi(self):
    print ('Perhitungan Luas Persegi')
    sisi = input('Masukan Sisi : ')
    sisi = int(sisi)
    luas = sisi * sisi
    print ('Luas Persegi = ', luas, 'cm2')
    print()
   
def kelilingpersegi(self):
    print ('Perhitungan Keliling Persegi')
    sisi = input('Masukan Sisi : ')
    sisi = int(sisi)
    keliling = sisi * 4
    print ('Keliling Persegi = ', keliling, 'cm2')
    print()

def luaspersegipanjang(self):
    print ('Perhitungan Luas Persegi Panjang')
    p = input('Masukan Panjang : ')
    l = input('Masukan Lebar : ')
    p = int(p)
    l = int(l)
    luas = p*l
    print ('Luas Persegi Panjang = ', luas, 'cm2')
    print()

def kelilingpersegipanjang(self):
    print ('Perhitungan Keliling Persegi Panjang')
    p = input('Masukan Panjang : ')
    l = input('Masukan Lebar : ')
    p = int(p)
    l = int(l)
    keliling = p * l
    print ('Keliling Persegi Panjang = ', keliling, 'cm2')
    print()
 
def luasjajargenjang(self):
    print ('Perhitungan Luas Jajar Genjang')
    a = input('Masukan Alas : ')
    t = input('Masukan Tinggi : ')
    a = int(a)
    t = int(t)
    luas = a * t
    print ('Luas Jajar Genjang = ', luas, 'cm2')
    print()
    
def kelilingjajargenjang(self):
    print ('Perhitungan Keliling Jajar Genjang')
    panjang = input('Masukan Panjang : ')
    l = input('Masukan Lebar : ')
    panjang = int(panjang)
    l = int(l)
    keliling = panjang * l
    print ('Keliling Jajar Genjang = ', keliling, 'cm2')
    print()
    