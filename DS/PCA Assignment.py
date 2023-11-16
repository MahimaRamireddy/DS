#!/usr/bin/env python
# coding: utf-8

# In[9]:


def asciiToNum(string:str)->int:
    ans = 0
    for i in string:
        ans = ans + ord(i)
    return ans

def add100(num:int):
    ans = []
    for i in range(5):
        ans.append(num + i*100)
    return ans

def add50(num:int):
    ans = []
    for i in range(5):
        ans.append(num + i*50)
    return ans

def add1(num:int):
    ans = []
    for i in range(5):
        ans.append(num + i*1)
    return ans

name = asciiToNum("SreeDivya")
rollno = asciiToNum("CS21B1050")
marks = 5
ascii_name = add100(name)
ascii_rollno = add50(rollno)
quizmarks = add1(marks)



# In[10]:


import pandas as pd
df = pd.DataFrame({"ASCII_Name": ascii_name, "ASCII_RollNumber" : ascii_rollno, "Quiz_1_Marks": quizmarks})
df


# In[11]:


normalized_df = (df - df.mean()) / df.std()
normalized_df


# In[12]:


covariance_matrix = normalized_df.cov()
covariance_matrix


# In[14]:


import numpy as np
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
eigenvalues, eigenvectors


# In[15]:


eigenvectors2 = eigenvectors[:,1:]
eigenvectors2


# In[16]:


new_df = np.matmul(normalized_df,eigenvectors2)
new_df


# In[17]:


new_df.rename(columns={"0": "ASCII_RollNumber", "1": "Quiz_1_Marks"})
new_df


# In[ ]:




