#!/usr/bin/env python
# coding: utf-8

# In[1]:


1+1


# In[2]:


print("Hello World")


# In[1]:


s1 = {1,2,3,4}
s2 = {3,4,5,6}
inter = s1.intersection(s2)
print(inter)


# In[2]:


s1 = {1,2,3,4}
s2 = {3,4,5,6}
diff = s1.difference(s2)
print(diff)


# In[4]:


lista = [1,2,3,3,3,4,5,5,6,7,7,7]
s = set(lista)
print(s)


# In[19]:


dic = {"marcos":28,"maria":20,"pedro":18}
print(dic)
print(dic['marcos'])
dic['marcos']=25
print(dic['marcos'])
dic['felipe']=30
print(dic)

for k in dic:
    print(dic[k], end=" ")
    
print("\n",dic.items())
print(dic.keys())
print(dic.values())
print('maria' in dic)
print('python' in dic)


# In[27]:


def f(*args):
    return print(sum(args))

lista = 1,2,3,4
f(*lista)


# In[29]:


class Conta:
    
    def __init__(self,cliente,numero):
        self.cliente = cliente
        self.numero = numero
        
class ContaEspecial(Conta):
    
    def __init__(self,cliente,numero,limite=0):
        Conta.__init__(self,cliente,numero)
        self.limite = limite
        
c = ContaEspecial('leo','1234',100)
print(c.limite)
print(c.numero)


# In[34]:


dobro = lambda x: x*2
print(dobro(3))

soma = lambda x, y: x+y
print(soma(10,20))

lista = [1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x%2 == 0, lista))
list(map(lambda x: x*2, lista))

