#!/usr/bin/env python
# coding: utf-8

# In[17]:


from PIL import Image
from math import pi, log, exp
import numpy as np

img = Image.open('darwin.png')
img.load()
img


# In[18]:


print(img.size)
print(img.mode)

data = img.getdata()
print(data[1])
a = np.array(img, dtype=np.uint8).reshape(img.size[::-1])
print(a[0,1])


# In[40]:


b = a[750:1500, 750:1500]
pic = Image.fromarray(b) # создаем новый объект Image из массива фрагмента
pic


# In[31]:


def average_blur(img, r):
    w, h = img.size
    a = np.array(img.getdata(), dtype=np.uint8).reshape(h, w)
    b = np.zeros((h,w), dtype=np.uint8)
    for i in range(r, h - r):
        for j in range(r, w - r):
            s = 0
            for x in range(-r, r):
                for y in range(-r, r):
                    s+=a[i+x,j+y]
            b[i,j] = s / (2*r+1)**2
    return Image.fromarray(b)


# In[33]:


average_blur(Image.fromarray(img[750:1500, 750:1500]), 5)


# In[ ]:
