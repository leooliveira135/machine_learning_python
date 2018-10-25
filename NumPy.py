#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy


# In[3]:


a = numpy.array([10,20,30,40])


# In[6]:


print(a)
type(a)


# In[9]:


mat = numpy.array([[1,2],[3,4]])
mat


# In[12]:


print(mat[1][1])
print(mat[-1][-1])


# In[16]:


mat[1,:]


# In[18]:


mat[:,0]


# In[20]:


mat.transpose()


# In[22]:


m1 = numpy.array([[1,2],[3,4]])
m2 = numpy.array([[5,6],[7,8]])
m1+m2


# In[23]:


m1-m2


# In[25]:


m1*m2


# In[26]:


m3 = numpy.array([1,2,3,4])
m3.sum()


# In[27]:


m3.argmax()


# In[28]:


m3.argmin()


# In[ ]:




