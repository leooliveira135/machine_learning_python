#!/usr/bin/env python
# coding: utf-8

# In[15]:


'''
Implementação do KNN
Sobrevivência de pacientes submetidos ao cancer de mama
link: https://archive.ics.uci.edu/ml/datasets/Haberman%27s+Survival
'''

#lista de amostras

amostras = []


# In[16]:


with open('/home/excript/machine_learning/teste_python/haberman.data','r') as f:
    for linha in f:
        atrib = linha.replace('\n','').split(',')
        amostras.append([int(atrib[0]),int(atrib[1]),int(atrib[2]),int(atrib[3])])


# In[17]:


amostras


# In[18]:


len(amostras)


# In[33]:


def info_dataset(amostras,verbose=True):
    if verbose == True:
        print('Total de amostras %d' %len(amostras))
    rot1, rot2 = 0, 0
    for amostra in amostras:
        if amostra[-1] == 1: rot1 += 1 
        else: rot2 += 1
    if verbose == True:
        print('Total rótulo 1 %d' % rot1)
        print('Total rótulo 2 %d' % rot2)
    return [len(amostras),rot1,rot2]


# In[34]:


info_dataset(amostras)


# In[36]:


info_dataset(amostras,False)


# In[38]:


p = 0.6
_,rot1,rot2 = info_dataset(amostras,False)


# In[49]:


treinamento,teste = [],[]
max_rot1,max_rot2 = int(p*rot1), int(p*rot2)
total_rot1,total_rot2 = 0,0

for amostra in amostras:
    if (total_rot1 + total_rot2) < (max_rot1 + max_rot2):
        treinamento.append(amostra)
        if (amostra[-1] == 1) and (total_rot1 < max_rot1): total_rot1 +=1
        else: total_rot2 += 1
    else:
        teste.append(amostra)


# In[50]:


print(len(treinamento))
print(len(teste))


# In[52]:


info_dataset(treinamento)


# In[54]:


info_dataset(teste)


# In[55]:


info_dataset(amostras)


# In[56]:


import math


# In[57]:


def dist_euclidiana(v1,v2):
    dim, soma = len(v1), 0
    
    for i in range(dim-1):
        soma += math.pow(v1[i]-v2[i],2)
    return math.sqrt(soma)


# In[58]:


#teste da distancia euclidiana
v1 = [1,2,3]
v2 = [2,1,3]

dist_euclidiana(v1,v2)


# In[65]:


def knn(treinamento, n_amostra, K):
    dists, tam_treino = {}, len(treinamento)
    #calcula a distancia euclidiana da nova amostra para
    #todos os outros exemplos de conjunto de treinamento
    
    for i in range(tam_treino):
        d = dist_euclidiana(treinamento[i],n_amostra)
        dists[i] = d
        
    #obter as chaves dos K-vizinhos mais próximos
    k_vizinhos = sorted(dists, key=dists.get)[:K]
    
    #votação majoritária
    qtd_rot1, qtd_rot2 = 0, 0
    
    for indice in k_vizinhos:
        if treinamento[indice][-1] == 1: qtd_rot1 += 1
        else: qtd_rot2 += 1
            
    if qtd_rot1 < qtd_rot2: return 1
    else: return 2


# In[68]:


print(teste[10])
print(knn(treinamento,teste[10],K=13))


# In[76]:


acertos, K = 0, 15
for amostra in teste:
    classe = knn(treinamento,amostra,K)
    if amostra[-1] == classe: acertos += 1
    
print('Total de treinamento: %d' %len(treinamento))
print('Total de testes: %d' %len(teste))
print('Total de acertos: %d' %acertos)
print('Porcentagem de acertos: %.2f%%' % (100*acertos/len(teste)))

