#!/usr/bin/env python
# coding: utf-8

# In[13]:


from db import DB


# In[14]:


database = DB(filename='logs.sqlite3',dbtype='sqlite')


# In[15]:


database.tables


# In[16]:


log_df = database.tables.log


# In[18]:


log_df


# In[22]:


log_df = database.tables.log.all()


# In[23]:


log_df


# In[28]:


log_df = database.query('select * from log where user_id = 3')


# In[29]:


log_df


# In[30]:


log_df = database.query('select * from log')
log_df

