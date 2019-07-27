#implements the graph coloring algorithm

#colors
import enum

class Color(enum.Enum):
    turquoise = 1
    indigo = 2
    magenta = 3
    cyan = 4
    teal = 5
    azure = 6
    rose = 7
    amber = 8
    vermillon = 9
    plum = 10
    russet = 11
    slate = 12

class GreedyGraphColoring:
    def __init__(self, graph):
        self.graph = graph

    def color_vertex_batch(self, color):
        vertex_batch = []

        #GREEDY - SELECT
        #for an uncolored vertex in graph (get a list of vertices with no color property)
        for v_uncolored in [v for v in self.graph if not v.has_property('color')]:
            #GREEDY - FEASIBLE
            is_neighbor_of_batch_vertex = False
            #check if it is the neighbor of any vertex in batch
            # iterate over vertices in the batch
            for v_batch in vertex_batch:
                #is this uncolored vertex a neighbor of some vertex in batch?
                if v_uncolored.get_id() in v_batch.get_neighbors():
                    #if yes, flag neighbor_found_in_batch, and break the batch vertex loop
                    is_neighbor_of_batch_vertex = True
                    break
            # GREEDY - UNION
            #if not is_neighbor_of_batch_vertex, add the color property to the vertex and add it to the batch
            if (is_neighbor_of_batch_vertex != True):
                #add the color property to the vertex
                v_uncolored.set_property('color', color)
                #add it to the batch
                vertex_batch.append(v_uncolored)

        #return vertex batch, an empty batch implying we have colored all vertices
        return vertex_batch

    #GREEDY APPROACH
    def color_graph(self):

        #iterate over colors (hoping we won't exhaust them
        for c in Color:
            # get vertex batch for this color
            vertex_batch = self.color_vertex_batch(c)
            # if batch is empty, we have finished coloring. break from the loop.
            if not vertex_batch:
                break
            print ('For', c)
            for v in vertex_batch:
                print (v.get_id(), " ", end = "")
            print ("")

    def print(self):
        print ("")
        #iterate over the vertices
        for v in self.graph:
            # print the id, and the color property
            print (v.get_id(), 'has', v.get_property('color'))