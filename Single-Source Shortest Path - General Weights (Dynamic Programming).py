#!/usr/bin/env python
# coding: utf-8

# In[1]:


#zero based vertices
zero_based_vertices = False


# In[2]:


#Horowitz, Section 5.4 - SSSP-General Weights
#define edges of the graph
edges = {(1,2,6), (1,3,5), (1,4,5), (2,5,-1), (3,2,-2), 
         (3,5,1), (4,3,-2), (4,6,-1), (5,7,3), (6,7,2)}


# In[3]:


#maximum vertex is the max of max_from_v and max_to_v
n_vertices = max (max(edges)[0], max(edges, key = lambda x: x[1])[1])
if zero_based_vertices:
    n_vertices += 1


# In[4]:


#initialize the adjacency matrix
import numpy as np

adj_matrix = np.ones((n_vertices, n_vertices)) * np.inf
np.fill_diagonal (adj_matrix, 0)
#least cost incoming vertex, gets initialized inside bellman_ford ()
P = []


# In[5]:


#fill the matrix with edge weights
for edge in edges:
    if zero_based_vertices:
        adj_matrix [edge[0]][edge[1]] = edge[2]
    else:
        #indices in 'edges' are 1-based, while indices in array are 0-based
        # hence we subtract 1 from edge index
        adj_matrix [edge[0]-1][edge[1]-1] = edge[2]
print (adj_matrix)


# In[6]:


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


# In[9]:


import queue
from IPython.core.debugger import set_trace
def bellman_ford (u):
    #count number of steps
    O_n_steps = 0
    #cost from source vertex
    cost = list(adj_matrix[u])
    #least cost incoming vertex
    path = np.ones ((n_vertices), dtype=int) * u
    #set of all non-source vertices
    S = list(filter(lambda x: x!=u, range(n_vertices)))
    #changing vertices, previous and current iteration
    v_changing_prev = S.copy ()
    v_changing = []

    #iterate for max path length = (n_vertices - 1) times
    for k in range (n_vertices):
        changing = False
        #for each iteration, revise shortest incoming edge
        for j in S:

            #was minimum updated for this vertex?
            min_updated = False
            #iterate over incoming edges
            for i, w in list(filter( lambda u: 
                                 u[0]!=j and u[1]!=np.inf and u[0] in v_changing_prev,
                                 enumerate(adj_matrix[:,j]) )):
                cost_i_to_j = cost[i] + adj_matrix[i][j]
                if cost_i_to_j < cost[j]:
                    print (i,j, cost[j], cost_i_to_j)
                    cost[j] = cost_i_to_j #update cost
                    path[j] = i #update least weigh incoming vertex
                    changing = True #keep iterating k
                    min_updated = True 

                O_n_steps += 1
            #queue of changing cost vertices
            if min_updated:
                v_changing.append(j)
                
        if not changing:
            break
        
        #prepare queues for the next iteration
        print (v_changing)
        v_changing_prev = v_changing.copy()
        v_changing = []

    return cost, path, O_n_steps


# In[10]:


cost, path, O_n_steps = bellman_ford (0)
print(get_path (0, 6, path))
print (O_n_steps)#70->30->14


# In[ ]:




