#!/usr/bin/env python
# coding: utf-8

# # Assignment_18

# In[ ]:





# In[ ]:


Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.


# In[8]:


get_ipython().system('type zoo.py')


# In[ ]:





# In[ ]:


2.In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
Ans:


# In[ ]:


import zoo as menagerie
menagerie.hours()


# In[ ]:





# In[ ]:


3.Using the interpreter, explicitly import and call the hours() function from zoo.


# In[ ]:


from zoo import hours
hours()


# In[ ]:





# In[ ]:


4.Using the interpreter, explicitly import and call the hours() function from zoo.
Ans:


# In[ ]:


from zoo import hours
hours()


# In[ ]:





# In[ ]:


5.Import the hours() function as info and call it.
Ans:


# In[ ]:


from zoo import hours as info
info()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain');get_ipython().run_line_magic('pinfo', 'plain')
Ans:


# In[ ]:


from collections import OrderedDict
fancy = OrderedDict(plain_dict)
print(f'plain_dict -> {plain_dict}')
print(f'fancy -> {fancy}')


# In[ ]:





# In[ ]:


7.Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].
Ans:


# In[ ]:


from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])

