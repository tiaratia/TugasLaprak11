#!/usr/bin/env python
# coding: utf-8

# In[5]:


# nomor 1
def cek_sama(t):
    
    if len(t) == 0:
        return True
    else:
        return t[0] == cek_sama(t[1:])

tA = (90, 90, 90, 90)

if cek_sama(tA):
  print("False")
else:
  print("True")


# In[9]:


# nomor 2
def biodata(nama, nim, alamat):
    
  nama_depan, nama_belakang = nama.split(' ', 1)

  nim_karakter = tuple(nim)
  nama_depan_karakter = tuple(nama_depan)
  nama_belakang_karakter = tuple(nama_belakang)
  

  print("NIM:", nim)
  print("NAMA:", nama)
  print("ALAMAT:", alamat)
  print("NIM:", nim_karakter)
  print("NAMA DEPAN:", nama_depan_karakter)
  print("NAMA TERBALIK:", nama_belakang, nama_depan)

biodata('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')


# In[ ]:




