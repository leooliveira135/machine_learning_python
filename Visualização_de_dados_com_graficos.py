#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


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


# In[5]:


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


# In[6]:


import mplleaflet
import matplotlib.pyplot as plt
plt.scatter(
    df['lat'],
    df['lng'],
    marker='.'
)
mplleaflet.display()


# In[7]:


df = pd.read_csv('reported.csv')


# In[8]:


df.head()


# In[9]:


df.fillna(0,inplace=True)


# In[10]:


df.head()


# In[11]:


plt.plot(df['Year'],df['crimes.total'],'-r')
plt.plot(df['Year'],df['crimes.person'],'-b')
plt.show()


# In[13]:


fig, ax = plt.subplots()
ax.plot(df['Year'],df['crimes.total'],'-r')
ax.plot(df['Year'],df['crimes.person'],'-b')
ax.legend()


# In[14]:


fig, ax = plt.subplots()
ax.plot(df['Year'],df['crimes.total'],'-r')
ax.plot(df['Year'],df['crimes.person'],'-b')
ax.legend(loc='upper left')


# In[15]:


fig, ax = plt.subplots()
ax.plot(df['Year'],df['crimes.total'],'-r')
ax.plot(df['Year'],df['crimes.person'],'-b')
ax.legend(loc='upper left')
ax.set_ylabel('Quantity')
ax.set_xlabel('Year')
ax.set_title('Crimes: Total x Person')


# In[16]:


fig, ax = plt.subplots()
ax.plot(df['Year'],df['crimes.total'],'-r')
ax.plot(df['Year'],df['crimes.person'],'-b')
ax.legend(loc='upper left')
ax.set_ylabel('Quantity')
ax.set_xlabel('Year')
ax.set_title('Crimes: Total x Person')
ax.set_xlim([df['Year'].min(),df['Year'].max()])


# In[17]:


fig, ax = plt.subplots()
ax.plot(df['Year'],df['crimes.total'],'-r')
ax.plot(df['Year'],df['crimes.person'],'-b')
ax.legend(loc='upper left')
ax.set_ylabel('Quantity')
ax.set_xlabel('Year')
ax.set_title('Crimes: Total x Person')
ax.set_xlim([df['Year'].min(),df['Year'].max()])
ax.plot()


# In[18]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import matplotlib.dates as dates
import datetime as dt


# In[19]:


df = pd.read_csv('ppz-jan-fev-2017.csv')


# In[20]:


df.head()


# In[21]:


df.tail()


# In[22]:


def to_date(value):
    return dt.datetime(2017,1,1) + dt.timedelta(hours=value)


# In[23]:


df['date'] = df['hour'].apply(to_date)


# In[24]:


df.head()


# In[26]:


df.tail()


# In[27]:


del df['hour']
df.head()


# In[28]:


df.set_index(['date'],inplace=True)


# In[30]:


df.head()


# In[34]:


fig,ax = plt.subplots()
ax.plot_date(df.index.to_pydatetime(),df['views'],'b-')
ax.xaxis.set_minor_locator(dates.DayLocator(bymonthday=range(5,32,5)))
ax.xaxis.set_minor_formatter(dates.DateFormatter('%d'))
ax.xaxis.grid(True,which='minor')
ax.yaxis.grid()
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))
ax.set_xlim([df.index.to_pydatetime().min(),df.index.to_pydatetime().max()])
plt.tight_layout()
plt.show()


# In[36]:


import locale


# In[38]:


locale.setlocale(locale.LC_ALL,'pt_BR')


# In[39]:


fig,ax = plt.subplots()
ax.plot_date(df.index.to_pydatetime(),df['views'],'b-')
ax.xaxis.set_minor_locator(dates.DayLocator(bymonthday=range(5,32,5)))
ax.xaxis.set_minor_formatter(dates.DateFormatter('%d'))
ax.xaxis.grid(True,which='minor')
ax.yaxis.grid()
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))
ax.set_xlim([df.index.to_pydatetime().min(),df.index.to_pydatetime().max()])
plt.tight_layout()
plt.show()


# In[40]:


fig,ax = plt.subplots()
ax.plot_date(df.index.to_pydatetime(),df['views'],'b-')
ax.xaxis.set_minor_locator(dates.DayLocator(bymonthday=range(5,32,5),interval=2))
ax.xaxis.set_minor_formatter(dates.DateFormatter('%d'))
ax.xaxis.grid(True,which='minor')
ax.yaxis.grid()
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))
ax.set_xlim([df.index.to_pydatetime().min(),df.index.to_pydatetime().max()])
plt.tight_layout()
plt.show()

