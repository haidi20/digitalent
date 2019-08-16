# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:24:09 2019

@author: haidinata
"""

class RumusBangunDatar():  
    menus       = ['Persegi', 'Persegi Panjang', 'Jajar Genjang', 'keluar']
    menu_detail = ['Keliling', 'Luas']
    
    def menu(self):
        print('Menu Pilihan Bangun Datar :')
        no = 1
        for menu in self.menus:
            print(no," ", menu)
            no+=1
        
        inputan = input('masukkan angka yang dipilih = ')
        pilihan = int(inputan) - 1
        
        if(pilihan == 3):
            return False
        else:
            validasi = self.validasi(pilihan)
            if(validasi):
                self.sub_menu(pilihan)
    
    def sub_menu(self, pilihan):
        print('Sub Menu Pilihan Bangunan',self.menus[pilihan],' :')
        no = 1
        for menu in self.menu_detail:
            print(no," ", menu)
            no+=1
        
        inputan = input('masukkan angka yang dipilih = ')
        pilih = int(inputan)
        
        validasi = self.validasi(pilih)
        if validasi:
            #print('menu = ', self.menus[pilihan] , ' sub menu = ', pilih)
            if pilihan == 0:
                if pilih == 1:
                    self.kelilingpersegi()
                elif pilih == 2:
                    self.luaspersegi()
                else:
                    self.validasi(pilih)
            elif pilihan == 1:
                if pilih == 1:
                    self.kelilingpersegipanjang()
                elif pilih == 2:
                    self.luaspersegipanjang()
                else:
                    self.validasi(pilih)
            elif pilihan == 2:
                if pilih == 1:
                    self.kelilingjajargenjang()
                elif pilih == 2:
                    self.luasjajargenjang()
                else:
                    self.validasi(pilih)
            else:
                self.validasi(pilihan)
                
            self.menu()

    def validasi(self, pilihan):
        if(pilihan >=0 and pilihan <=2):
            return True
        else:
            print('pilihan tidak tersedia')
            
    def kelilingpersegi(self):
        print ('Perhitungan Keliling Persegi')
        sisi = input('Masukan Sisi : ')
        sisi = int(sisi)
        keliling = sisi * 4
        print ('Keliling Persegi = ', keliling, 'cm2')
        print()
            
    def luaspersegi(self):
        print ('Perhitungan Luas Persegi')
        sisi = input('Masukan Sisi : ')
        sisi = int(sisi)
        luas = sisi*sisi
        print ('Luas Persegi = ', luas, 'cm2')
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
        keliling = 2*(p+l)
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
        
        
        
        
rumus = RumusBangunDatar()
rumus.menu()