#!/usr/bin/env python
# coding: utf-8

# # Assignment-7
# 

# In[ ]:


get_ipython().set_next_input('1. What is the name of the feature responsible for generating Regex objects');get_ipython().run_line_magic('pinfo', 'objects')
Ans:
    
    re.compile() is the feature responsible for generation of Regex objects.


# In[2]:


import re
x = re.compile("random_pattern")
type(x)
print(x)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2. Why do raw strings often appear in Regex objects');get_ipython().run_line_magic('pinfo', 'objects')
Ans:
    Raw strings are used so that backslashes do not have to be escaped.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3. What is the return value of the search() method');get_ipython().run_line_magic('pinfo', 'method')
Ans:
    
    The return value of re.search(pattern,string) method is a match object if the pattern is observed in 
the string else it returns a None


# In[3]:


import re
match = re.search('i','Ineuron Full Stack Data Science Program', flags=re.IGNORECASE)
print('Output:',match)
match = re.search('X','Ineuron Full Stack Data Science Program', flags=re.IGNORECASE)
print('Output:',match)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4. From a Match item, how do you get the actual strings that match the pattern');get_ipython().run_line_magic('pinfo', 'pattern')
Ans: 
    For Matched items group() methods returns actual strings that match the pattern


# In[4]:


import re
match = re.search('ineuron','Ineuron Full Stack Data Science Program', flags=re.IGNORECASE)
print('Output:',match.group())


# In[ ]:





# In[ ]:


5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover? Group 2? Group 1?
Ans: In the Regex r'(\d\d\d)-(\d\d\d-\d\d\d\d)' the zero group covers the entire pattern match where as the first group cover 
    (\d\d\d) and the second group cover (\d\d\d-\d\d\d\d)


# In[6]:


import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 630-076-3758.')
print(mo.groups()) # Prints all groups in a tuple format
print(mo.group()) # Always returns the fully matched string 
print(mo.group(1)) # Returns the first group
print(mo.group(2)) # Returns the second group


# In[ ]:





# In[ ]:


6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell a regex that 
get_ipython().set_next_input('you want it to fit real parentheses and periods');get_ipython().run_line_magic('pinfo', 'periods')
Ans: 
    The \. \( and \) escape characters in the raw string passed to re.compile() will match actual parenthesis characters.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('7. The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options');get_ipython().run_line_magic('pinfo', 'options')
Ans: 
    If the regex pattern has no groups, a list of strings matched is returned. if the regex pattern has groups,
    a list of tuple of strings is returned


# In[ ]:





# In[ ]:





# In[ ]:


get_ipython().set_next_input('8. In standard expressions, what does the | character mean');get_ipython().run_line_magic('pinfo', 'mean')
Ans: 
    In Standard Expressions | means OR operator.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('9. In regular expressions, what does the ? character stand for');get_ipython().run_line_magic('pinfo', 'for')
Ans: 
    
    In regular Expressions, ? characters represents zero or one match of the preceeding group.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('10.In regular expressions, what is the difference between the + and * characters');get_ipython().run_line_magic('pinfo', 'characters')
Ans: 
    In Regular Expressions, * Represents Zero ore more occurances of the preceeding group,
    whereas + represents one or more occurances of the preceeding group.


# In[12]:


import re
match_1 = re.search("Bat(wo)*man","Batman returns")
print(match_1)
match_2 = re.search("Bat(wo)+man","Batman returns")
print(match_2)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('11. What is the difference between {4} and {4,5} in regular expression');get_ipython().run_line_magic('pinfo', 'expression')
Ans:
    {4} means that its preceeding group should repeat 4 times. 
    where as {4,5} means that its preceeding group should repeat mininum 4 times and maximum 5 times inclusively


# In[13]:


import re
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('Ha')
print(mo1.group())
print(mo2)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('12. What do you mean by the \\d, \\w, and \\s shorthand character classes signify in regular expressions');get_ipython().run_line_magic('pinfo', 'expressions')
Ans:
    
\d, \w and \s are special sequences in regular expresssions in python:

