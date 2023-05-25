#!/usr/bin/env python
# coding: utf-8

# # Assignment-21

# In[ ]:





# In[ ]:


1.Add the current date to the text file today.txt as a string.
Ans:


# In[1]:


import datetime
# Code to Add current date to the today.txt file
file = open('today.txt','w')
file.write(datetime.datetime.now().strftime("%d-%m-%Y"))
file.close()
# Code to Read current date from today.txt file
file = open('today.txt','r')
print(file.read())
file.close()


# In[ ]:





# In[ ]:


2.Read the text file today.txt into the string today_string
Ans:


# In[2]:


file = open('today.txt','r')
today_string = file.read()
print(today_string)


# In[ ]:





# In[ ]:


3.Parse the date from today_string.
Ans:


# In[3]:


from datetime import datetime
parsed_data = datetime.strptime(today_string, '%d-%m-%Y')
print(parsed_data)


# In[ ]:





# In[ ]:


4.List the files in your current directory
Ans:


# In[4]:


import os
for folders, subfolders, files in os.walk(os.getcwd()):
    for file in files:
        print(file)


# In[ ]:





# In[ ]:


5.Create a list of all of the files in your parent directory (minimum five files should be available).
Ans:


# In[5]:


import os 
os.listdir()


# In[ ]:





# In[ ]:


6.Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.
Ans:


# In[6]:


import multiprocessing
import time 
import random
import datetime


# In[ ]:





# In[ ]:


7.Create a date object of your day of birth.
Ans:


# In[7]:


from datetime import datetime
my_dob = datetime.strptime('22/04/1997','%d/%m/%Y')
print(my_dob, type(my_dob))


# In[ ]:





# In[ ]:


get_ipython().set_next_input('8.What day of the week was your day of birth');get_ipython().run_line_magic('pinfo', 'birth')
Ans:


# In[8]:


from datetime import datetime
my_dob = datetime(1997,4,22)
my_dob.strftime("%A")


# In[ ]:





# In[ ]:


get_ipython().set_next_input('9.When will you be (or when were you) 10,000 days old');get_ipython().run_line_magic('pinfo', 'old')
Ans:


# In[9]:


from datetime import datetime, timedelta
my_dob = datetime.strptime("22/04/1997",'%d/%m/%Y')
future_date = my_dob-timedelta(10000)
future_date

