#!/usr/bin/env python
# coding: utf-8

# # Multistage Graphs

# In[ ]:


import sys


# In[9]:


class Node:
    def __init__ (self, id):
        self.id = id
        self.edges = []
        self.cost = -1 #minimum cost
        self.cost_node_id = -1 #node selected in V_i+1 for minimum cost
    def add_edge (self, id, weight):
        self.edges.append ((id, weight))
    def print (self):
        print ('Node', self.id)
        print ('Edges:')
        for i in self.edges:
            print ('id', i[0], 'weight', i[1], ';', end = '')
        print ('')


# In[10]:


n = Node (1)
n.add_edge (2, 9)
n.add_edge (3, 7)


# In[11]:


n.print ()


# In[22]:


#edge is (from_vertex, to_vertex, weight)
edges = {(1,2,9), (1,3,7), (1,4,3), (1,5,2), (2,6,4),
         (2,7,2), (2,8,1), (3,6,2), (3,7,7), (4,8,11), 
         (5,7,11), (5,8,8), (6,9,6), (6,10,5), (7,9,4), 
         (7,10,3), (8,10,5), (8,11,6), (9,12,4), (10,12,2), (11,12,5), (12,-1,-1)}


# In[23]:


graph = {}
for edge in edges:
    from_vertex = edge[0]
    to_vertex = edge[1]
    weight = edge[2]
    #if from_vertex is already in the graph
    if from_vertex in graph.keys ():
        #append edge to the edge-list of the vertex
        graph[from_vertex].add_edge (to_vertex, weight)
    else:
        #create a node for from_vertex
        node = Node (from_vertex)
        #append edge to the edge-list of the vertex
        node.add_edge (to_vertex, weight)
        #add from_vertex to the graph
        graph[from_vertex] = node


# In[37]:


#we start with target and calculate towards source
#reverse sort the edges of nodes
for node in graph.values ():
    node.edges.sort (reverse = True)


# In[38]:


for node in graph.values ():
    node.print ()


# In[48]:


#set the cost of the target vertex to 0
target_node = max(graph.keys())
graph[target_node].cost = 0
#reverse process starting from target - 1 vertex
for i in range (target_node - 1, 0, -1):
    #placeholders for minimum cost node among edge-nodes
    min_cost = sys.maxsize
    min_cost_node_id = -1
    #from the edge list of the node, find the edge with minimum cost
    for edge in graph[i].edges:
        #cost = weight + cost of to_node
        cost = edge[1] + graph[edge[0]].cost
        if cost <= min_cost:
            min_cost = cost
            min_cost_node_id = edge[0]
    #store minimum cost and the corresponding edge-node
    graph[i].cost = min_cost
    graph[i].cost_node_id = min_cost_node_id


# In[50]:


print ('Shortest Path')
node = graph[1]
while node.id != target_node:
    print (node.id)
    node = graph[node.cost_node_id]
print (node.id)

