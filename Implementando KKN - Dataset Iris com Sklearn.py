#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn import neighbors, datasets


# In[2]:


iris = datasets.load_iris()


# In[4]:


iris.DESCR


# In[5]:


x = iris.data
x


# In[6]:


len(x)


# In[7]:


y = iris.target
y


# In[8]:


iris.target_names


# In[12]:


knn = neighbors.KNeighborsClassifier(n_neighbors=5)

knn.fit(x,y)


# In[13]:


knn.predict(x)


# In[14]:


acuracia = knn.score(x,y)
acuracia


# In[ ]:




