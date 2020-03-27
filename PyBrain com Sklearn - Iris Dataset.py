#!/usr/bin/env python
# coding: utf-8

# In[1]:


# carregando os dados da Iris Dataset com sklearn

from sklearn import datasets
iris = datasets.load_iris()

# obtendo as entradas e saidas
x, y = iris.data, iris.target

print(len(x))
print(len(y))


# In[29]:


from pybrain3.datasets.classification import ClassificationDataSet

dataset = ClassificationDataSet(4,1,nb_classes=3)

# adicionando as amostras
for i in range(len(x)):
    dataset.addSample(x[i],y[i])

len(dataset)


# In[4]:


dataset['input']


# In[5]:


dataset['target']


# In[6]:


len(dataset['target'])


# In[30]:


# particionando os dados para treinamento
train_data, part_data = dataset.splitWithProportion(0.6)
print('Quantidade para treino %d' % len(train_data))

#dividindo os dados para teste e validação
test_data, val_data = part_data.splitWithProportion(0.5)
print('Quantidade para teste %d' % len(test_data))
print('Quantidade para validação %d' % len(val_data))


# In[19]:


from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.supervised.trainers import BackpropTrainer

net = buildNetwork(dataset.indim, 3, dataset.outdim)
trainer = BackpropTrainer(net, dataset=train_data, learningrate=0.01, momentum=0.1, verbose=True)

train_errors, val_errors = trainer.trainUntilConvergence(dataset=train_data, maxEpochs=100)


# In[20]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.plot(train_errors, 'b', val_errors, 'r')
plt.show()

trainer.totalepochs


# In[21]:


trainer.trainOnDataset(train_data, 500)


# In[27]:


out = net.activateOnDataset(test_data)

for i in range(len(out)):
    print('out: %f, correct: %f' % (out[i], test_data['target'][i]))


# In[28]:


print(type(dataset))
print(type(train_data))


# In[52]:


from sklearn import datasets
from pybrain3.datasets.classification import ClassificationDataSet
from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.supervised.trainers import BackpropTrainer

iris = datasets.load_iris()
x, y = iris.data, iris.target
dataset = ClassificationDataSet(4,1,nb_classes=3)

for i in range(len(x)):
    dataset.addSample(x[i],y[i])
    
train_data_temp, part_data_temp = dataset.splitWithProportion(0.6)
test_data_temp, val_data_temp = part_data_temp.splitWithProportion(0.5)

train_data = ClassificationDataSet(4,1,nb_classes=3)

for n in range(train_data_temp.getLength()):
    train_data.addSample(train_data_temp.getSample(n)[0],train_data_temp.getSample(n)[1])
    
test_data = ClassificationDataSet(4,1,nb_classes=3)

for n in range(test_data_temp.getLength()):
    test_data.addSample(test_data_temp.getSample(n)[0],test_data_temp.getSample(n)[1])    

val_data = ClassificationDataSet(4,1,nb_classes=3)

for n in range(val_data_temp.getLength()):
    val_data.addSample(val_data_temp.getSample(n)[0],val_data_temp.getSample(n)[1])

print('Antes de usar _convertToOneOfMany...')
print(train_data['target'][:5])

train_data._convertToOneOfMany()
test_data._convertToOneOfMany()
val_data._convertToOneOfMany()

print('Depois de usar _convertToOneOfMany...')
print(train_data['target'][:5])

print('-------------------------------------')

from pybrain3.structure.modules import SoftmaxLayer

net = buildNetwork(4, 5, 3, outclass=SoftmaxLayer)
trainer = BackpropTrainer(net, dataset=train_data, learningrate=0.01, momentum=0.5)
trainer.trainOnDataset(train_data,100)

from pybrain3.utilities import percentError

out = net.activateOnDataset(test_data).argmax(axis=1)
print('Erro de teste: %f' % percentError(out,test_data['class']))

import numpy as np

out = net.activateOnDataset(val_data).argmax(axis=1)
print('Erro de validação: %f' % percentError(out,val_data['class']))

print('-------------------------------------')

print('Validação')
print('saída da rede:\t', out)
print('correto:\t', val_data['class'][:,0])


# In[2]:


from sklearn import datasets

iris = datasets.load_iris()

print(iris.feature_names)
print(iris.target_names)
print(len(iris.data))


# In[6]:


from sklearn.neural_network import MLPClassifier

x, y = iris.data, iris.target

mlp = MLPClassifier(solver='adam',alpha=0.0001,hidden_layer_sizes=(5,),random_state=1,
                   learning_rate='constant',learning_rate_init=0.01,max_iter=500,
                   activation='logistic',momentum=0.9,verbose=True,tol=0.0001)

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x,y,test_size=0.3,random_state=1)

mlp.fit(x_treino,y_treino)
saidas = mlp.predict(x_teste)
print('-------------------------------------')

print('Saída da rede:\t',saidas)
print('Saída desejada:\t',y_teste)

print('-------------------------------------')

print('Score: ', (saidas==y_teste).sum()/len(x_teste))
print('Score: ', mlp.score(x_teste,y_teste))

