#!/usr/bin/env python
# coding: utf-8

# In[65]:


import numpy as np


# In[78]:


X = "AGGTABX"
Y = "GXTXAYB"
n_x = len(X)
n_y = len(Y)
lcs_matrix = np.ones ((n_x+1,n_y+1)) * -1
lcs = []


# In[79]:


for i in range (0, n_x+1):
    for j in range (0, n_y+1):
        if i == 0 or j == 0:
            lcs_matrix[i][j] = 0
        elif X[i-1] == Y[j-1]:
            lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
            print (i,j)
            lcs.append (X[i-1])
        else:
            max_candidate = max([(0, lcs_matrix[i-1][j]),
                                 (1, lcs_matrix[i][j-1])],
                                key = lambda x: x[1])
            #if max_candidate[0] == 0:
            #    lcs.append(X[])
            lcs_matrix[i][j] = max_candidate[1]


# In[80]:


lcs_matrix


# In[81]:


lcs


# In[ ]:




