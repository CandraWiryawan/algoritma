# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 14:38:34 2022

@author: MSI GAMING
"""

#mencetak judul program
def main():
    print('menentukan bilangan terbesar dari tiga buah bilangan')
    
    #data diri
    print('Nama : I Nengah Candra Wiryawan')
    print('NIM : 21081000002')
    print('Kelas : 1D')
    
    #menentukan variabel yang akan di input
    a = int(input('masukan nilai ke-1: '))
    b = int(input('masukan nilai ke-2: '))
    c = int(input('masukan nilai ke-3: '))
    
    #menentukan bilangan terbesar
    if a > b:
        maks = a
        if a > c:
            maks = a
            
    else:
        if b > c:
            maks = b
        else:
            maks = c
            
    #mencetak bilangan terbesar
    print('nilai terbesar dari ketiga bilangan tersebut adalah %d' %maks)
    
if __name__ == '__main__':
    main()