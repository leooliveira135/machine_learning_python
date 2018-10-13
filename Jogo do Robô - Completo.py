#!/usr/bin/env python
# coding: utf-8

# In[33]:


class Point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '<%s, %s>' %(self.x, self.y)
        
class Reward(Point):
    
    def __init__(self,x,y,name):
        super(Reward, self).__init__(x,y)
        self.name = name
        
    def __str__(self):
        return '<%s, %s>: %s' %(self.x, self.y, self.name)
    
    def __repr__(self):
        return 'Reward %s' % str(self)
        
class Robot(Point):
        
    def move_up(self):
        if self.y < 10:
            self.y = self.y + 1
        else:
            print('Movimento proibido')
        
    def move_down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print('Movimento proibido')
    
    def move_left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print('Movimento proibido')
        
    def move_right(self):
        if self.x < 10:
            self.x = self.y + 1
        else:
            print('Movimento proibido')


# In[34]:


def check_reward(robot, rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print("O robô achou a recompensa ", reward.name)
            ok = True
    return ok


# In[3]:


r1 = Reward(1,2,'moeda')
r2 = Reward(5,3,'gasolina')


# In[4]:


robo = Robot(2,2)


# In[9]:


lista = r1, r2
check_reward(robo,lista)


# In[10]:


robo.move_left()


# In[11]:


check_reward(robo,lista)


# In[18]:


import random


# In[35]:


r1 = Reward(random.randint(0,10),random.randint(0,10),'moeda')
r2 = Reward(random.randint(0,10),random.randint(0,10),'gasolina')
r3 = Reward(random.randint(0,10),random.randint(0,10),'arma')

lista = [r1,r2,r3]


# In[36]:


print(r1)


# In[37]:


lista


# In[39]:


r1.__repr__()


# In[41]:


robo = Robot(random.randint(0,10),random.randint(0,10))
robo.__str__()

