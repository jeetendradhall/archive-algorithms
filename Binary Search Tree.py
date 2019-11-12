#!/usr/bin/env python
# coding: utf-8

# In[20]:


import queue
import math
from IPython.core.debugger import set_trace

#a node of the binary search tree
class Node:
    #total number of nodes
    total_nodes = 0
    
    #create a node and initialize it with a value
    def __init__ (self, value):
        self.left = None
        self.right = None
        self.value = value
        
        #keep track of number of nodes
        Node.total_nodes += 1

    #insert a node in the subtree of this node
    def insert (self, value):
        #go left for value lesser (or equal) than current node value
        if value <= self.value:
            #if there is no left , create one and assign value. the function will then return
            if self.left == None:
                #set_trace ()
                self.left = Node (value)
            #if there is a left , then recursively call insert on the left subtree
            else:
                self.left.insert (value)
        #else, go right
        else:
            #if there is no right , create one and assign value. the function will then return
            if self.right == None:
                self.right = Node (value)
            #if there is a right , then recursively call insert on the right subtree
            else:
                self.right.insert (value)

    #return the node in this subtree with the given value
    #also return its parent
    def lookup (self, value):
        #print ("In non-recursive lookup")
        #root has no parent
        parent = None
        #start from root (self)
        node = self

        #keep traversing down
        while node != None and node.value != value:
            #make parent point to node
            parent = node
            #move the node to its child
            if value < node.value:
                node = node.left
            else:
                node = node.right

        #in case value was not found, node will be pointing to None (child of leaf node)
        return node, parent
    
    #return the node in this subtree with the given value
    #also return its parent
    #recursive approach
    def lookup (self, value, parent = None, is_left_child = True):
        #print ("In recursive lookup")
        if value == self.value:
            return self, parent, is_left_child
        
        if value < self.value:
            if self.left != None:
                #calling lookup on self.left causes 'self.left and self'
                # to be 'self and parent' respectively in the nested function
                return self.left.lookup (value, self, True)
            else:
                return None, None, True
        else:
            if self.right != None:
                return self.right.lookup (value, self, False)
            else:
                return None, None, True

    #get node with the minimum value in the subtree
    def get_min (self, parent = None):
        #start with the root
        node = self
        #is successor a left child?
        #False, since the function is called on the right child
        is_left_child = False
        
        #traverse down and left
        while node.left != None:
            parent = node
            node = node.left
            #even if we reach here once, we now know that the successor is a left child
            is_left_child = True
            
        return node, parent, is_left_child

    def num_children (self):
        #initialize number of children to 0
        n = 0
        #initialize single child is left flag
        is_single_left_child = False
        
        if self.left != None:
            n += 1
            is_single_left_child = True
            
        if self.right != None:
            n += 1
            #if there is only a right child, we set the left child flag to false
            #if we have both left and right child, we do not use this value in the caller.
            # so, setting the left child flag to false has no impact.
            is_single_left_child = False
            
        return n, is_single_left_child
    
    def delete (self, value):
        #lookup the node to be deleted, we get hold of its parent too
        node, parent, is_left_child = self.lookup (value)
        
        #get number of children
        num_children, is_single_left_child = node.num_children ()
        
        #no children
        if num_children == 0:
            #set the parent's child to None

            #if this is not a root node with no children
            if parent != None:
                #if this node was the left child
                if is_left_child:
                    parent.left = None
                else:
                    parent.right = None

                #delete the node
                del (node)
            #we are deleting the root node
            else:
                #clear the self data.
                #cannot delete self while being inside the instance method
                self.value = None
        
        #one child
        elif num_children == 1:
            
            #get the only child

            #if node had a left child
            if is_single_left_child:
                node_child = node.left
            else:
                node_child = node.right

            #set the only child to be the child of the parent
            
            #if this is not a root node
            if parent != None:

                #set parent's child as the node's child
                
                #if this node was the left child
                if is_left_child:
                    parent.left = node_child
                else:
                    parent.right = node_child
            
                #delete the node
                del (node)
            #we are deleting the root node
            else:
                #copy over the values from the node's child and delete the node's child
                self.left = node_child.left
                self.right = node_child.right
                self.value = node_child.value
                
                del (node_child)
        
        #two children
        else:
            
            #set the parent's child to the successor

            #get successor and its parent
            succ, parent_succ, is_succ_left_child = node.right.get_min (node)

            #set successor as parents child by just copying successors data.
            # because we want the deleted node's children to be accessible.
            # so, we don't actually delete the node,
            # we just replace its value and instead delete the successor.
            node.value = succ.value

            #set successor's parent's child to None
            #if successor was the left child
            if is_succ_left_child:
                parent_succ.left = succ.left
            else:
                parent_succ.right = succ.right

            #delete successor node
            del (succ)
            
    def compare (self, other):
        
        #set_trace()
        #compare the node
        if self.value != other.value:
            return False
        
        same = True
        
        #compare the left child
        if (self.left == None and other.left == None):
            same = True
        elif (self.left != None and other.left != None):
            same = self.left.compare (other.left)
        else:
            same = False
            
        #we proceed to the right side only if left side is same
        if same == True:
            #compare the right child
            if (self.right == None and other.right == None):
                same = True
            elif (self.right != None and other.right != None):
                same = self.right.compare (other.right)
            else:
                same = False
            
        return same

    #print the subtree of this node
    def print (self):
        #set_trace ()
        
        #a queue to keep track of the sequence of nodes level-wise
        q = queue.Queue ()
        
        #add this node to the queue
        q.put (self)
        
        #keep fetching nodes from the queue, enqueueing their  nodes
        
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
                padding = (max_levels - level) * 3
                print ("")
                print (" " * padding, end = " ")
                
            #print the node
            value = node.value
            if (value != None):
                print (" " * padding, value, end = " ")
            else:
                print (" " * padding, '$', end = " ")
            
            #enqueue the left 
            if (node.left != None):
                q.put (node.left)
            else:
                #level change detection requires a complete binary tree
                if (level < max_levels - 1):
                    q.put (Node (None))
                
            #enqueue the right 
            if (node.right != None):
                q.put (node.right)
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


# In[26]:


from IPython.core.debugger import set_trace
root = Node (8)
root.insert (3)
root.insert (10)
#root.insert (1)
root.insert (6)
root.insert (4)
root.insert (7)
root.insert (14)
root.insert (13)
root.print()


# In[27]:


root2 = Node (8)
root2.insert (3)
root2.insert (10)
#root2.insert (1)
root2.insert (6)
root2.insert (4)
root2.insert (7)
root2.insert (14)
root2.insert (13)
root2.print()


# In[ ]:


lookup_value = 4
print('Node ', root.lookup (lookup_value)[0].value)
print('Parent', root.lookup (lookup_value)[1].value)
print('Is left child?', root.lookup (lookup_value)[2])


# In[ ]:


get_min_of_subtree = 8
n, parent_of_subtree, ilc = root.lookup (get_min_of_subtree)
node, parent, is_left_child = root.lookup (get_min_of_subtree)
print('Minimum in subtree of', node.value, 'is', node.get_min(parent_of_subtree)[0].value)
print('Parent of minimum is', node.get_min(parent_of_subtree)[1].value)


# In[ ]:


root.lookup(1)[0].num_children()


# In[ ]:


root.delete (8)
root.print ()


# In[28]:


root.compare(root2)


# In[ ]:




