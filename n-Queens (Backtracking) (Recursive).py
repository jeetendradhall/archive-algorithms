#!/usr/bin/env python
# coding: utf-8

# In[1]:


S_i = {1,2,3,4,5,6,7,8}
l_solution_vector = []


# In[2]:


def get_set_of_next_component_of_solution_vector (path_in_solution_space):
    return [i for i in S_i if i not in path_in_solution_space]

def validate_implicit_constraints_4_queens (path_in_solution_space, component):
    #we are at root, all columns (components) are valid
    if path_in_solution_space == []:
        return True

    #if the column (component) is to the left or right of the last column
    # in the path_in_solution_space, then the queen in this column (component)
    # will be on the diagonal of the queen in the row above (in column last_component_of_solution_space).
    #constraint violated.
    last_component_of_solution_space = path_in_solution_space[len(path_in_solution_space)-1]
    if component == last_component_of_solution_space + 1 or component == last_component_of_solution_space - 1:
        #queen in the 'component' column is on the diagonal of the queen in the row above.
        return False
    else:
        return True

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
    if len(path_in_solution_space) == len(S_i):
        #store it in the solution set
        l_solution_vector.append (path_in_solution_space)
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


# In[3]:


def validate_implicit_constraints (path_in_solution_space, component):
    #for every component in the path in reverse order
    # if the component (column) in the path is 
    # +/- (component_index+1) places left/right of the candidate component
    reverse_path = reversed (path_in_solution_space)
    for i in enumerate (reverse_path):
        if i[1] == component + (i[0]+1) or i[1] == component - (i[0]+1):
            return False
    return True


# In[4]:


bounding_function ([])
print (len(l_solution_vector))
print (l_solution_vector)
#[[2, 4, 1, 3], [3, 1, 4, 2]]


# In[ ]:




