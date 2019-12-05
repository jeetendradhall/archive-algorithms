#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


X = "AGGTAB"
Y = "GXTXAYB"
n_x = len(X)
n_y = len(Y)
lcs_matrix = np.zeros ((n_x+1,n_y+1))


# In[5]:


for i in range (n_x, 0, -1):
    for j in range (n_y, 0, -1):
        if X[i-1] == Y[i-1]:
            lcs_matrix[i][j] = 


# In[13]:


def lcs(X, Y, m, n):
    if m == 0 or n == 0: 
        return 0; 
    elif X[m-1] == Y[n-1]: 
        print (m, n, X[m-1], Y[n-1])
        return 1 + lcs(X, Y, m-1, n-1); 
    else: 
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 


# In[14]:


# Driver program to test the above function 
X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X , Y, len(X), len(Y)) )


# In[ ]:




