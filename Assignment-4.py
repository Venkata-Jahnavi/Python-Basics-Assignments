#!/usr/bin/env python
# coding: utf-8

# # Assignment-4

# In[ ]:


1.What exactly is [ ]?
Ans: 

[ ] - The square brackets are used to represent / declare a list data type.
since the square brackets are empty that means they are not containing any values  or items so its a "empty list

Usually to declare a list we use square brackets [ ] , after the name of the list

#example:
list_name[]


# In[ ]:





# In[ ]:


2.In a list of values stored in a variable called spam, 
how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

Ans:
    spam[2] = 'hello'

    The expalnation for the answer is given below.


# In[1]:


# lets now constuct a list with given values in the question

spam = [2, 4, 6, 8, 10]
print(spam)


# In[2]:


#the task given in the question is to add 'hello' as the third vslue in the list,
#the index number of the third value in the list is  2  , so we need to insert the 'hello' @ index value-2

spam[2] = 'hello'

print(spam)


# In[ ]:


#the desired output is achieved.


# In[ ]:





#  ## Let's pretend the spam includes the list ['a','b','c',d'] for the next three queries.# 

# In[5]:


spam=['a','b','c','d']


# In[ ]:


3. What is the value of spam[int(int('3'*2)//11)] ?
    Ans: 'd'
        
        The expalnation for the answer is given below.


# In[3]:


[int(int('3'*2)//11)] 


# In[6]:


spam[3]


# In[ ]:





# In[ ]:


4.What is the value of spam[-1]?
Ans:"d"
    The expalnation for the answer is given below.
    


# In[7]:


spam[-1]#negative indexing


# In[ ]:





# In[ ]:


5. What is the value of spam[:2]?
Ans:
    ['a', 'b']
    
    The expalnation for the answer is given below.


# In[8]:


spam[:2]


# In[ ]:





# # Let's pretend bacon has the list [3.14,'cat',11,'cat',True] for the next three question

# In[18]:


bacon = [3.14,'cat',11,'cat',True]


# In[ ]:


6. What is the value of bacon.index('cat')?

Ans: '1'
    
    The expalnation for the answer is given below.


# In[19]:


bacon.index('cat')


# In[ ]:





# In[ ]:


get_ipython().set_next_input('7. How does bacon.append(99) change the look of the list value in bacon');get_ipython().run_line_magic('pinfo', 'bacon')
Ans: 
    bacon.append(99) adds 99 at the end of the list named- 'bacon' as we know the append function adds a value at the end of the list   
    
    
    The expalnation for the answer is given below.


# In[20]:


bacon#before bacon.append(99)


# In[21]:


bacon.append(99) # appending 99
bacon


# In[ ]:





# In[ ]:


get_ipython().set_next_input("8. How does bacon.remove('cat') change the look of the list in bacon");get_ipython().run_line_magic('pinfo', 'bacon')

Ans : 
     bacon.remove('cat') - it removes 'cat' value from the list - 'bacon'


# In[23]:


bacon.remove('cat') # remove fumction removes cat from the list
bacon


# In[ ]:





# In[ ]:


get_ipython().set_next_input('9.what are the list concatenation and list replication operations');get_ipython().run_line_magic('pinfo', 'operations')
Ans:
    
The operator for list concatenation is +, while the operator for replication is *.

The demonstration of the above two functions can help us  understand them better bb the following example.


# In[24]:


list_1 = ['Arun','Kumar','Ashok','Bavaji','Simon']
list_2 = ['Praveen','Phani','Saii']
print(list_1 + list_2) # List Concatenation
print(list_2*2) # List Replication


# In[ ]:


get_ipython().set_next_input('11. What are the two methods for removing items from a list');get_ipython().run_line_magic('pinfo', 'list')
Ans: 
    The del statement and the remove() method are two ways to remove values from a list
    
    We have already used remove function in Q8.


# In[ ]:





# In[ ]:


12. Describe how list values and string values are identical.
Ans:
    Both lists and strings can be passed to len() function, have indexes and slices, 
    be used in for loops, be concatenated or replicated, and be used with the in and not in operators.


# In[ ]:





# In[ ]:


get_ipython().set_next_input("13. What's the difference between tuples and lists");get_ipython().run_line_magic('pinfo', 'lists')

Ans: 
    Lists are Mutable, Indexable and Slicable. they can have values added, removed, or changed. 
    Tuples are Immutable but Indexable and Slicable. the tuple values cannot be changed at all. 
    Also, tuples are represented using parentheses, (), while lists use the square brackets, [].


# In[ ]:





# In[ ]:


14. How do you type a tuple value that only contains the integer 42?
Ans:
    (42,)


# In[26]:


tuple1=(42)
tuple2=(42,)
print(type(tuple))
print(type(tuple2))


# In[ ]:





# In[ ]:


get_ipython().set_next_input("15. How do you get a list value's tuple form? How do you get a tuple value's list form");get_ipython().run_line_magic('pinfo', 'form')
Ans: 
    
    The tuple() and list() functions, respectively are used to convert a list to tuple and vice versa
    
    Example:


# In[28]:


#Convert list to tuple
listx = [1, 2, 3, 4, 5]
print(listx)
#use the tuple() function built-in Python, passing as parameter the list
tuplex = tuple(listx)
print(tuplex)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain');get_ipython().run_line_magic('pinfo', 'contain')
Ans: 
    They contain references to list values.


# In[ ]:





# In[ ]:


7. How do you distinguish between copy.copy() and copy.deepcopy()?

Ans:
    The copy.copy() function will do a shallow copy of a list,
    while the copy.deepcopy() function will do a deep copy of a list. 
    That is, only copy.deepcopy() will duplicate any lists inside the list.

