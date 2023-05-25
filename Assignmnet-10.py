#!/usr/bin/env python
# coding: utf-8

# # Assignment - 10 
# 

# In[ ]:


1. How do you distinguish between shutil.copy() and shutil.copytree()?
Ans:
    shutil.copy() method is used to copy the contents of a file from one file to another file/folder, it primary takes two arguments src,dest, src represents the file to be copied where as destination refers to the file/folder to where the src data should be copied, if dest is a folder name the src with exact name will be copied to the dest folder, if its a file then the contents of src will be copied to dest where dest retains it name.

shutil.copytree() function is used to copy the entire contents of a folder to other folder. it also takes two arguments src & dest, it copies all the content recursively and stores it in dest. the important catch here is dest must not exist prior to this and it will be created during the copy operation. Permissions and times of directories are copied with shutil.copystat() and individual files are copied using shutil.copy2() by default which can be modified using copy_function attribute.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('2. What function is used to rename files');get_ipython().run_line_magic('pinfo', 'files')
Ans:
    os.rename() function is used to rename files or directories using a python program, 
    this function takes two arguments src and dest, src represents the name file/directory which we want to rename,
    whereas dest represents the new name of the file/directory.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('3. What is the difference between the delete functions in the send2trash and shutil modules');get_ipython().run_line_magic('pinfo', 'modules')
Ans:
    send2trash() will delete but after delete file will go to recycle bin
    where as delete() will permanently delete the file.
    


# In[ ]:





# In[ ]:


4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is
get_ipython().set_next_input('equivalent to File objects’ open() method');get_ipython().run_line_magic('pinfo', 'method')
Ans:
    ZipFile Module provides a method called as zipfile.ZipFile() to read and write to zipFiles.
    it takes arugments lile filename and mode etc zipfile.ZipFile('filename', mode = 'r')


# In[ ]:





# In[ ]:


5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf
or .jpg). Copy these files from whatever location they are in to a new folder.
Ans:
    import os,shutil
def changeLocation(folder,filetype,destination):
    for foldername,filenames in os.walk():
        for filename in filenames:
            if fileName.endsWith(filetype):
                shutil.copy(os.path.join(foldername,filename),destination)

