#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr = np.array([1,2,3])
arr


# In[3]:


np.insert(arr,1,10)


# In[4]:


a = np.array([[1,2],[3,4]])
print(a)
print(a.ndim)


# In[6]:


print(a.sum(axis=0))
print(a.sum(axis=1))


# In[7]:


np.insert(a,1,5,axis=1)


# In[8]:


np.insert(a,0,5,axis=0)


# In[9]:


a = np.array([1,2,3])


# In[10]:


np.append(a,[4,5,6])


# In[11]:


a = np.array([[1,2],[3,4]])


# In[12]:


np.append(a,[[5,6]])


# In[13]:


np.append(a,[[5,6]],axis=0)


# In[15]:


a.ndim


# In[16]:


a2 = np.array([5,6,7])
a2.ndim


# In[18]:


a = np.array([[1,2],[3,4],[5,6]])


# In[19]:


np.delete(a,1,0)


# In[20]:


np.delete(a,0,1)


# In[21]:


a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
a


# In[22]:


np.delete(a,np.s_[::2],0)


# In[23]:


a = np.array([[1,2],[3,4]])


# In[24]:


np.repeat(a,2)


# In[25]:


np.repeat(a,3)


# In[26]:


np.repeat(a,2,0)


# In[27]:


np.repeat(a,2,1)


# In[28]:


np.repeat(3,4)


# In[29]:


a = np.array([1,2,3])


# In[31]:


np.tile(a,2)


# In[32]:


b = np.array([[1,2],[3,4]])


# In[33]:


np.tile(b,2)


# In[34]:


a = np.array([[1,2,3],[4,5,6]])


# In[35]:


np.array_split(a,2,0)


# In[36]:


np.array_split(a,2,1)


# In[37]:


b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])


# In[38]:


arrays = np.array_split(b,2,0)

for array in arrays:
    print(array)


# In[39]:


print(arrays)


# In[40]:


np.zeros(4)


# In[42]:


np.zeros([2,2])


# In[43]:


np.zeros([2,3])


# In[44]:


np.zeros([5,5])


# In[2]:


np.ones([10,10])


# In[3]:


a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])


# In[4]:


np.concatenate((a,b),axis=0)


# In[6]:


b.T


# In[7]:


a.T


# In[8]:


np.concatenate((a,b.T),axis=1)