\w – Matches a word character equivalent to [a-zA-Z0-9_]
\d – Matches digit character equivalent to [0-9]
\s – Matches whitespace character (space, tab, newline, etc.)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('13. What do means by \\D, \\W, and \\S shorthand character classes signify in regular expressions');get_ipython().run_line_magic('pinfo', 'expressions')
Ans:
    
\D, \W and \S are special sequences in regular expresssions in python:

\W – Matches any non-alphanumeric character equivalent to [^a-zA-Z0-9_]
\D – Matches any non-digit character, this is equivalent to the set class [^0-9]
\S – Matches any non-whitespace character


# In[ ]:





# In[ ]:


get_ipython().set_next_input('14. What is the difference between .*? and .*');get_ipython().run_line_magic('psearch', '*')
Ans: 
    .* is a Greedy mode, which returns the longest string that meets the condition. 
    Whereas .*? is a non greedy mode which returns the shortest string that meets the condition.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('15. What is the syntax for matching both numbers and lowercase letters with a character class');get_ipython().run_line_magic('pinfo', 'class')
Ans: 
    
    The Synatax is Either [a-z0-9] or [0-9a-z]


# In[ ]:





# In[ ]:


get_ipython().set_next_input('16. What is the procedure for making a normal expression in regax case insensitive');get_ipython().run_line_magic('pinfo', 'insensitive')
Ans: 
    
    We can pass re.IGNORECASE as a flag to make a noraml expression case insensitive


# In[ ]:





# In[ ]:


17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?
Ans: 
    
    Dot . character matches everything in input except newline character .. 
    By passing re.DOTALL as a flag to re.compile(), you can make the dot character match all characters, 
    including the newline character.


# In[ ]:





# In[ ]:


get_ipython().set_next_input("18. If numReg = re.compile(r'\\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return");get_ipython().run_line_magic('pinfo', 'return')
Ans: 
    
    The Ouput will be 'X drummers, X pipers, five rings, X hen'


# In[14]:


import re
numReg = re.compile(r'\d+')
numReg.sub('y', '10 dreamers, 1 pipes, five rings, 4 balls')


# In[ ]:





# In[ ]:


get_ipython().set_next_input('19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do');get_ipython().run_line_magic('pinfo', 'do')
Ans:
    re.VERBOSE will allow to add whitespace and comments to string passed to re.compile().


# In[ ]:





# In[ ]:


20.How would you write a regex that match a number with comma for every three digits? It must match the given following:

'42'
'1,234'
'6,368,745'
but not the following:
'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)


# In[15]:


import re
pattern = r'^\d{1,3}(,\d{3})*$'
pagex = re.compile(pattern)
for ele in ['42','1,234', '6,368,745','12,34,567','1234']:
    print('Output:',ele, '->', pagex.search(ele))


# In[ ]:





# In[ ]:


21. How would you write a regex that matches the full name of someone whose last name is Watanabe? 
You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'

but not the following:

'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)

Ans: pattern = r'[A-Z]{1}[a-z]*\sWatanabe'


# In[16]:


import re
pattern = r'[A-Z]{1}[a-z]*\sWatanabe'
namex = re.compile(pattern)
for name in ['Haruto Watanabe','Alice Watanabe','RoboCop Watanabe','haruto Watanabe','Mr. Watanabe','Watanabe','Haruto watanabe']:
    print('Output: ',name,'->',namex.search(name))


# In[ ]:





# In[ ]:


22. How would you write a regex that matches a sentence where the first word is either Alice, Bob,or Carol; 
the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'

but not the following:

'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'

Ans: 
    pattern = r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.'


# In[17]:


import re
pattern = r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.'
casex = re.compile(pattern,re.IGNORECASE)
for ele in ['Alice eats apples.','Bob pets cats.','Carol throws baseballs.','Alice throws Apples.','BOB EATS CATS.','RoboCop eats apples.'
,'ALICE THROWS FOOTBALLS.','Carol eats 7 cats.']:
    print('Output: ',ele,'->',casex.search(ele))


# In[ ]:




