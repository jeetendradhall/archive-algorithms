#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np


# In[63]:


X = "AGGTAB"
Y = "GXTXAYB"
n_x = len(X)
n_y = len(Y)
lcs_matrix = np.ones ((n_x+1,n_y+1)) * -1


# In[64]:


for i in range (0, n_x+1):
    for j in range (0, n_y+1):
        if i == 0 or j == 0:
            lcs_matrix[i][j] = 0
        elif X[i-1] == Y[j-1]:
            lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
        else:
            max_candidate = max([(0, lcs_matrix[i-1][j]),
                                 (1, lcs_matrix[i][j-1])],
                                key = lambda x: x[1])
            lcs_matrix[i][j] = max_candidate[1]


# In[65]:


lcs_matrix


# In[66]:


i = n_x
j = n_y
lcs = []
#from the end of the strings moving towards the beginning
while (i > 0 and j > 0):
    #if chars in X and Y are same
    if X[i-1] == Y[j-1]:
        lcs.insert (0, X[i-1])
        #the X and Y chars match, add char to substring, go the X_truncated and Y_truncated route
        i -= 1
        j -= 1
    #if Y_truncated has longer subsequence than X_truncated, go the Y_truncated route
    elif lcs_matrix[i][j-1] > lcs_matrix[i-1][j]:
        j -= 1
    #if Y_truncated has shorter subsequence than X_truncated, go the X_truncated route
    else:
        i -= 1


# In[67]:


lcs

