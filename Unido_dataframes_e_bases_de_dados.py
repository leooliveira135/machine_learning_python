#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from db import DemoDB


# In[2]:


database = DemoDB()


# In[3]:


database.tables


# In[4]:


album = database.tables.Album.all()


# In[5]:


album.head()


# In[6]:


artists = database.tables.Artist.all()


# In[7]:


artists.head()


# In[8]:


album_artists = pd.merge(artists,album)


# In[10]:


album_artists.head(10)


# In[11]:


album_artists = pd.merge(artists,album,on='ArtistId')


# In[12]:


album_artists.head()


# In[14]:


album.rename(columns={'ArtistId':'Artist_Id'},inplace=True)


# In[15]:


album.head()


# In[17]:


album_artist = pd.merge(album,artists,left_on='Artist_Id',right_on='ArtistId')


# In[19]:


album_artist.head()


# In[21]:


pd.merge(album,artists,left_on='Artist_Id',right_on='ArtistId').drop('Artist_Id',axis=1)


# In[22]:


alunos1 = pd.DataFrame({
    'nome':['Maria','Sofia'],
    'nota':[8,9]
})

alunos2 = pd.DataFrame({
    'nome':['João','Pedro','Maria'],
    'cod':[1,2,3]
})


# In[25]:


alunos_total = pd.merge(alunos1,alunos2,on='nome')


# In[26]:


alunos_total


# In[28]:


pd.merge(alunos1,alunos2,how='outer')


# In[29]:


pd.merge(alunos1,alunos2,how='left')


# In[30]:


pd.merge(alunos1,alunos2,how='right')


# In[ ]:




