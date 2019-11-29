#!/usr/bin/env python
# coding: utf-8

# In[123]:


#zero based vertices
zero_based_vertices = False


# In[124]:


#Horowitz, Section 5.3 - APSP
#define edges of the graph
edges = {(1,2,4), (1,3,11), (2,1,6), (2,3,2), (3,1,3)}


# In[125]:


#https://courses.engr.illinois.edu/cs374/sp2017/slides/18-dyn-prog-shortest-paths.pdf
#define edges of the graph
edges = {(0,1,4), (0,2,1), (0,4,100), (1,3,1), (1,4,5), (2,1,2), (2,4,10), (3,4,1)}
zero_based_vertices = True


# In[126]:


#maximum vertex is the max of max_from_v and max_to_v
n_vertices = max (max(edges)[0], max(edges, key = lambda x: x[1])[1])
if zero_based_vertices:
    n_vertices += 1


# In[127]:


#initialize the adjacency matrix
import numpy as np

adj_matrix = np.ones((n_vertices, n_vertices)) * np.inf
np.fill_diagonal (adj_matrix, 0)
path_matrix = np.ones((n_vertices, n_vertices), dtype = int) * (-1) #-1 indicates invalid vertex id


# In[128]:


def get_path (from_v, to_v):
    via_vertex = path_matrix [from_v][to_v]
    if via_vertex == -1:
        return [from_v, to_v]
    else:
        left_subpath = get_path (from_v, via_vertex)
        right_subpath = get_path (via_vertex, to_v)
        path = left_subpath
        path.extend (right_subpath[1:])
        return path


# In[129]:


#fill the matrix with edge weights
for edge in edges:
    if zero_based_vertices:
        adj_matrix [edge[0]][edge[1]] = edge[2]
    else:
        #indices in 'edges' are 1-based, while indices in array are 0-based
        # hence we subtract 1 from edge index
        adj_matrix [edge[0]-1][edge[1]-1] = edge[2]
print (adj_matrix)


# In[130]:


for k in range (n_vertices):
    for i in range (n_vertices):
        for j in range (n_vertices):
            cost = adj_matrix[i][j]
            cost_via_k = adj_matrix[i][k] + adj_matrix[k][j]
            if (cost_via_k < cost):
                adj_matrix[i][j] = cost_via_k
                path_matrix [i][j] = k
                #print (i, j, k)
                #print (adj_matrix)


# In[136]:


print (path_matrix)
get_path(0,4)


# In[ ]:




