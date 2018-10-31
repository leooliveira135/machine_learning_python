#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


dados = {
    'nomes':['João','Maria','José',np.nan,'Pedro','Judas','Tiago'],
    'sexo':['M','F','M',np.nan,'M','M',np.nan],
    'idade':[14,13,np.nan,np.nan,15,13,14],
    'nota':[4,10,7,np.nan,8,9,7]
}

df = pd.DataFrame(dados)


# In[4]:


df


# In[5]:


df.dropna()


# In[6]:


df.dropna(how='all')


# In[7]:


df['serie'] = np.nan


# In[8]:


df


# In[9]:


df.dropna(how='all',axis=1)


# In[10]:


df.dropna(thresh=3)


# In[11]:


df['serie'].fillna('8')


# In[12]:


df


# In[13]:


df['serie'].fillna('8',inplace=True)


# In[14]:


df


# In[15]:


df['serie'] = np.nan
df


# In[16]:


df['idade'].fillna(df['idade'].mean(),inplace=True)


# In[17]:


df


# In[19]:


df[df['nomes'].notnull() & df['sexo'].notnull()]


# In[ ]:




