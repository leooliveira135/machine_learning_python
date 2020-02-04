#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_boston


# In[4]:


boston = load_boston()


# In[5]:


boston.DESCR


# In[6]:


boston.data.shape


# In[7]:


boston.feature_names


# In[8]:


from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split


# In[10]:


K = 9
knn = KNeighborsRegressor(n_neighbors=K)
knn.fit(boston.data, boston.target)
print(boston.target[0])
print(knn.predict([boston.data[0]]))


# In[13]:


y_ = knn.fit(boston.data, boston.target).predict([boston.data[12]])
print(y_)
print(boston.target[12])


# In[17]:


import matplotlib.pyplot as plt
import numpy as np

knn = KNeighborsRegressor(n_neighbors=K)
x, y = boston.data[:50], boston.target[:50]
y_ = knn.fit(x,y).predict(x)

plt.plot(np.linspace(-1,1,50),y,label='data',color='black')
plt.plot(np.linspace(-1,1,50),y_,label='prediction',color='red')
plt.legend()
plt.show()


# In[18]:


from sklearn.metrics import mean_squared_error


# In[19]:


y_true = [3,-0.5, 2, 7]
y_pred = [2.5, 0, 2, 8]

mean_squared_error(y_true,y_pred)


# In[20]:


y_true = [1,2,3]
y_pred = [1,2,3]

mean_squared_error(y_true,y_pred)


# In[21]:


y_true = [0.9,1.2,3.4]
y_pred = [0.8,1.3,3.5]

mean_squared_error(y_true,y_pred)


# In[22]:


y_true = [1,2,3]
y_pred = [10,20,30]

mean_squared_error(y_true,y_pred)


# In[23]:


from sklearn import datasets


# In[24]:


diabetes = datasets.load_diabetes()
diabetes.data


# In[25]:


diabetes.target


# In[26]:


len(diabetes.data)


# In[27]:


len(diabetes.target)


# In[28]:


x, y = diabetes.data, diabetes.target


# In[29]:


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42)
print(len(x_train))
print(len(x_test))


# In[37]:


from sklearn.neighbors import KNeighborsRegressor

knn = KNeighborsRegressor(n_neighbors=50, p=2)
knn.fit(x_train,y_train)
output = knn.predict(x_test)

print('Saida esperada %f' % y_test[3])
print('Saida predita %f' % output[3])

from sklearn.metrics import mean_squared_error

mean_squared_error(y_test,output)


# In[ ]:




