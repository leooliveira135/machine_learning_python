#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


valores = np.genfromtxt('arquivo.csv',delimiter=',',skip_header=1)
print(valores)

