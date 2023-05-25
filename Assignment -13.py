#!/usr/bin/env python
# coding: utf-8

# # Python Assignment -13

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1.What advantages do Excel spreadsheets have over CSV spreadsheets');get_ipython().run_line_magic('pinfo', 'spreadsheets')
Ans:
    The Advantages of Excel over CSV are:

1) Excel (XLS and XLSX) file formats are better for storing and analysing complex data. 
2) An Excel not only stores data but can also do operations on the data using macros, formulas etc 
3) CSV files are plain-text files, Does not contain formatting, formulas, macros, etc. It is also known as flat files


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2.What do you pass to csv.reader() and csv.writer() to create reader and writer objects');get_ipython().run_line_magic('pinfo', 'objects')
Ans:
    We pass the object of the file which we have open or on wich file operation needs to be performed.mfro examle open(filename, 'r') as csvfile: # creating a csv reader object csvreader = csv.reader(csvfile)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3. What modes do File objects for reader and writer objects need to be opened in');get_ipython().run_line_magic('pinfo', 'in')
Ans: 
    
    For csv.reader(iterable_file_object), the file objects needed to be opened in read mode mode='r'
    Whereas for csv.writer(iterable_file_object) the file objects needed to be opened in write mode mode='w'


# In[ ]:


get_ipython().set_next_input('4.hat method takes a list argument and writes it to a CSV file');get_ipython().run_line_magic('pinfo', 'file')
Ans:

The csv. writer writerow method takes an iterable as an argument. The result set has to be a list (rows) of lists (columns)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.What do the keyword arguments delimiter and line terminator do');get_ipython().run_line_magic('pinfo', 'do')
Ans:
    Lets take the example of a csv file: First Name, Last Name, Age Mano, Vishnu, 24 Vishnu, Vardhan, 21 Here ',' is Delimiter. We can use any Character as per our needs if required. Similarly Line Terminator comes at end of line by default it is newline and can be changed accourding to Requirement.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('6. What function takes a string of JSON data and returns a Python data structure');get_ipython().run_line_magic('pinfo', 'structure')
Ans: 
    loads() method takes a string of JSON data and returns a Python data structure


# In[ ]:





# In[ ]:


get_ipython().set_next_input('7. What function takes a Python data structure and returns a string of JSON data');get_ipython().run_line_magic('pinfo', 'data')
Ans: 
    dumps() method takes a python data structure and returns a string of JSON data

