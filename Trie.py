#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.debugger import set_trace
from collections import deque


# In[47]:


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
        
    #get child corresponding to a char
    def get_child (self, ch):
        node = None
        #iterate over children and look for a matching char
        for child in self.children:
            if child.char == ch:
                node = child
                break
                
        return node
    
    #form strings from current node to all leaf nodes
    def form_strings_using_children (self):
        #no more string formation at leaf node, form string using self.char
        if len(self.children) == 0:
            return [self.char]
        
        strings = []
        l_substr = []
        
        for child in self.children:
            l_substr.extend(child.form_strings_using_children ())
        
        #print ('substrings ', l_substr, 'for node', self.char)
        for substr in l_substr:
            strings.append (self.char + substr)
        
        return strings
    
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
    
    @staticmethod
    def print ():
        #queue first level siblings
        qu = deque (TrieNode.trie.values())
        #insert marker after siblings
        qu.append (TrieNode('.'))
        while qu:
            item = qu.popleft ()
            print (item.char, end = " ")
            #queue nested level siblings
            qu.extend (item.children)
            #insert marker after siblings
            if item.char != '.':
                qu.append (TrieNode('.'))

    @classmethod
    def find_strings_with_prefix (cls, prefix):
        #prefix is required
        if len(prefix) == 0:
            return None
        
        #strings found with prefix
        strings = []
        #which (char at) index of prefix we are currently looking for
        idx = 0
        
        #traverse down the trie using prefix for navigation

        #get the trie header for the first character
        key = prefix[idx]
        if key in TrieNode.trie.keys ():
            node = TrieNode.trie [key]
        else:
            #we do not have any strings with the given prefix
            return []

        #we now process further starting from the second char in the prefix
        idx += 1

        #traverse down the tree till the prefix is found
        
        #while we are still processing the prefix, and we haven't gone past the leaf
        while idx < len (prefix) and node != None:
            
            #get to the child node based on the char in the prefix
            node = node.get_child (prefix[idx])
            
            #get to the next char in the prefix for the next iteration
            idx += 1
            
        #we should now either be at a node where the prefix ended (valid node)
        #or the prefix was not present (node == None)
        if node == None:
            return []
        
        #get substrings (actually postfix strings)
        l_substr = node.form_strings_using_children ()
        
        #combine prefix with all postfix strings
        for substr in l_substr:
            strings.append (prefix[:-1] + substr)
            
        return strings


# In[48]:


words = {'bear', 'stop', 'buy', 'sell', 'bid', 'stock', 'bell', 'bull'}
TrieNode.create_trie (words)


# In[49]:


print(len(TrieNode.trie['b'].children))#b[u/i/e]
print(TrieNode.trie['b'].children[1].char)#bid
print(TrieNode.trie['b'].children[0].char)
print(len(TrieNode.trie['b'].children[0].children))#bull, buy


# In[50]:


TrieNode.print()


# In[51]:


TrieNode.trie['b'].form_strings_using_children()


# In[63]:


TrieNode.find_strings_with_prefix ('b')

