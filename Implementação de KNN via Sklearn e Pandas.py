#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


train = pd.read_csv('/home/excript/machine_learning/teste_python/testes_arquivos/train.csv')
test = pd.read_csv('/home/excript/machine_learning/teste_python/testes_arquivos/test.csv')


# In[3]:


train.head()


# In[4]:


test.head()


# In[9]:


from sklearn.neighbors import KNeighborsClassifier

cols = ['shoe size','height']
cols2 = ['class']

x_train = train.as_matrix(cols)
y_train = train.as_matrix(cols2)
x_test = test.as_matrix(cols)
y_test = test.as_matrix(cols2)


# In[10]:


knn = KNeighborsClassifier(n_neighbors=3,weights='distance')

knn.fit(x_train,y_train.ravel())
output = knn.predict(x_test)


# In[12]:


print(knn.predict([x_test[0]]))
print(y_test[0])


# In[13]:


correct = 0.0

for i in range(len(output)):
    if y_test[i][0] == output[i]: correct += 1
        
correct / len(output)


# In[ ]:




