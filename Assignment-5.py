#!/usr/bin/env python
# coding: utf-8

# # Assignment-5

# In[ ]:


get_ipython().set_next_input("1.What does an empty dictionary's code look like");get_ipython().run_line_magic('pinfo', 'like')

Ans: 
    
    An empty dictionary is often represented by two empty curly brackets
    d = {} or d = dict()


# In[ ]:





# In[ ]:


2.what is the value of dictionary value with key 'foo' and the value 42 ?
Ans: 
    
    The value of a dictionary value with the key 'foo' and the value 42 is {'foo': 42}


# In[4]:


dic = {'foo':42}
dic


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.What is the most significant distinction between a dictionary and a list');get_ipython().run_line_magic('pinfo', 'list')
Ans: 
     Dictionaries are represented by {} where as listed are represented by []
     The Items stored in a dictionary are Unordered , while the items in a list are ordered


# In[ ]:





# In[ ]:


4.What happens if you try to access spam ['foo'] if spam is {'bar':100} ?
Ans:
    The output box will show a keyError KeyError: 'foo',like the bwlow one


# In[5]:


spam = {'bar': 100}
spam['foo']


# In[ ]:





# In[ ]:


5.if a dictionary is stored in spam,what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys() ?
Ans:
    There is no difference . The operator checks whether a value exits as a key in the dictionary or not


# In[ ]:





# In[ ]:


6.if a dictionary is stored in spam,what is the difference between the
expressions 'cat' in spam and 'cat' in spam.values() ?

Ans:'cat' in spam checks whether there is a 'cat' key in the dictionary, 
    while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.


# In[ ]:





# In[ ]:


7.what is a shortcut for the following code ?
if 'color' not in spam: spam['color'] ='black'

Ans: 
    spam.setdefault('color','black')


# In[8]:


spam.setdefault('color','black')


# In[ ]:





# In[ ]:


8.How do you 'pretty print' dictionary values using which modules and function ?
Ans:
    we can pretty print a dictionary using 

        by using pprint() function of pprint module.
        
Note: pprint() function doesnot prettify nested dictionaries

