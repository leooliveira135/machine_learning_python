#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


salario = np.array([100,200,300,500,400,150])
salario


# In[9]:


plt.plot(salario)


# In[11]:


plt.plot(salario, c='green')


# In[13]:


plt.plot(salario, c='green', ls='--')


# In[14]:


plt.plot(salario, ls='--', marker='s')


# In[16]:


plt.plot(salario,c='green',ls='--',marker='s',ms=19)
plt.show()


# In[17]:


salarios_marcos = np.array([100,200,400,300])
salarios_gileno = np.array([50,300,500,450])


# In[18]:


plt.plot(salarios_marcos,c='blue',ls='--',marker='s',ms=8,label='Salários do Marcos')
plt.plot(salarios_gileno,c='red',ls='--',marker='s',ms=8,label='Salários do Gileno')
plt.show()


# In[19]:


plt.plot(salarios_marcos,c='blue',ls='--',marker='s',ms=8,label='Salários do Marcos')
plt.plot(salarios_gileno,c='red',ls='--',marker='s',ms=8,label='Salários do Gileno')
plt.legend()
plt.show()


# In[20]:


plt.plot(salarios_marcos,c='blue',ls='--',marker='s',ms=8,label='Salários do Marcos')
plt.plot(salarios_gileno,c='red',ls='--',marker='^',ms=8,label='Salários do Gileno')
plt.legend()
plt.show()


# In[23]:


plt.plot(salarios_marcos,c='blue',ls='--',marker='s',ms=8,label='Salários do Marcos')
plt.plot(salarios_gileno,c='red',ls='--',marker='^',ms=8,label='Salários do Gileno')
plt.legend(loc='lower right')
plt.show()


# In[25]:


salarios_pedro = np.array([200,150,300,700])
plt.plot(salarios_marcos,c='blue',ls='--',marker='s',ms=8,label='Salários do Marcos')
plt.plot(salarios_gileno,c='red',ls='--',marker='^',ms=8,label='Salários do Gileno')
plt.plot(salarios_pedro,c='green',ls='--',marker='o',ms=10,label='Salários do Pedro')
plt.legend(loc='lower right')
plt.show()


# In[ ]:




