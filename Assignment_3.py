#!/usr/bin/env python
# coding: utf-8

# # Assignment_3

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.Why are functions advantageous to have in your programs');get_ipython().run_line_magic('pinfo', 'programs')

Ans: Below are some advantages of using functions in a program:

    Function can eliminate the duplication of code by allowing the reuse of the code
    Function improve the clarity and readability of the code.
    Function can make code easy to understand by breaking complex logic into smaller chunks
    Breaking code into smaller chunks also helps in maintaining the code and updating specific parts of code becomes easier.
    Function can be used to hide certain information if needed.


# In[ ]:





# In[ ]:


get_ipython().set_next_input("2.When does the code in a function run: when it's specified or when it's called");get_ipython().run_line_magic('pinfo', 'called')

Ans: For executing the function, we need to call the function. When the function is specified it just creates its definition and did not run it.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3.What statement creates a function');get_ipython().run_line_magic('pinfo', 'function')

Ans: Function can be created by using keyword def. Below is basic function sytnax:

def functionname():
    dosomething
    return


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.What is the difference between a function and a function call');get_ipython().run_line_magic('pinfo', 'call')

Ans: Function is the reusable definition of the code block. To use this code block and get the desired result we will need to execute the function, this process of executing the function is called Function Call.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.How many global scopes are there in a Python program? How many local scopes');get_ipython().run_line_magic('pinfo', 'scopes')

Ans:

There is only one Global scope in python. The variable defined in the global scope can be accessed anywhere throughout the program.

Local scope is the scope of a variable defined within a function. Its scope lies only with the function, it is not accessible outside of the function. New local scope is created whenever a function is called, so the numbers of total local scopes depend on the number of function calls.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('6.What happens to variables in a local scope when the function call returns');get_ipython().run_line_magic('pinfo', 'returns')

Ans: When the function call returns or completes the local scope for that function is destroyed. Since the local scope no longer exists, the variables in that function are lost and no longer accessible.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('7.What is the concept of a return value? Is it possible to have a return value in an expression');get_ipython().run_line_magic('pinfo', 'expression')

Ans: return is special statement used in functions which can be used to send the function's result back to the caller. The return value can be of any python object and yes they can be used in the expressions.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('8.If a function does not have a return statement, what is the return value of a call to that function');get_ipython().run_line_magic('pinfo', 'function')

Ans: If function does not have a return statement, then the return value of function will be None


# In[ ]:





# In[ ]:


get_ipython().set_next_input('9.How do you make a function variable refer to the global variable');get_ipython().run_line_magic('pinfo', 'variable')

Ans: Global variables are accessible throughout the program. In case you want to make the function variable global and allow it to use outside of the function's local scope then we can use the keyword global to force the function variable to act as a global variable.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('10.What is the data type of None');get_ipython().run_line_magic('pinfo', 'None')

Ans: The data type of None is NoneType.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('11.What does the sentence import areallyourpetsnamederic do');get_ipython().run_line_magic('pinfo', 'do')

Ans:

import areallyourpetsnamederic

will import all the methods and code from the module areallyourpetsnamederic.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('12.If you had a bacon() feature in a spam module, what would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')

Ans: the function can be called using follwing code lines:

import spam
spam.bacon()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('13.What can you do to save a programme from crashing if it encounters an error');get_ipython().run_line_magic('pinfo', 'error')

Ans: We can enclose the code which is causing error in a try and use except to catch and handle the error.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('14.What is the purpose of the try clause? What is the purpose of the except clause');get_ipython().run_line_magic('pinfo', 'clause')

Ans: The purpose of try is to prevent the program from crashing due to unexpected and unhandled error. If any unhandled error in encounter in try block it goes to 'except' block where we can take appropriate action to gracefully handle the error and prevent break into program flow.


# In[ ]:




