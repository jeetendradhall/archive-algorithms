#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Horowitz, Section 5.3 - APSP
#define edges of the graph
edges = {(1,2,4), (1,3,11), (2,1,6), (2,3,2), (3,1,3)}


# In[6]:


#maximum vertex is the max of max_from_v and max_to_v
n_vertices = max (max(edges)[0], max(edges, key = lambda x: x[1])[1])


# In[7]:


#initialize the adjacency matrix
import numpy as np

adj_matrix = np.ones((n_vertices, n_vertices)) * np.inf
np.fill_diagonal (adj_matrix, 0)


# In[8]:


#fill the matrix with edge weights
for edge in edges:
    #indices in 'edges' are 1-based, while indices in array are 0-based
    # hence we subtract 1 from edge index
    adj_matrix [edge[0]-1][edge[1]-1] = edge[2]
print (adj_matrix)


# In[9]:


for k in range (n_vertices):
    for i in range (n_vertices):
        for j in range (n_vertices):
            adj_matrix[i][j] = min (adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])


# In[10]:


print (adj_matrix)


# In[ ]:




