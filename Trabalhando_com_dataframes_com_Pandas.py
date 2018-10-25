#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


s = pd.Series([1,4,6,5,7,10,6])


# In[3]:


s


# In[7]:


s[1]
s[2:4]


# In[8]:


s.describe()


# In[9]:


s.mean()


# In[10]:


s.median()


# In[11]:


s.duplicated()


# In[12]:


s2 = pd.Series([11,5,8])


# In[13]:


s = s.append(s2)
s


# In[14]:


df = pd.DataFrame(
    [['fchollet/keras',11302],
    ['openai/universe',4350],
    ['pandas-dev/pandas',8168]]
)


# In[16]:


df.shape


# In[17]:


df


# In[19]:


df = pd.DataFrame(
    [['fchollet/keras',11302],
    ['openai/universe',4350],
    ['pandas-dev/pandas',8168]],
    columns=['repository','stars']
)


# In[21]:


df


# In[25]:


df['repository']


# In[26]:



df['stars']


# In[27]:


df['stars'].mean()


# In[29]:


df['stars'].median()


# In[31]:


df.iloc[1]


# In[32]:


df.iloc[1]['stars']


# In[ ]:




