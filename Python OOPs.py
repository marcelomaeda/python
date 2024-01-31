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


# In[28]:


#Class with Constructor


# In[37]:


class Employee:    
    def __init__(self,name,age,salary,gender):        
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        
    def show_details(self):
        print("The name of the Employee is ", self.name)
        print("The age of the Employee is ", self.age)
        print("The salary of the Employee is ", self.salary)
        print("The gender of the Employee is ", self.gender)


# In[38]:


e1 = Employee('Julia', 25, 112000, 'Female')


# In[39]:


e1.show_details()


# In[40]:


#Inheritance 


# In[44]:


class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost
        
    def show_details(self):
        print("Vehicle")
        print("The mileage is: ", self.mileage)
        print("The cost is ", self.cost)


# In[45]:


v1 = Vehicle(300,1000)


# In[46]:


v1.show_details()


# In[47]:


class Car(Vehicle):
    def show_car_details(self):
        print("I am a car")


# In[48]:


c1 = Car(100,2000)


# In[50]:


c1.show_details()


# In[51]:


c1.show_car_details()


# In[52]:


#Over riding init method


# In[53]:


class Car(Vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost) # parent class
        self.tyres = tyres
        self.hp = hp
        
    def show_car_details(self):
        print("I am a car")
        print("Number of tyres are ", self.tyres)
        print("Value of horse power is ", self.hp)


# In[54]:


c1 = Car(500,5000,8,200)


# In[55]:


c1.show_details()


# In[56]:


c1.show_car_details()


# In[57]:


#Types of Inheritance
#Single, Multiple, Multi-level and Hybrod


# In[58]:


class Parent1:
    def __init__(self):
        self.str1 = ""
        
    def assign_str1(self,str1):
        self.str1 = str1
        
    def show_str1(self):
        print(self.str1)


# In[59]:


class Parent2:   
    def __init__(self):
        self.str2 = ""
        
    def assign_str2(self,str2):
        self.str2 = str2
        
    def show_str2(self):
        print(self.str2)


# In[60]:


class Child(Parent1,Parent2):
    def __init__(self):
        super().__init__()
        self.str3 = ""
        
    def assign_str3(self,str3):
        self.str3 = str3
        
    def show_str3(self):
        print(self.str3)


# In[61]:


c1 = Child()


# In[62]:


c1.assign_str1("Movie")
c1.assign_str2("Movieeeeeeee")
c1.assign_str3("Hello Movie")


# In[81]:


c1.show_str1()


# In[79]:


c1.show_str2()


# In[80]:


c1.show_str3()


# In[82]:


#Multi-level Inheritance


# In[94]:


class Person:
	def __init__(self):
		print('Person - Hii')


	def age(self, a):
		print('Printing the age: ', a)


class Father(Person):
	def __init__(self):
		print('Father - Hii')
		super().__init__()


	def age(self, a):
		print('Printing the age(Father): ', a)
		super().age(a - 1)


class Mother(Father):
	def __init__(self):
		print('Mother - Hii')
		super().__init__()


	def age(self, a):
		print('Printing the age(Mother): ', a)
		super().age(a + 5)


# Main function
if __name__ == '__main__':
	o = Mother()
	o.age(30)


# In[84]:





# In[85]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




