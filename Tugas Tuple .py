#!/usr/bin/env python
# coding: utf-8

# In[4]:


# mengakses nilai tuple 
# membuat tuple
nama = ('pak dida', 'pak karel', 'ibu gloria')

# mengakses nilai tuple
print(nama[1])
print(nama[0])
print(nama[2])


# In[6]:


#Element pada tuple tidak dapat dirubah tetapi dapat diganti dengan elemen lain.
t = ('a', 'b', 'c', 'd', 'e')
t = ('A',) + t[1:]
print(t)


# In[3]:





# In[4]:


#perbandigan Tuple
tuple1 = (1, 2, 3)
tuple2 = (1, 2)

# buat tuple2 sama panjangnya dengan tuple1 dengan menambahkan elemen ketiga
tuple2 += (0,) * (len(tuple1) - len(tuple2))

if tuple1 < tuple2:
    print("tuple1 lebih kecil dari tuple2")
else:
    print("tuple1 lebih besar atau tuple2")


# In[5]:


# menggunakan loop untuk membandingkan elemen kedua tupel hingga panjang minimum kedua tupel. 
tuple1 = (1, 2, 3)
tuple2 = (1, 2)

for i in range(min(len(tuple1), len(tuple2))):
    if tuple1[i] < tuple2[i]:
        print("tuple1 lebih kecil dari tuple2")
        break
else:
    print("tuple1 lebih besar atau tuple2")


# In[6]:


# peugasan tuple contoh 1
(n1, n2) = (99, 7)
print(n1)
print(n2)


# In[3]:






# In[ ]:





# In[ ]:




