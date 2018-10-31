#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


df = pd.read_csv('primary-results.csv')


# In[5]:


df.head()


# In[6]:


len(df)


# In[8]:


df.groupby('candidate')


# In[9]:


df.groupby('candidate').aggregate({'votes':[min, np.mean, max]})


# In[10]:


df[df['votes']==590502]


# In[17]:


df.loc[df['votes'] == 590502]


# In[18]:


df.groupby('candidate').aggregate({'fraction_votes':[min, np.mean, max]})


# In[21]:


df[(df['fraction_votes'] == 1) & (df['candidate'] == 'Hillary Clinton')]


# In[22]:


def fraction_votes_filter(x):
    return x['votes'].sum() > 300000

df.groupby('state').filter(fraction_votes_filter)


# In[23]:


df[df['state_abbreviation'] == 'AL']['votes'].sum()


# In[24]:


def fraction_votes_filter(x):
    return x['votes'].sum() > 1000000

df.groupby('state').filter(fraction_votes_filter)


# In[25]:


df.groupby(['state_abbreviation','candidate'])['votes'].sum()

