#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Class


# In[9]:


class Phone:
    
    def __init__(self):
        pass
    
    def make_call(self):
        print("Let's make a phone call")
        
    def play_game(self):
        print("Let's play a game")


# In[10]:


p1 = Phone()


# In[11]:


p1.make_call()


# In[12]:


p1.play_game()


# In[13]:


#Adding Parameters to a Class


# In[20]:


class Phone:

    def __init__(self):
        pass
    
    def set_color(self, color):
        self.color = color
    
    def set_cost(self, cost):
        self.cost = cost
        
    def show_color(self):
        return self.color
    
    def show_cost(self):
        return self.cost
    
    def play_game(self):
        print("Playing a game")
        
    def make_call(self):
        print("Making a call")


# In[21]:


p2 = Phone()


# In[22]:


p2.set_color('blue')


# In[23]:


p2.set_cost(500)


# In[24]:


p2.show_color()


# In[25]:


p2.show_cost()


# In[26]:


p2.play_game()


# In[27]:


p2.make_call()


# In[ ]:




