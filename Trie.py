#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.core.debugger import set_trace


# In[1]:


class TrieNode:
    
    #trie, class variable
    trie = {}
    
    #initialize with char the node represents.
    #children will be created on string insertion by making nested calls
    def __init__ (self, c):
        self.char = c
        self.children = []
    
    #insert the tail string (2nd char onwards till end)
    #children will be created on string insertion by making nested calls
    def insert (self, word):
        #if no child node to create, then return
        if len(word) == 0:
            return
        
        #create (or use existing) child to continue nested insert on the right path of the trie

        #key to check in list of children if the child already exists
        key = word[0]
        node = None
        for child in self.children:
            if child.char == key:
                node = child
                break;
        
        #if child did not exist already, create one and append to the list of children
        if node == None:
            node = TrieNode (word[0])
            self.children.append (node)

        #continue nested insertion
        node.insert (word[1:])
    
    @classmethod
    def create_trie (cls, words):
        #iterate over words
        for word in words:
            #first char of the word is the key for the trie dictionary
            key = word[0]
            #node is the value for that key
            node = None
            
            #if key already exists, reuse the value
            if key in TrieNode.trie.keys ():
                node = TrieNode.trie [key]
            #else, insert a key, value pair into the trie
            else:
                node = TrieNode (word[0])
                TrieNode.trie [key] = node

            #insert the word in the trie value node
            node.insert (word[1:])


# In[2]:


words = {'bear', 'stop', 'buy', 'sell', 'bid', 'stock', 'bell', 'bull'}
TrieNode.create_trie (words)


# In[6]:


print(len(TrieNode.trie['b'].children))#b[u/i/e]
print(TrieNode.trie['b'].children[1].char)#bid
print(TrieNode.trie['b'].children[0].char)
print(len(TrieNode.trie['b'].children[0].children))#bull, buy


# In[ ]:




