#!/usr/bin/env python
# coding: utf-8

# # Assignment_1

# In[ ]:





# In[ ]:


In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
*
'hello'
-87.8
-
()
+
6


# In[ ]:


#ANS:

VALUES :
    -87.8
    6
    'HELLO'
EXPRESSIONS : 
    *
    -
    ()
    +
    


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')

ANS:  Variables are symbols that you can use to store data in a program. 
     we can think of them as an empty box that we fill with some data or value.
        Strings are data, so we can use them to fill up a variable.


# In[ ]:





# In[ ]:


3. Describe three different data types.

Ans:

    int: Integer datatype, represented as int. These are used to store the whole number without a fraction.
    str: String datatype, represented as str. These are used to store a list of one or more Unicode characters.
    bool: Boolean datatype, represented as a bool. These are used to store True or False values.

Examples:
     


# In[5]:


a = 11
b = "Hello"
c = False

print(f"{a} is of type {type(a)}")
print(f"{b} is of type {type(b)}")
print(f"{c} is of type {type(c)}")


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')

Ans: An expression is made up of a combination of operators and operands (values i.e. int, float, string etc.) Expression should always have atleast one operator.
    Once we evaluate the expression it perform the necssary calculation/computation on the operands and display the reult.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.This assignment statements, like spam = 10. What is the difference between an expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')

Ans: We can safely state that an expression is a subset of a statement but not vice e versa.
    An expression always gets evaluated and returns the evaluated result. But a statement can be just and declaration and assignment of a variable which not necessarily need to be evaluated and returns the result.


# In[8]:


a = 10 
b = a + 5
b


# In[ ]:





# In[ ]:


get_ipython().set_next_input('6.After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')

bacon = 22
bacon + 1

Ans: Here bacon is assigned a int value 22. And second statement is an expression bacon + 1. But as an expression evalutes and returns a result, that result should be stored in some variable otherwise it will be lost. Here we are not storing result evaluted by bacon + 1 in any variable hence it will be lost. The original bacon variable will be still be holding int value 22


# In[9]:


bacon = 22
bacon + 1
print(bacon)


# In[ ]:





# In[ ]:




get_ipython().set_next_input('7.What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')

'spam' + 'spamspam'
'spam' * 3


# In[10]:


'spam' + 'spamspam'


# In[12]:


'spam' * 3


# In[ ]:


Here both expressions evaluate to the same result albeit using two different techniques.
The first technique is simple string concatenation whereas the second one is string multiplication.


# In[ ]:


get_ipython().set_next_input('8.Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')

Ans: There are some rules defined in python for naming variables, those are as follows:

    Variable names should start with alphabets or underscore.
    Variable names should not contain any special characters excluding underscores.
    Variable names can contain numbers but can't start with numbers.
    Variable names are case-sensitive.
    Variable names must not contain any space.
    Variable names must not be one of the reserved words in python.

Hence eggs is the valid variable name but 100 is not since it violates rules 1 and 3.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('9.What three functions can be used to get the integer, floating-point number, or string version of a value');get_ipython().run_line_magic('pinfo', 'value')

Ans: Using int(), float(), str() we can get integer, float and string version of the value.


# In[13]:


a = 15
print(f"integer value of a is {int(a)} type : {type(int(a))}")
print(f"float value of a is {float(a)} type : {type(float(a))}")
print(f"string value of a is {str(a)} type : {type(str(a))}")


# In[ ]:





# In[ ]:


get_ipython().set_next_input('10.Why does this expression cause an error? how can you fix it');get_ipython().run_line_magic('pinfo', 'it')

'I have eaten ' + 99 + ' burritos.'

Ans:


# In[14]:


'I have eaten ' + 99 + ' burritos.'


# In[16]:


'I have eaten ' + str(99) + ' burritos'


# In[ ]:




