#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


data = np.genfromtxt('iris.data',delimiter=',',usecols=(0,1,2,3))
data


# In[3]:


len(data)


# In[4]:


data[:,0]


# In[5]:


data[:50,0]


# In[6]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


plt.plot(data[:50,0],c='red',ls=':',marker='s',ms=8)


# In[12]:


data[50:100,0]


# In[14]:


plt.plot(data[:50,0],c='red',ls=':',marker='s',ms=8,label='Comp. Sépala Iris-Setosa')
plt.plot(data[50:100,0],c='green',ls=':',marker='o',ms=8,label='Comp. Sépala Iris-Versicolor')
plt.plot(data[100:150,0],c='black',ls=':',marker='s',ms=8,label='Comp. Sépala Iris-Virginica')
plt.legend()
plt.show()

