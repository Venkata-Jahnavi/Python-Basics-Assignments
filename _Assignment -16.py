#!/usr/bin/env python
# coding: utf-8

# #  Assignment 16

# In[ ]:





# In[ ]:


1.Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].
Ans:


# In[2]:


years_list = [1998,1999,2000,2001,2002,2003]
print(years_list )


# In[ ]:





# In[ ]:


2.In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.


# In[3]:


years_list[3]


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.In the years list, which year were you the oldest');get_ipython().run_line_magic('pinfo', 'oldest')

Ans:


# In[ ]:


years_list[5]


# In[ ]:





# In[ ]:


4.Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
Ans:


# In[5]:


things=["mozzarella", "cinderella", "salmonella"]
print(things)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list');get_ipython().run_line_magic('pinfo', 'list')
Ans:


# In[6]:


things[1].upper()


# In[ ]:





# In[ ]:


6.Make a surprise list with the elements "Groucho," "Chico," and "Harpo."
Ans:


# In[8]:


surprice_list=[ "Groucho", "Chico","Harpo"]
print(surprice_list)


# In[ ]:





# In[ ]:


7.owercase the last element of the surprise list, reverse it, and then capitalize it.
Ans:


# In[9]:


surprice_list[2][::-1].upper()


# In[ ]:


8.Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.


# In[11]:


etf={"dog" : "chien", "cat" : "chat",  "walrus" : "morse"}


# In[ ]:





# In[ ]:


9.Write the French word for walrus in your three-word dictionary e2f.


# In[12]:


etf["walrus"]= "morse"


# In[ ]:





# In[ ]:


10.Make a French-to-English dictionary called f2e from e2f. Use the items method.


# In[13]:


fte= etf.items()


# In[ ]:





# In[ ]:


11.Print the English version of the French word chien using f2e.
Ans:


# In[14]:


fte


# In[ ]:





# In[ ]:


12.Make and print a set of English words from the keys in e2f.
Ans:


# In[15]:


etf.keys()


# In[ ]:





# In[ ]:


13.Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.


# In[16]:


life={'animals':{'cats':{'Henri', 'Grumpy' ,'Lucy'},'octopi':{},'emus':{}}}


# In[ ]:





# In[ ]:


14.Print the top-level keys of life.


# In[17]:


life.keys()


# In[ ]:





# In[ ]:


15.rint the keys for life['animals'].
Ans:


# In[18]:


for key in life["animals"]:
    print(key)


# In[ ]:





# In[ ]:


16.Print the values for life['animals']['cats']
Ans:


# In[19]:


for key in life["animals"]['cats']:
    print(key)


# In[ ]:




