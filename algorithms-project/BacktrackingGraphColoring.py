from Color import Color

class BacktrackingGraphColoring:

    def __init__(self, graph):
        self.graph = graph
        self.it_color = iter(Color.turquoise)

    def mColoring(self, it):
        #print('inside mColoring')
        #get the next vertex
        v = next (it)
        if v is None:
            return

        #assign color to the vertex
        self.nextValue(v)

        #color the remaining vertices ???
        self.mColoring (it)
        #print ('vertex', v.get_id(), 'got color', v.get_property ('color'))

    #given a vertex id, assign it a color distinct from the colors of its adjacent vertices
    def nextValue(self, v):
        #print ('inside nextValue for vertex', v.get_id())

        #proposed color
        color = next(self.it_color)
        if (color is None):
            self.it_color = iter(Color.turquoise)
            color = next(self.it_color)

        #loop until we color this vertex
        while (True):

            #does this vertex have any neighbor with the proposed color?
            b_neighbor_has_this_color = False
            for id_neighbor in v.get_neighbors():
                v_neighbor = self.graph.get_vertex(id_neighbor)
                if v_neighbor.has_property ('color'):
                    if v_neighbor.get_property ('color') == color:
                        b_neighbor_has_this_color = True
                        break

            #if a neighbor found with the proposed color, we try with the next color
            if b_neighbor_has_this_color:
                color = next(self.it_color)
                if (color is None):
                    self.it_color = iter(Color.turquoise)
                    color = next(self.it_color)
            else:
                #go ahead with the proposed color
                v.set_property('color', color)
                break

    def print(self):

        it = iter (self.graph)
        while True:
            v = next(it)
            if (v is None):
                break
            print (v.get_id(), 'HAS', v.get_property('color'))