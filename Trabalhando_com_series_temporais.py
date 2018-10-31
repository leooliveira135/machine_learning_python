#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from db import DB


# In[2]:


database = DB(filename='logs.sqlite3',dbtype='sqlite')


# In[3]:


database.tables


# In[4]:


log_df = database.tables.log.all()


# In[6]:


log_df.head()


# In[9]:


log_df.dtypes


# In[11]:


log_df['date'] = pd.to_datetime(log_df['date'],format="%Y-%m-%d %H:%M:%S.%f")


# In[13]:


log_df.dtypes


# In[15]:


log_df.head()


# In[16]:


log_df.set_index(['date'],inplace=True)


# In[17]:


log_df.head()


# In[18]:


log_df['2017']


# In[19]:


log_df['2017-01-03 10:47']


# In[21]:


log_df['2017-01-03 10:47':'2017-01-03 10:51']

