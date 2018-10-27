#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pydataset


# In[2]:


titanic = pydataset.data('titanic')


# In[3]:


titanic.columns


# In[4]:


titanic['class'].describe()


# In[5]:


titanic['class'].nbytes


# In[6]:


get_ipython().run_cell_magic('time', '', "titanic['class'] == '3rd class'")


# In[7]:


titanic['class'] = titanic['class'].astype('category')


# In[9]:


titanic['class'].describe()


# In[10]:


titanic['class'].nbytes


# In[11]:


get_ipython().run_cell_magic('time', '', "titanic['class'] == '3rd class'")

