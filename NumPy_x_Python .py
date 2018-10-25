#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np

a = np.array([[2,4],[6,8]])
print(a.mean())
print(a.diagonal())
print(a.ndim) 


# In[8]:


lista = [1,2,3,'leo']


# In[15]:


soma = 0
for i in range(0,100000001):
    soma += i


# In[18]:


l = [20,30,10,40]
print(l[1:3])
print(l[::2])


# In[20]:


import numpy as np
a = np.array(l)
a


# In[23]:


print(a[1:3])
print(a[::2])


# In[25]:


l


# In[29]:


l2 = l[:]
l2
l2[0] = 1000
print(l)
print(l2)


# In[30]:


a


# In[33]:


b = a[:]
b
b[0]=1000
print(a)
print(b)


# In[34]:


c = a.copy()
print(c)
print(a)


# In[35]:


c[0] = 1000000
print(c)
print(a)


# In[39]:


mat = [[5,4,7],[0,3,4],[0,0,6]]

print(mat[1][1])


# In[41]:


[linha[1] for linha in mat]


# In[42]:


import numpy as np


# In[43]:


joao_pts=[20,30,40,15]
pedro_pts=[100,24,48,23]
maria_pts=[92,22,34,12]
marcos_pts=[12,34,13,43]

pontos = np.array([joao_pts,pedro_pts,maria_pts,marcos_pts])


# In[46]:


pontos


# In[48]:


pontos[0]


# In[49]:


pontos[1][0]


# In[51]:


my_data = np.arange(0,20)
print(my_data)


# In[53]:


mat1 = np.reshape(my_data,(5,4))
print(mat1)


# In[55]:


mat1[2,2]


# In[58]:


pontos.item(5)


# In[59]:


m1 = ['python','e','legal']
m2 = ['guido','van','rossum']
m3 = [10,20,30]


# In[60]:


[m1,m2,m3]


# In[61]:


np.array([m1,m2,m3])


# In[62]:


import numpy as np


# In[63]:


m1 = np.array([[1,2,3],[4,5,6]])
m2 = np.array([[7,8,9],[10,11,12]])


# In[65]:


m2/m1


# In[67]:


np.matrix.round(m2/m1)


# In[68]:


10*m2


# In[70]:


m1 + 5


# In[72]:


m2 -1


# In[73]:


m1*m2

