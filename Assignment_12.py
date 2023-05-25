#!/usr/bin/env python
# coding: utf-8

# # Assignment_12

# In[ ]:





# In[ ]:


get_ipython().set_next_input('1. In what modes should the PdfFileReader() and PdfFileWriter() File objects will be opened');get_ipython().run_line_magic('pinfo', 'opened')
Ans: 
    For PdfFileReader() file objects should be opened in rb -> read binary mode, 
    Whereas for PdfFileWriter() file objects should be opened in wb -> write binary mode.


# In[ ]:





# In[ ]:


2. From a PdfFileReader object, how do you get a Page object for page 5?
Ans: 
    PdfFileReader class provides a method called getPage(page_no) to get a page object.


# In[ ]:



from PyPDF2 import PdfFileReader
pdf_reader = PdfFileReader(file_path)
for page in pdf_reader.getNumPages():
    pdf_reader.getPage(page)


# In[ ]:


get_ipython().set_next_input('3.What PdfFileReader variable stores the number of pages in the PDF document');get_ipython().run_line_magic('pinfo', 'document')
Ans:
    The total number of pages in the document is stored in the numPages attribute of a PdfFileReader object.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('4.If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it');get_ipython().run_line_magic('pinfo', 'it')
Ans:
    To read an encrypted PDF, call the decrypt() function and pass the password as a string . 
After you call decrypt() with the correct password, you’ll see that calling getPage() no longer causes an error. 
If given the wrong password, the decrypt() function will return 0 and getPage() will continue to fail.
Note that the decrypt() method decrypts only the PdfFileReader object, not the actual PDF file. 
After your program terminates, the file on your hard drive remains encrypted.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('5.What methods do you use to rotate a page');get_ipython().run_line_magic('pinfo', 'page')
Ans:
    We can rotate a page clockwise or counter-clockwise by an angle. 
The PdfFileWriter is used to write the PDF file from the source PDF. 
We are using rotateClockwise(90) method to rotate the page clockwise by 90-degrees.
We are adding the rotated pages to the PdfFileWriter instance.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('6.What is the difference between a Run object and a Paragraph object');get_ipython().run_line_magic('pinfo', 'object')
Ans:
    Each Paragraph object also has a runs attribute that is a list of Run objects. Run objects also have a text attribute, containing just the text in that particular run.


# In[ ]:


get_ipython().set_next_input('7.How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc');get_ipython().run_line_magic('pinfo', 'doc')
Ans:
    docx.Document(docx=None),Return a Document object loaded from docx, where docx can be either a path to a .docx file (a string) or a file-like object. If docx is missing or None, the built-in default document “template” is loaded.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('8.What type of object has bold, underline, italic, strike, and outline variables');get_ipython().run_line_magic('pinfo', 'variables')
Ans:
    A doc File object can have the above specified variables as properties.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('9. What is the difference between False, True, and None for the bold variable');get_ipython().run_line_magic('pinfo', 'variable')
Ans:
    True / False are used where the field takes a boolean value. None is used where the field takes an Optional.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('10.How do you create a Document object for a new Word document');get_ipython().run_line_magic('pinfo', 'document')
Ans : 
    Following step can be used f = open('foobar.docx', 'rb') document = Document(f) f.close()


# In[ ]:





# In[ ]:


get_ipython().set_next_input("11.How do you add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named doc");get_ipython().run_line_magic('pinfo', 'doc')
Ans :
    We can use the following below step : import docx doc = Document('Path of Doc file where Hellow There need to be written') doc.add_heading('Add Heading', 0) doc_para = doc.add_paragraph('Hello There, ')


# In[ ]:





# In[ ]:


get_ipython().set_next_input('12.What integers represent the levels of headings available in Word documents');get_ipython().run_line_magic('pinfo', 'documents')
Ans:
    We can number headings so that top-level headings (Heading 1) are numbered 1, 2, 3, for example, and second-level headings (Heading 2) are numbered 1.1, 1.2, 1.3. Open your document that uses built-in heading styles, and select the first Heading 1. On the Home tab, in the Paragraph group, choose Multilevel List.

