#!/usr/bin/env python
# coding: utf-8

# In[1]:


W_i = [11,13,24,7]
m = 31
S_i = [0,1,2,3]
l_solution_vector = []


# In[11]:


#next X_i should be one not among path_in_solution_space
# and higher than the last X_i in path_in_solution_space.
# this is because of the implicit constraints
# 1. X_i not_= X_j for i not_= j
# 2. X_i < X_i+1
def get_set_of_next_component_of_solution_vector (path_in_solution_space):
    #if path_in_solution_space is at root, return S_i
    # since all indices are its children
    if path_in_solution_space == []:
        return S_i
    
    last_component_of_solution_space =     path_in_solution_space [len(path_in_solution_space)-1]
    return [i for i in S_i if i not in             path_in_solution_space and             i > last_component_of_solution_space]


# In[12]:


get_set_of_next_component_of_solution_vector ([2])


# In[13]:


# implicit constraints
# 1. X_i not_= X_j for i not_= j
# 2. X_i < X_i+1
# 3. SIGMA(W_i[X_i]) == m
# (we check for <=m so that we keep collecting components till m is reached/surpassed)
# (we check for ==m in is_answer_state ())
# 1 and 2 are validated in get_set_of_next_component_of_solution_vector()
# 3 is validated here
def validate_implicit_constraints (path_in_solution_space, component):
    #get W_i nmbers corresponding to path indices
    path_W_i = [x[1] for x in enumerate (W_i)                 if x[0] in path_in_solution_space]
    #get W_i number corresponding to component
    component_W_i = W_i [component]
    #SIGMA(W_i[X_i]) <= m
    # (we check for <=m so that we keep collecting components till m is reached/surpassed)
    if sum (path_W_i + [component_W_i]) <= m:
        return True
    else:
        return False


# In[14]:


validate_implicit_constraints ([0,1], 3)


# In[19]:


def is_answer_state (path_in_solution_space):
    #get W_i nmbers corresponding to path indices
    path_W_i = [x[1] for x in enumerate (W_i)                 if x[0] in path_in_solution_space]
    #SIGMA(W_i[X_i]) = m
    if sum (path_W_i) == m:
        return True
    else:
        return False


# In[20]:


#depth-first traversal
#if answer state is reached, store it in the solution set
#get a set of next component of the solution vector
# for each component, see if the partial solution vector
# created by including this component violates the implicit constraints.
# backtrack (check next component in the set, or return if all components are checked)
# if partial solution violates the implicit constraints.
# otherwise add component to the partial solution vector and traverse deeper.
def bounding_function (path_in_solution_space):
    #if answer state is reached
    if is_answer_state (path_in_solution_space):
        #get W_i nmbers corresponding to path indices
        path_W_i = [x[1] for x in enumerate (W_i)                 if x[0] in path_in_solution_space]
        #store it in the solution set
        l_solution_vector.append (path_W_i)
        return
    
    #get a set of next component of the solution vector
    components = get_set_of_next_component_of_solution_vector (path_in_solution_space)
    # for each component, see if the partial solution vector
    # created by including this component violates the implicit constraints.
    for component in components:
        # otherwise add component to the partial solution vector and traverse deeper.
        if validate_implicit_constraints (path_in_solution_space, component):
            bounding_function (path_in_solution_space + [component])
        # backtrack (check next component in the set, or return if all components are checked)
        # if partial solution violates the implicit constraints.
        else:
            #do nothing
            continue


# In[21]:


bounding_function([])


# In[22]:


l_solution_vector


# In[ ]:




