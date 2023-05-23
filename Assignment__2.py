#!/usr/bin/env python
# coding: utf-8

# # Assignment_2

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')
Ans: The two values of boolean data types are true and false which are written as True and False.
    Internally python evaluates true as 1 and false as 0.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2.What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')

Ans: There are two binary boolean operators namely and and or Also, there is the not operator which is the logical boolean operator which compliments the variable's current boolean value i.e. if the value of a variable is True then the not operator will return False and vice versa.


# In[ ]:





# In[ ]:


3.Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

Ans:

Truth table for and
Expression 	Evaluates to
True and True 	True
True and False 	False
False and True 	False
False and False 	False

Truth table for or
Expression 	Evaluates to
True or True 	True
True or False 	True
False or True 	True
False or False 	False

Truth table for not
Expression 	Evaluates to
not True 	False
not False 	True


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')

    (5 > 4) and (3 == 5) : Evaluates to False
    not (5 > 4) : Evaluates to False
    (5 > 4) or (3 == 5) : Evaluates to True
    not ((5 > 4) or (3 == 5)) : Evaluates to False
    (True and True) and (True == False) : : Evaluates to False
    (not False) or (not True) : : Evaluates to True

Let's verify it:


# In[1]:


(5 > 4) and (3 == 5)


# In[2]:


not (5 > 4)


# In[3]:


(5 > 4) or (3 == 5)


# In[4]:


not ((5 > 4) or (3 == 5))


# In[5]:


(True and True) and (True == False)


# In[6]:


(not False) or (not True) 


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')

Ans: There are six differnt comparison Operators which evalutes to boolean result. They are described in below table.
Operation 	Meaning
==  Equal to
<   Less than
>   Greater than
get_ipython().system('=  Not equal to')
<=  Less than or equal to
>=  Greater than or equal to


# In[ ]:





# In[ ]:


6.How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

Ans: Equal or equality operator is denoted by double equal to mark whereas assignment operator is denoted by single equal to marks.

= : this is the assignment operator

== : this is an equality operator

The assignment operator is used when we want to store some value in the variable, whereas the equality operator is used when we want to compare the values of one or more variables. The equality operator is commonly used with the if statements.

Example:


# In[7]:


a = 10 
b = 15  
print(f"a = {a}, b = {b}")
print(a == b) 
if(a == b): 
    print("a is equal to b")
else:
    print("a is not equal to b")


# In[ ]:





# In[ ]:


7.Identify the three blocks in this code:

spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')


# In[9]:


spam = 0
if spam == 10:
 print('eggs')
if spam > 5:
 print('bacon')
else:
 print('ham')
 print('spam')
 print('spam')


# In[ ]:





# In[ ]:


8.Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.


# In[10]:


spam = int(input("Please enter a value for spam: "))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
    


# In[ ]:





# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')

Ans: Pressing Ctrl+c key will terminate the endless loop.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

Ans: Below are some differences between break and continue
break                                                       
Break terminates the execution of all the remaining iteration of the loop. 
Break will resume the control of the program at the end of the loop enclosing it. 
Break can be used with switch and label 

continue
Continue will terminate only th current iteration of the loop.
Continue will resume the control of the program to the next iteration of the loop enclosing it.
Continue is not compatible with switch and label


# In[ ]:





# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

Ans: The syntax for range is range(start, stop, step) where

    strat refers to stating position/index and has default value as 0th index
    stop refers to the end position/index, mandatory argument. in the case of an iterable object, it will consider the total len of the object if not given.
    step refers to increment or decrement of position, default value is increment by 1

With this knowledge, let us understand the statement given in the problem:

    range(10) : This means iterate from default position 0 till position 9 excluding position 10
    range(0,10) : Similar to above but starting position is explicitly given as 0
    range(0,10,1) : This means iterating from starting position of 0 till 9 excluding 10 with an increment of 1 step at a time.


# In[ ]:





# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.


# In[11]:


for i in range (1,11):
    print(i)


# In[12]:


a = 1
while a <= 10:
    print(a)
    a += 1


# In[ ]:





# In[ ]:


get_ipython().set_next_input('13.If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')

Ans: We can use following lines of code to call bacon()

import spam
spam.bacon()


# In[ ]:




