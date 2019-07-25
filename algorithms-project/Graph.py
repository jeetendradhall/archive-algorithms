#vertex of a graph

class Vertex:
    def __init__ (self, id):
        self.id = id
        self.props = {}
        self.neighbors = {}

    #properties

    def get_key (self):
        return self.id

    def set_property (self, name, value):
        self.props[name] = value

    def get_property (self, name):
        return self.props[name]

    #neighbors

    def add_neighbor (self, id, weight = -1):
        self.neighbors[id] = weight

    def get_weight (self, id):
        return self.neighbors[id]

    def is_neighbor (self, id):
        if id in self.neighbors.keys():
            return True
        return False

    def remove_neighbor (self, id):
        self.neighbors.pop(id)

    def get_neighbors (self):
        return self.neighbors.keys()

#graph
class Graph:
    def __init__(self):
        self.vertices = {}

    #vertices

    def add_vertex (self, id):
        self.vertices[id] = Vertex(id)

    def get_vertex (self, id):
        return self.vertices[id]

    def remove_vertex (self, id):
        self.vertices.pop(id)

    def __contains__ (self, id):
        return id in self.vertices

    #edges

    def add_edge (self, src, dest, weight = -1):
        self.vertices[src].add_neighbor (dest, weight)

    def has_edge (self, src, dest):
        return self.get_vertex(src).is_neighbor(dest)

    #iterate over vertices

    def __iter__ (self):
        return iter(self.vertices.values())

    #print

    def print (self):
        for v in self:
            print ('Vertex', v.get_key(), 'has neighbors ', end = "")
            for n in v.get_neighbors():
                print (n, ' ', end = "")
            print ('')