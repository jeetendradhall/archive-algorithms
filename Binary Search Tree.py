#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
import math

#a node of the binary search tree
class Node:
    #total number of nodes
    total_nodes = 0
    
    #create a node and initialize it with a value
    def __init__ (self, value):
        self.leftChild = None
        self.rightChild = None
        self.value = value
        
        #keep track of number of nodes
        Node.total_nodes += 1

    #insert a node in the subtree of this node
    def insert (self, value):
        #go left for value lesser (or equal) than current node value
        if value <= self.value:
            #if there is no left child, create one and assign value. the function will then return
            if self.leftChild == None:
                #set_trace ()
                self.leftChild = Node (value)
            #if there is a left child, then recursively call insert on the left subtree
            else:
                self.leftChild.insert (value)
        #else, go right
        else:
            #if there is no right child, create one and assign value. the function will then return
            if self.rightChild == None:
                self.rightChild = Node (value)
            #if there is a right child, then recursively call insert on the right subtree
            else:
                self.rightChild.insert (value)
                
    

    #print the subtree of this node
    def print (self):
        #set_trace ()
        
        #a queue to keep track of the sequence of nodes level-wise
        q = queue.Queue ()
        
        #add this node to the queue
        q.put (self)
        
        #keep fetching nodes from the queue, enqueueing their child nodes
        
        #formatting
        #left padding
        max_levels = math.ceil (math.log (self.total_nodes, 2))
        #level change detection
        node_count = 0
        #level
        level = -1
        
        #get a node from the queue
        node = q.get ()
        while True:
            
            node_count += 1
            exponent_base2 = math.log (node_count, 2)
            #is there a change in level?
            if exponent_base2.is_integer ():
                level += 1
                #padding keeps reducing with increasing level
                padding = (max_levels - level) * 4
                print ("")
                print (" " * padding, end = " ")
                
            #print the node
            value = node.value
            if (value != None):
                print (" " * padding, value, end = " ")
            else:
                print (" " * padding, '$', end = " ")
            
            #enqueue the left child
            if (node.leftChild != None):
                q.put (node.leftChild)
            else:
                #level change detection requires a complete binary tree
                if (level < max_levels - 1):
                    q.put (Node (None))
                
            #enqueue the right child
            if (node.rightChild != None):
                q.put (node.rightChild)
            else:
                #level change detection requires a complete binary tree
                if (level < max_levels - 1):
                    q.put (Node (None))

            #continue processing nodes
            if (q.empty() == False):
                #get a node from the queue
                node = q.get ()
                #print ('GOT ', node.value)
            else:
                #print ('DONE')
                break


# In[ ]:


from IPython.core.debugger import set_trace
root = Node (8)
root.insert (3)
root.insert (10)
root.insert (1)
root.insert (6)
root.insert (4)
root.insert (7)
root.insert (14)
root.insert (13)


# In[ ]:


from IPython.core.debugger import set_trace

root.print()
root.leftChild.print()


# In[ ]:




