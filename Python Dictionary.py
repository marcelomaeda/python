#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dictionary


# In[2]:


fruit = {'apple':50,'banana':30,'orange':40,'peach':100}


# In[3]:


type(fruit)


# In[4]:


fruit.keys()


# In[5]:


fruit.values()


# In[6]:


fruit.items()


# In[7]:


fruit


# In[10]:


fruit['Mango']=200
fruit


# In[11]:


fruit['apple']=5
fruit


# In[12]:


fruit1 = {'apple':50,'banana':10}


# In[13]:


fruit2 = {'mango':100,'dragonfruit':500}


# In[16]:


fruit1.update(fruit2)


# In[17]:


fruit1


# In[18]:


fruit1.pop('mango')


# In[19]:


fruit1


# In[ ]:




