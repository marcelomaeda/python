#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Functions


# In[2]:


def hello():
    print("Hello")


# In[3]:


hello()


# In[4]:


# Function with parameter


# In[5]:


def add10(x):
    return x+10


# In[6]:


add10(10)


# In[7]:


def even_odd(x):
    if x%2==0:
        print(x, " is even")
    else:
        print(x, "is odd")


# In[8]:


even_odd(5)


# In[9]:


#Lambda functions


# In[10]:


g = lambda x: x*x*x
print(g(7))


# In[11]:


#Lambda functions with filter
li = [5,7,22,97,54,62,77,23,73,61]
final_list = list(filter(lambda x: (x%2 != 0), li))
print(final_list)


# In[12]:


#Lambda functions with map
li = [5,7,22,97,54,62,77,23,73,61]
final_list = list(map(lambda x: x*2, li))
print(final_list)


# In[13]:


from functools import reduce
li = [5,8,10,20,50,100]
sum = reduce((lambda x, y: x+y), li)
print(sum)


# In[ ]:




