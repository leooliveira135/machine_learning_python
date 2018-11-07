#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[5]:


x = np.linspace(1,10,100)


# In[5]:


x


# In[8]:


plt.plot(x,np.sin(x))


# In[9]:


np.sin(1)


# In[10]:


plt.plot(x,np.sin(x),'r')


# In[13]:


plt.plot(x,np.sin(x),'b--')


# In[14]:


fig = plt.figure()
plt.plot(x,np.sin(x),'r--')


# In[16]:


fig.savefig('sin.png')


# In[17]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[18]:


import matplotlib.pyplot as plt
import numpy as np


# In[20]:


x = np.linspace(1,10,100)


# In[22]:


plt.plot(x,np.sin(x),'b--')
plt.plot(x,np.cos(x),'r--')
plt.show()#fora do jupyter notebook


# In[3]:


import seaborn as sns


# In[12]:


plt.plot(x,np.sin(x),'b--')
plt.plot(x,np.cos(x),'r--')
plt.show()#fora do jupyter notebook


# In[13]:


sns.set_style('white')
sns.set_style('ticks')


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import pydataset
import matplotlib.pyplot as plt
import seaborn as sns


# In[16]:


pydataset.data('titanic',show_doc=True)


# In[18]:


titanic = pydataset.data('titanic')


# In[20]:


titanic.head()


# In[22]:


titanic['class'].value_counts()


# In[26]:


titanic['class'].value_counts().plot(kind='bar')
plt.show()


# In[28]:


titanic['survived'].value_counts().plot(kind='bar')
plt.show()


# In[30]:


titanic.groupby(['survived'])['class'].value_counts()


# In[32]:


titanic.groupby(['survived'])['class'].value_counts().plot(kind='bar')
plt.show()


# In[36]:


estados = pd.read_csv('Downloads/populacao_brasil.csv')


# In[38]:


estados.head()


# In[40]:


estados['total'].hist()


# In[41]:


fig, ax = plt.subplots()
plt.hist(estados['total'],bins=15,orientation='horizontal')
ax.ticklabel_format(style='plain')
plt.show()


# In[44]:


estados['percent'] = estados['total'] / estados['total'].sum()


# In[46]:


estados.head()


# In[48]:


plt.pie(estados['percent'],labels=estados['estado'])
plt.show()


# In[52]:


plt.pie(estados['percent'],labels=estados['estado'],autopct='%1.2f%%')
plt.show()


# In[53]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import pydataset
import matplotlib.pyplot as plt
import seaborn as sns


# In[56]:


pydataset.data('AirPassengers',show_doc=True)


# In[57]:


df = pydataset.data('AirPassengers')


# In[59]:


df.head(12)


# In[60]:


plt.plot(df['time'],df['AirPassengers'])


# In[62]:


plt.scatter(df['time'],df['AirPassengers'])


# In[69]:


iris = pydataset.data('iris')


# In[71]:


iris.head()


# In[72]:


iris.tail()


# In[74]:


plt.scatter(iris['Sepal.Length'],iris['Sepal.Width'],sizes=50*iris['Petal.Length'])


# In[75]:


def specie_color(x):
    if x == 'setosa':
        return 0
    elif x == 'versicolor':
        return 1
    return 2


# In[76]:


iris['SpeciesNumber'] = iris['Species'].apply(specie_color)


# In[77]:


iris.head()


# In[78]:


plt.scatter(
    iris['Sepal.Length'],
    iris['Sepal.Width'],
    sizes=20*iris['Petal.Length'],
    c=iris['SpeciesNumber'],
    cmap='viridis',
    alpha=0.4
)


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn


# In[3]:


df = pd.read_csv('Downloads/copacabana_lat_lng.csv')


# In[4]:


df.head()


# In[17]:


plt.scatter(
    df['lat'],
    df['lng'],
    marker='.'
)


# In[18]:


import mplleaflet
import matplotlib.pyplot as plt
plt.scatter(
    df['lat'],
    df['lng'],
    marker='.'
)
mplleaflet.display()

