#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


help(pd.read_csv)


# In[3]:


copacabana = pd.read_csv('copacabana.csv',delimiter=';')


# In[4]:


copacabana


# In[5]:


populacao_pe = pd.read_excel('total-populacao-pernambuco.xls')


# In[6]:


populacao_pe


# In[7]:


copacabana.columns


# In[9]:


copacabana['Quartos'].describe()


# In[10]:


copacabana['Quartos'] > 5


# In[20]:


copacabana.loc[copacabana['Quartos'] == 6]


# In[21]:


copacabana.loc[copacabana['Quartos'] == 5]


# In[22]:


copacabana['AreaConstruida'] * copacabana['VAL_UNIT']


# In[23]:


copacabana['TOTAL'] = copacabana['AreaConstruida'] * copacabana['VAL_UNIT']


# In[24]:


copacabana['TOTAL'].describe()


# In[25]:


copacabana['TOTAL'].head()


# In[26]:


copacabana['TOTAL'].tail()

