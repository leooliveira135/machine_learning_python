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


# In[2]:


df = pd.DataFrame(
    [
        ['PE','Pernambuco','Recife'],['RJ','Rio de Janeiro','RJ'],
        ['PB','Paraíba','João Pessoa'],['SP','São Paulo','São Paulo'],['MG','Minas Gerais','Belo Horizonte'],
        ['CE','Ceará','Fortaleza'],['AC','Acre','Rio Branco'],
        ['MA','Maranhão','São Luís'],['RN','Rio Grande do Norte','Natal'],
        ['PR','Paraná','Curitiba'],['RS','Rio Grande do Sul','Porto Alegre'],
    ], columns=['sigla','nome','capital']
)


# In[5]:


df['sigla']


# In[7]:


df.index


# In[10]:


df.iloc[0]


# In[12]:


df.ix[:2]


# In[14]:


df.iloc[:2]


# In[15]:


df.index = pd.Index([1,2,3,4,5,6,7,8,9,10,11])
df


# In[16]:


df.index = df['sigla']


# In[19]:


df.ix['PE']


# In[20]:


del df['sigla']
df


# In[2]:


import pydataset


# In[4]:


pydataset.data()


# In[6]:


type(pydataset.data())


# In[7]:


titanic = pydataset.data('titanic')


# In[10]:


titanic.head()


# In[12]:


titanic.tail()


# In[13]:


titanic.describe()


# In[14]:


titanic['class'].value_counts()


# In[15]:


len(pydataset.data())


# In[ ]:




