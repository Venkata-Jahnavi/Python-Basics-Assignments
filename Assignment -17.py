#!/usr/bin/env python
# coding: utf-8

# # Assignment -17

# In[ ]:





# In[ ]:


1.Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.
Ans:


# In[1]:


guess_me = 7
if guess_me < 7:
    print("too Low")
elif guess_me > 7:
    print("too high")
elif guess_me == 7:
    print('just right')


# In[ ]:





# In[ ]:


2.Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while loop that compares start with guess_me. Print too low if start is less than guess me. If start equals guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of the loop.
Ans:


# In[2]:


guess_me = 7
start = 1
while start <= 7:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    elif start > guess_me:
        print('oops')
        break
    start = start+1


# In[ ]:





# In[ ]:


3.Print the following values of the list [3, 2, 1, 0] using a for loop.
Ans:


# In[3]:


i=3
while i>=0:
    print(i)
    i = i-1


# In[ ]:





# In[ ]:


4.Use a list comprehension to make a list of the even numbers in range(10)
Ans:


# In[4]:


[x for x in range(10) if x%2 ==0]


# In[ ]:





# In[ ]:


5.Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the square of each key as its value.
Ans:


# In[5]:


{num : num*num for num in range(1,10)}


# In[ ]:





# In[ ]:


6.Construct the set odd from the odd numbers in the range using a set comprehension (10).
Ans:


# In[6]:


{x for x in range(10) if x%2 ==0}


# In[ ]:





# In[ ]:


7.Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). Iterate through this by using a for loop.
Ans:


# In[7]:


Got = (i for i in range(10) )
Got


# In[ ]:





# In[ ]:


8.Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].
Ans:


# In[8]:


def good():
    return ['Harry', 'Ron', 'Hermione']


# In[ ]:





# In[ ]:


9.Define a generator function called get_odds that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.
Ans:


# In[9]:


get_odds = (i for i in  range(10) if i%2 != 0)
get_odds


# In[ ]:





# In[ ]:


10.Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch this exception and print 'Caught an oops'.
Ans:


# In[10]:


class OopsException(Exception):
    pass
def exceptioncheck():
    try:
        raise OopsException
    except Exception as e:
        print('Caugnt an Exception')


# In[ ]:





# In[ ]:


11.Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].
Ans:


# In[11]:


titles =  ['Creature of Habit', 'Crewel Fate'] 
plots =  ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles,plots))
movies

