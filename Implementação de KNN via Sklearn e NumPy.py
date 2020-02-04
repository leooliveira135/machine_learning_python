#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Implementação do KNN com Sklearn
from sklearn.neighbors import KNeighborsClassifier


# In[3]:


entradas, saidas = [], []


# In[4]:


with open('/home/excript/machine_learning/teste_python/haberman.data','r') as f:
    for linha in f.readlines():
        atrib = linha.replace('\n','').split(',')
        entradas.append([int(atrib[0]),int(atrib[2])])
        saidas.append([int(atrib[3])])


# In[5]:


p = 0.6 #porcentagem dos dados para treinamento


# In[10]:


limite = int(p*len(entradas))
knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(entradas[:limite],saidas[:limite])
labels = knn.predict(entradas[limite:])
acertos, indice_label = 0,0

for i in range(limite,len(entradas)):
    if labels[indice_label] == saidas[i]: acertos += 1
    indice_label += 1
    
print('Total de treinamento: %d' % limite)
print('Total de testes: %d' % (len(entradas)-limite))
print('Total de acertos: %d' % acertos)
print('Porcentagem de acertos: %.2f' % (100 * acertos / (len(entradas) - limite)))


# In[12]:


'''
Dataset: https://archive.ics.uci.edu/ml/datasets/Balance+Scale

Attribute Information:

1. Class Name: 3 (L, B, R) 
2. Left-Weight: 5 (1, 2, 3, 4, 5) 
3. Left-Distance: 5 (1, 2, 3, 4, 5) 
4. Right-Weight: 5 (1, 2, 3, 4, 5) 
5. Right-Distance: 5 (1, 2, 3, 4, 5)

São 625 exemplos, 4 atributos e 3 possíveis classes.

"L" -> 1
"B" -> 2
"R" -> 3

'''

import numpy as np


# In[15]:


# x são as entradas e y são as saidas

x = np.genfromtxt('/home/excript/machine_learning/teste_python/dataset.data',delimiter=',',usecols=(1,2,3,4))
y = np.genfromtxt('/home/excript/machine_learning/teste_python/dataset.data',delimiter=',',usecols=(0))

print(len(x))
print(len(y))
print(x)
print(y)


# In[16]:


from sklearn.model_selection import train_test_split


# In[17]:


x_treino, x_teste, y_treino, y_teste = train_test_split(x,y,test_size=0.3,random_state=42)


# In[18]:


print(len(x_treino))
x_treino


# In[20]:


print(len(x_teste))
x_teste


# In[21]:


y_teste[0]


# In[22]:


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=17,p=2)
knn.fit(x_treino,y_treino)
labels = knn.predict(x_teste)
print(len(labels))
labels


# In[23]:


y_teste


# In[24]:


np.sum(labels == y_teste)


# In[26]:


(labels == y_teste).sum()


# In[27]:


(100 * (labels == y_teste).sum() / len(x_teste))


# In[28]:


knn.score(x_teste,y_teste)


# In[29]:


np.mean(labels == y_teste)


# In[ ]:




