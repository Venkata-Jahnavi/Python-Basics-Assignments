#!/usr/bin/env python
# coding: utf-8

# # Assignment-20

# In[ ]:





# In[ ]:


1.Set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt.
Ans:


# In[1]:


test1 =  'This is a test of the emergency text system'
print(test1)
with open('test.txt','w') as file:
    file.write(test1)
    file.close()


# In[2]:


get_ipython().system(' type test.txt')


# In[ ]:





# In[ ]:


2.Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?
Ans:


# In[3]:


with open('test.txt','r') as file:
    test2 = file.read()
print(test2)
print(test1==test2)


# In[ ]:





# In[ ]:


3.Create a CSV file called books.csv by using these lines:
title,author,year The Weirdstone of Brisingamen,Alan Garner,1960 Perdido Street Station,China Miéville,2000 Thud!,Terry Pratchett,2005 The Spellman Files,Lisa Lutz,2007 Small Gods,Terry Pratchett,1992
Ans:


# In[4]:


data = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''

with open('books.csv','w') as file:
    file.write(data)


# In[ ]:





# In[ ]:


4.Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).
Ans:


# In[8]:


import sqlite3
db = sqlite3.connect('books.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE books (title text, author text, year int)")
db.commit()
db.close()


# In[ ]:





# In[ ]:


5.Read books.csv and insert its data into the book table.
Ans:


# In[9]:


import sqlite3
import csv
conn = sqlite3.connect("books.db")
cursor = conn.cursor()
with open("books.csv","r") as file:
    books = csv.DictReader(file)
    for book in books:
        cursor.execute("INSERT INTO books VALUES (?,?,?)",(book['title'],book['author'],book['year']))
conn.commit()
conn.close()


# In[ ]:





# In[ ]:


6.Select and print the title column from the books table in alphabetical order.
Ans:


# In[10]:


import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
output = cursor.execute("SELECT title FROM books ORDER BY title ASC")
for ele in output:
    print(ele[0])
conn.commit()
conn.close()


# In[ ]:





# In[ ]:


7.From the book table, select and print all columns in the order of publication.
Ans:


# In[11]:


import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
ouput = cursor.execute("SELECT * FROM books ORDER BY year")
for record in ouput:
    print(record)


# In[ ]:





# In[ ]:


8.Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 6.
Ans:


# In[5]:


import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
conn


# In[ ]:





# In[13]:


import redis
conn = redis.Redis()
conn.hset('test',{
    'count':1,
    'name':'Fester Bestertester'
})
conn.hgetall('test')


# In[ ]:


10.Increment the count field of test and print it.
Ans:


# In[12]:


conn.hincrby('test', 'count', 1)
conn.hget('test', 'count')


# In[ ]:




