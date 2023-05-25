#!/usr/bin/env python
# coding: utf-8

# # Assignment-11
# 

# In[ ]:


1. Create an assert statement that throws an AssertionError if the variable spam is a negative integer.


# In[1]:


spam = -22
assert spam >=0, 'Variable Spam should not be a -ve number'


# In[ ]:





# In[ ]:


2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).


# In[3]:


def raise_assert(egg,bacon):
    egg = egg.upper()
    bacon = bacon.upper()
    assert not(egg == bacon), 'Eggs/Bacon should not be same, which are same now'


# In[4]:


assertionErr()


# In[ ]:





# In[ ]:


3.Create an assert statement that throws an AssertionError every time.


# In[5]:


def assertFalse():
    assert False,"Assertion will aleays be false"


# In[6]:


assertFalse()


# In[ ]:





# In[ ]:


4. What are the two lines that must be present in your software in order to call logging.debug()?
Ans:
    import logging
logging.basicConfig(filename = 'application_log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt');get_ipython().run_line_magic('pinfo', 'programLog.txt')
Ans:
    import logging
>>> logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
format=' %(asctime)s - %(levelname)s - %(message)s')


# In[ ]:





# In[ ]:


get_ipython().set_next_input('6. What are the five levels of logging');get_ipython().run_line_magic('pinfo', 'logging')
Ans: The Five levels of Logging provided by python's 
    logging module are CRITICAL(50), ERROR(40), WARNING(30), INFO(20, DEBUG(10), NOTSET(0)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('7.What line of code would you add to your software to disable all logging messages');get_ipython().run_line_magic('pinfo', 'messages')
Ans:
    The following statement will be :- logging.disable(logging.CRITICAL)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('8.Why is using logging messages better than using print() to display the same message');get_ipython().run_line_magic('pinfo', 'message')

Ans:-You can disable logging messages without removing the logging function calls.
    You can selectively disable lower-level logging messages. You can create logging messages. Logging messages provides a timestamp.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('9.What are the differences between the Step Over, Step In, and Step Out buttons in the debugger');get_ipython().run_line_magic('pinfo', 'debugger')
Ans: 
    The Differences between Step Over, Step In, Step Out buttons in debugger are:

Step in - Step In button will cause the debugger to execute the next line of code and then pause again.
Step Over - Step Over button will execute the next line of code, similar to the Step In button. However, if the next line of code is a function call, the Step Over button will “step over” the code in the function. The function’s code will be executed at full speed, and the debugger will pause as soon as the function call returns.
Step out - Step Out button will cause the debugger to execute lines of code at full speed until it returns from the current function.


# In[ ]:





# In[ ]:


10.After you click Continue, when will the debugger stop ?
Ans: 
    This will cause the program to continue running normally, 
    without pausing for debugging untill it terminates or reaches a breakpoint.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('11. What is the concept of a breakpoint');get_ipython().run_line_magic('pinfo', 'breakpoint')
Ans: 
    Breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line

