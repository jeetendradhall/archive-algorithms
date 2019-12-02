#!/usr/bin/env python
# coding: utf-8

# In[1]:


#zero based vertices
zero_based_vertices = False


# In[2]:


#Horowitz, Section 5.4 - SSSP-General Weights
#define edges of the graph
edges = {(1,2,6), (1,3,5), (1,4,5), (2,5,-1), (3,2,-2), 
         (3,5,1), (4,3,-2), (4,6,-1), (5,7,3), (6,7,3)}


# In[3]:


#maximum vertex is the max of max_from_v and max_to_v
n_vertices = max (max(edges)[0], max(edges, key = lambda x: x[1])[1])
if zero_based_vertices:
    n_vertices += 1


# In[74]:


#initialize the adjacency matrix
import numpy as np

adj_matrix = np.ones((n_vertices, n_vertices)) * np.inf
np.fill_diagonal (adj_matrix, 0)
#least cost incoming vertex, gets initialized inside bellman_ford ()
P = []


# In[75]:


#fill the matrix with edge weights
for edge in edges:
    if zero_based_vertices:
        adj_matrix [edge[0]][edge[1]] = edge[2]
    else:
        #indices in 'edges' are 1-based, while indices in array are 0-based
        # hence we subtract 1 from edge index
        adj_matrix [edge[0]-1][edge[1]-1] = edge[2]
print (adj_matrix)


# In[115]:


def get_path (u, v, P):
    path = [u, v]
    _u = P[v]
    _v = v
    cost = adj_matrix [_u][_v]
    while _u != u:
        path.insert (1, _u)
        _v = _u
        _u = P[_u]
        cost += adj_matrix[_u][_v]
    return path, cost


# In[91]:


def bellman_ford (u):
    #cost from source vertex
    cost = list(adj_matrix[u])
    #least cost incoming vertex
    path = np.ones ((n_vertices), dtype=int) * u
    #set of all non-source vertices
    S = list(filter(lambda x: x!=u, range(n_vertices)))
    #iterate for max path length = (n_vertices - 1) times
    for k in range (n_vertices):
        #for each iteration, revise shortest incoming edge
        for j in S:
            #get shortest weight incoming vertex in column j
            i, w = min(list(filter(lambda u: u[0]!=j and u[1]!=np.inf,
                enumerate(adj_matrix[:,j]) )), key = lambda x: x[1])
            cost_i_to_j = cost[i] + adj_matrix[i][j]
            if cost_i_to_j < cost[j]:
                print (i,j, cost[j], cost_i_to_j)
                cost[j] = cost_i_to_j #update cost
                path[j] = i #update least weigh incoming vertex
    return cost, path


# In[117]:


cost, path = bellman_ford (0)
print(get_path (0, 4, path))
print (cost)

