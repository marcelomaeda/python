#!/usr/bin/env python
# coding: utf-8

# In[1]:


#if


# In[5]:


a=10
b=20


# In[6]:


if a>b:
    print("a is > than b")


# In[7]:


if b>a:
    print("b is > a")


# In[8]:


if a>b:
    print("a is > b")
else:
    print("b is > a")


# In[9]:


a=10
b=20
c=30


# In[11]:


if (a>b & a>c):
    print("a is >>>")
elif (b>a & b>c):
    print("b is >>>")
else:
    print("c is >>>")


# In[12]:


#if with list


# In[18]:


l1 = [1,2,3,4,5]


# In[19]:


if l1[1]==2:
    l1[1]=l1[1]+100


# In[20]:


l1


# In[21]:


if l1[4]==10:
    l1[1]=l1[1]+100
else:
    l1[4]=l1[4]+500


# In[22]:


l1


# In[23]:


#if with dictionary


# In[24]:


d1 = {"a":1,"b":2,"c":3}


# In[25]:


if d1["b"]==2:
    d1["b"]=d1["b"]+100


# In[26]:


d1


# In[ ]:




