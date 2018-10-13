#!/usr/bin/env python
# coding: utf-8

# In[145]:


class Point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y


# In[146]:


class Reward(Point):
    
    def __init__(self,x,y,name):
        super(Reward, self).__init__(x,y)
        self.name = name


# In[151]:


reward1 = Reward(1,1,'moeda de ouro')


# In[152]:


print(reward1.x)
print(reward1.name)


# In[149]:


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


# In[150]:


r1 = Robot(5,5)


# In[144]:


r1.y


# In[143]:


r1.move_up()


# In[6]:


robo1 = Robo(10,10)
type(robo1)
robo1.x
robo1.y


# In[20]:


robo2 = Robo3D(5,6,8)
robo2.print_x()


# In[18]:


class Robo3D(Robo):
    
    def __init__(self,x,y,z):
        super(Robo3D, self).__init__(x,y)
        self.z = z

