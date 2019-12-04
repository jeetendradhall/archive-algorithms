#!/usr/bin/env python
# coding: utf-8

# In[99]:


import numpy as np


# In[109]:


#Horowitz - 5.6: String Editing
#two strings for which edit sequence is to be deduced 
# to change X to Y using minimum steps
X = "aabab"
Y = "babb"
X = "keysha"
Y = "sheetal"
#length of strings
n_x = len(X)
n_y = len(Y)
#cost matrix, '+1' to accomodate Y insertions ([:,0] first row)
# and deletions ([0:1] first column)
cost = np.zeros ((n_x+1,n_y+1))
cost [:,0] = range(n_x+1) #cost of deleting n chars of X
cost [0,:] = range(n_y+1) #cost of inserting n chars of Y

#track which sub-operation was of minimum cost
#initialize all candidates to -1 (invalid code).
#0,1,2 are valid codes
#0 - delete char of X
#1 - replace char of Y with char of X (min cost will signify
#                                      that chars are the same)
#2 - insert char of Y
min_candidate = np.ones ((n_x+1,n_y+1)) * -1
#first column indicates deletion (code=0) of char of X at index i
min_candidate [1:,0] = np.zeros((n_x))
#first row indicates insertion (code=2) of char of Y at index j
min_candidate [0,1:] = np.ones((n_y)) * 2


# In[110]:


#cost of replacing a char in X with a char in Y
def C (i,j):
    #if chars differ, it is delete+insert = 2 operations
    if X[i-1] != Y[j-1]:
        return 2
    #if chars are same, there are no operations required
    return 0


# In[111]:


#get sequence of edit operations to move from X to Y
def get_sequence ():
    #start at bottom right of the min_candidate matrix
    # and work backwards along the min cost sub-operation path
    i = n_x
    j = n_y
    sequence = []
    while (i>=0 and j>=0):
        #if sub-operation was deletion of char of X at i
        if min_candidate[i][j] == 0:
            sequence.insert(0, 'remove '+ X[i-1]+ ' at '+ str(i))
            i -= 1
        #if sub-operation was replacing of 
        # char of X at i with char of Y at j
        elif min_candidate[i][j] == 1:
            sequence.insert(0, 'skip '+ X[i-1]+ ' at '+ str(i))
            i -= 1
            j -= 1
        #if sub-operation was insertion of char of Y at j
        elif min_candidate[i][j] == 2:
            sequence.insert(0, 'insert '+ Y[j-1]+ ' at '+ str(j))
            j -= 1
        else:
            return sequence
    return sequence


# In[112]:


for i in range (1, n_x+1):
    for j in range (1, n_y+1):
        candidates = [(0, cost[i-1][j]+1),
                      (1, cost[i-1][j-1]+C(i,j)),
                      (2,cost[i][j-1]+1)]
        min_candi_cost = min(candidates, key = lambda x: x[1])
        min_candidate[i][j] = min_candi_cost[0]
        cost[i][j] = min_candi_cost[1]


# In[113]:


get_sequence()


# In[ ]:




