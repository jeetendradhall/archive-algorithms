#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Horowitz, Section 4.9 - SSSP
#define edges of the graph
edges = {(1,2,50), (1,3,45), (1,4,10), (2,3,10), (2,4,15),
         (3,5,30), (4,1,20), (4,5,15), (5,2,20), (5,3,35), (6,5,3)}


# In[2]:


#maximum vertex is the max of max_from_v and max_to_v
n_vertices = max (max(edges)[0], max(edges, key = lambda x: x[1])[1])


# In[3]:


#initialize the adjacency matrix
import numpy as np

adj_matrix = np.ones((n_vertices, n_vertices)) * np.inf
path_matrix = np.zeros((n_vertices, n_vertices), dtype = int)
np.fill_diagonal (adj_matrix, 0)
print (adj_matrix)
print (path_matrix)


# In[4]:


#fill the matrix with edge weights
for edge in edges:
    #indices in 'edges' are 1-based, while indices in array are 0-based
    # hence we subtract 1 from edge index
    adj_matrix [edge[0]-1][edge[1]-1] = edge[2]
print (adj_matrix)


# In[5]:


#get neighbors of a vertex
#get non-infinity and non-zero edge-weight neighbors
#remove source vertices from neighbors
def get_neighbors (adj_matrix, vertex, source_set):
    #get non-infinity and non-zero edge-weight neighbors
    neighbors = (list(filter(
        #include infinity neighbors
        #lambda x: x[1] != np.inf and x[1] != 0,
        lambda x: x[1] != 0,
        enumerate(adj_matrix[vertex]))))
    #remove source vertices from neighbors
    neighbors = list(filter(lambda x: x[0] not in source_set, neighbors))
    return neighbors


# In[6]:


from IPython.core.debugger import set_trace
#initialize a source set with the 'single source' vertex
source_set = [0]

#while length of source set != number of vertices
while len (source_set) < n_vertices:
    print ('Source Set:', source_set)
    #get all neighbors of vertices in source_set, sorted by weights
    neighbors = []
    for src in source_set:
        neighbors.extend (get_neighbors (adj_matrix, src, source_set))
    print ('Neighbors of Source Set:', neighbors)
    #if no more neighbors of source set, then break from loop
    if neighbors == []:
        break
    #get neighbor with minimum weight,
    # it becomes our candidate neighbor to next include in the source set
    cand_neighbor = min(neighbors, key = lambda x: x[1])
    print ('Candidate Neighbor:', cand_neighbor)
    #get neighbors of candidate source vertex
    neighbors_of_cand = get_neighbors (adj_matrix,
                                            cand_neighbor[0], source_set)
    print ('Neighbors of Candidate:', neighbors_of_cand)
    #update matrix
    for row in source_set:
        #print ('Updating: row', row)
        neighbors = get_neighbors (adj_matrix, row, source_set)
        #print ('Updating: neighbors of row', neighbors)
        #remove candidate neighbor
        if cand_neighbor in neighbors:
            #print ('Updating: Removing candidate neighbor', cand_neighbor)
            neighbors.remove (cand_neighbor)
        #iterate over neighbors
        for neighbor in neighbors:
            #print ('Updating: for neighbor', neighbor)
            col = neighbor [0]
            weight = neighbor [1]
            #if a source set neighbor also a neighbor of candidate
            if col in [i[0] for i in neighbors_of_cand]:
                #print ('Updating: found', col, 'from', row, 'to go via', cand_neighbor[0])
                #if weight from source to neighbor via candidate is
                # less than the present calculated weight
                # from source to neighbor,
                # then update the weight to via candidate weight
                #set_trace ()
                weight_via_candidate = adj_matrix[row][cand_neighbor[0]] + adj_matrix[cand_neighbor[0]][col]
                #print ('Updating: weight', weight, ' .Via weight', weight_via_candidate)
                if weight_via_candidate < weight:
                    print ('Updating: from', row, 'to', col, 'to go via', cand_neighbor[0])
                    print ('UPDATING: weight', weight, ' .Via weight', weight_via_candidate)
                    adj_matrix[row][col] = weight_via_candidate
                    #update the path
                    path_matrix [row][col] = int(cand_neighbor[0])
                    
    #add candidate to the source set
    print ('Add', cand_neighbor[0], 'to Source Set')
    source_set.append (cand_neighbor[0])
    print (adj_matrix)


# In[7]:


def get_path (from_v, to_v):
    #set_trace ()
    path = [from_v, to_v]
    row = from_v
    col = to_v
    print (type(row), type(col))
    while (path_matrix[row][col] != 0):
        path.insert (1, path_matrix[row][col])
        col = path_matrix[row][col]
    return path, adj_matrix [from_v][to_v]


# In[8]:


get_path (0,1)

