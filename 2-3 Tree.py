#!/usr/bin/env python
# coding: utf-8

# In[1]:


l = [5, 7, 3, 9, 0, 2]
l


# In[2]:


l.sort()
l


# In[7]:


max(max(2,3), max(4,5))


# In[8]:


sorted([(25,32),(5,7),(63,69),(19,21)])


# In[70]:


sorted([[25,32],[5,7],[63,69],[19,21]])


# In[86]:


a = [[25,32],[5,7],[63,69],[19,21]]
a.sort()


# In[87]:


a


# In[29]:


import array as arr
x = arr.array('i', [12,4,6,8,10])
y = [v/sum(x) for v in x]
y


# In[30]:


sorted(x)


# In[72]:


x[:2]


# In[35]:


z = sorted(x)
type(z)


# In[103]:


class InnerNode:
    def __init__ (self, child1, child2):
        #set up the keys, and children
        #key is the higher key of the child (which we expect it to be at index 1)
        self.keys = [child1.keys[1], child2.keys[1]]
        self.children = [child1, child2]

class LeafParent:
    def __init__ (self, child1, child2):
        #set up the keys, and children
        self.keys = [child1, child2]
        self.children = [child1, child2]
        #keep the keys and children sorted
        self.keys.sort ()
        self.children.sort ()

    #add a child to the list of children already having either 2 or 3 children
    def insert (self, child):
        print ('Begin: Insert child', child, 'into leaf-parent.')
        #add child and keep the children sorted
        self.children.append (child)
        self.children.sort ()
        #add key and keep the keys sorted
        self.keys.append (child)
        self.keys.sort () #we now have an excess key which we should remove

        #if there are 3 children now
        if len (self.children) == 3:
            print (' Add a 3rd child', child, 'to leaf-parent now having leaves', self.children, '.')
            #we now have an excess key which we should remove
            self.keys = self.keys [:-1]
            #there is no split, so return None to retain the same root for the subtree
            print ('End: Insert child', child, 'into leaf-parent.')
            return None
        #we have 4 children, we need to split the node
        else:
            print (' Split leaf-parent with keys', self.keys, 'and children', self.children, '.')
            #create a sibling node and copy over the 3rd and 4th child
            sibling = LeafParent (self.children[2], self.children[3])
            #remove the 3rd and 4th child from this node
            self.keys = self.keys [:2]
            self.children = self.children [:2]
            #create a parent of self and the newly created sibling
            parent = InnerNode (self, sibling)            
            #return the newly created parent
            print ('End: Insert child', child, 'into leaf-parent.')
            return parent


class TwoThreeTree:
    def __init__ (self, value):
        self.root = value

    def insert (self, value):
        #if the tree has just one leaf node (int value) so far
        if isinstance (self.root, int):
            #create a leaf parent and set it as root. its parent is None
            self.root = LeafParent (self.root, value)
        else:
            #call insert on the root node
            #the existing root may have split and formed a parent which it returns
            new_root = self.root.insert (value)
            if new_root != None:
                self.root = new_root


# In[104]:


tree = TwoThreeTree (5)
tree.insert (21)
tree.insert (8)
tree.insert (63)

print (type(tree.root))
print (tree.root.keys)
print (tree.root.children)
print (tree.root.children[0].keys, tree.root.children[1].keys)
print (tree.root.children[0].children, tree.root.children[1].children)


# In[ ]:




