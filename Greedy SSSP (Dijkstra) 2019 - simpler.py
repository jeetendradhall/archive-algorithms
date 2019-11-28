#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Horowitz, Section 4.9 - SSSP
#define edges of the graph
edges = {(1,2,50), (1,3,45), (1,4,10), (2,3,10), (2,4,15),
         (3,5,30), (4,1,20), (4,5,15), (5,2,20), (5,3,35), (6,5,3)}


# In[17]:


#Ullman, Section 6.3 - SSSP
#define edges of the graph
edges = {(1,2,10), (1,4,30), (1,5,100), (2,3,50), (3,5,10), (4,3,20), (4,5,60)}


# In[18]:


#maximum vertex is the max of max_from_v and max_to_v
n_vertices = max (max(edges)[0], max(edges, key = lambda x: x[1])[1])


# In[19]:


def get_path (to_v):
    path = [0, to_v]
    col = to_v
    while (P[col] != 0):
        path.insert (1, P[col])
        col = P[col]
    return path, adj_matrix [0][to_v]


# In[20]:


#initialize the adjacency matrix
import numpy as np

adj_matrix = np.ones((n_vertices, n_vertices)) * np.inf
np.fill_diagonal (adj_matrix, 0)


# In[21]:


#fill the matrix with edge weights
for edge in edges:
    #indices in 'edges' are 1-based, while indices in array are 0-based
    # hence we subtract 1 from edge index
    adj_matrix [edge[0]-1][edge[1]-1] = edge[2]
print (adj_matrix)


# In[22]:


from IPython.core.debugger import set_trace
S = {0} #set of vertices whose shortest distance is known
D = adj_matrix[0,:] #array of length of shortest special path from source to other vertices
P = np.zeros ((n_vertices), dtype=int)
print ('Distance from source before Dijkstra', D)
#iterate and add a vertex to S in each iteration
for i in range (1, n_vertices):
    #get V-S
    l_vMs = list(filter(lambda x: x[0] not in S, enumerate (D)))
    #get the minimum of V-S
    candidate = min((l_vMs), key = lambda x: x[1])[0]
    #add candidate to S
    S.add (candidate)
    #get V-S after adding candidate
    l_vMs = list(filter(lambda x: x[0] not in S, enumerate (D)))
    #iterate V-S and update their path length if going via candidate is shorter
    for id, weight in l_vMs:
        #calculate cost via candidate
        cost_via_candidate = adj_matrix[0][candidate] + adj_matrix[candidate][id]
        #update distance from source if going via candidate is shorter
        if (cost_via_candidate < D[id]):
            D[id] = cost_via_candidate
            P[id] = int(candidate) #update path

print ('Distance from after before Dijkstra', D)
print (P)


# In[23]:


for i in range (1, n_vertices):
    path, distance = get_path (i)
    print ('Path to', i, 'is', path, ' and is', distance, ' long.')


# In[ ]:




