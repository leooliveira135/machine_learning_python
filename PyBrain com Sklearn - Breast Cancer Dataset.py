#!/usr/bin/env python
# coding: utf-8

# In[9]:


from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

print(cancer.feature_names)
print(cancer.target_names)
print(len(cancer.data))
print(cancer.keys())
print(cancer['data'].shape)

x, y = cancer['data'], cancer['target']

print(len(x))
print(len(y))


# In[12]:


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y)

print(len(x_train))
print(len(x_test))


# In[30]:


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(30,30,30))
mlp.fit(x_train,y_train)


# In[31]:


predictions = mlp.predict(x_test)
print(predictions)
print('Score: ',mlp.score(x_test,y_test))


# In[29]:


from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))


# In[32]:


mlp.coefs_


# In[33]:


mlp.intercepts_


# In[ ]:




