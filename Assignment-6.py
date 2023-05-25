#!/usr/bin/env python
# coding: utf-8

# # Assignment-6

# In[ ]:


1.What are Escape characters ? and how do you use them ?

Ans:
    
Escape characters represent characters in string values that would otherwise be difficult or impossible to type into code.
The escape character allows yus to use double quotes when you normally would not be allowed.


# In[2]:


answer = "I am from  \"Andhra\" Puttaparthi."
print(answer) 


# In[ ]:





# In[ ]:


2.What do the escape characters n and t stand for ?
Ans: 
    
    \n is a newline, \t is a tab


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.What is the way to include backslash character in a string');get_ipython().run_line_magic('pinfo', 'string')
Ans: 
    The \ escape character will represent a backslash character.


# In[ ]:





# In[ ]:


4.The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not
escaped a problem ?

Ans:
    The single quote in Howl's is fine because we have used double quotes to mark the beginning and end of the string.


# In[ ]:





# In[ ]:


get_ipython().set_next_input("5.How do you write a string of newlines if you don't want to use the n character");get_ipython().run_line_magic('pinfo', 'character')
Ans: 
    Multiline string allow you to use newlines in string without the \n escape character


# In[ ]:





# In[ ]:


6.What are the values of the given expressions ?
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]

Ans:
    
The values for the given expressions are:
'Hello, world!'[1] -> 'e'
'Hello, world!'[0:5] -> 'Hello'
'Hello, world!'[:5] -> 'Hello'
'Hello, world!'[3:] -> 'lo, world!'


# In[5]:


'Hello, world!'[1]


# In[6]:


'Hello, world!'[0:5]


# In[7]:


'Hello, world!'[:5]


# In[8]:


'Hello, world!'[3:]


# In[ ]:





# In[ ]:


7.What are the values of the following expressions ?
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()

Ans:
The values for the given expressions are:
'Hello'.upper() -> 'HELLO'
'Hello'.upper().isupper() -> True
'Hello'.upper().lower() -> 'hello'


# In[10]:


'Hello'.upper()


# In[11]:


'Hello'.upper().isupper()


# In[12]:


'Hello'.upper().lower()


# In[ ]:





# In[ ]:


8.What are the values of the following expressions ?
'Remember, remember, the fifith of July.'.split()
-'.join('There can only one'.split())

Ans:
    ['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.'] There-can-only-one.


# In[13]:


'Remember, remember, the fifth of July.'.split()


# In[14]:


'-'.join('There can only one.'.split())


# In[ ]:





# In[ ]:


9.What are the methods for right-justifying, left-justifying and centering a string ?
Ans: 
    
    The rjust(),ljust(),center() string methods, respectively


# In[ ]:





# In[ ]:


10.What is the best way to remove whitespace characters from the start or end ?
Ans:
    
    The lstrip() and rstrip() methods remove whitesapce characters from the left and right ends of a string respectively

