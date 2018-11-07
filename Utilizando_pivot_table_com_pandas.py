#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


primary_df = pd.read_csv('primary-results.csv')


# In[5]:


primary_df['candidate'].unique()


# In[6]:


pd.pivot_table(
    primary_df,
    index=['state','party','candidate'],
    values=['votes'],
    aggfunc={'votes':np.sum})


# In[7]:


primary_df['rank'] = primary_df.groupby(
    ['county','party'])['votes'].rank(ascending=False
)


# In[9]:


primary_df[primary_df['county']=='Los Angeles']


# In[11]:


primary_df_groupby = primary_df.groupby([
    'state','party','candidate'
]).sum()
del primary_df_groupby['fips']
del primary_df_groupby['fraction_votes']
primary_df_groupby.reset_index(inplace=True)
primary_df_groupby.head(10)


# In[12]:


primary_df_groupby['rank'] = primary_df_groupby.groupby([
    'state','party'
])['votes'].rank(ascending=False)


# In[15]:


primary_df_groupby.head(10)


# In[18]:


pd.pivot_table(primary_df_groupby,index=[
    'state','party','candidate'
],values=[
    'rank','votes'
])


# In[19]:


primary_df_groupby[primary_df_groupby['rank'] == 1]['candidate'].value_counts()

