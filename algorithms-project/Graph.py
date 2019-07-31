#vertex of a graph

class Vertex:
    def __init__ (self, id):
        self.id = id
        self.props = {}
        self.neighbors = {}

    #properties

    def get_id (self):
        return self.id

    def set_property (self, name, value):
        self.props[name] = value

    def get_property (self, name):
        return self.props[name]

    def has_property (self, name):
        return name in self.props.keys()

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

    def print (self):
        print ('id=', self.id)
        print ('properties: ', end = "")
        for n, v in self.props.items():
            print (n, '=', v, ' ', end = "")
        print("")
        print ('neighbors: ', end = "")
        for n, v in self.neighbors.items():
            print (n, ' ', end = "")
        print ("")

#graph
class Graph:
    def __init__(self, directed = False):
        self.vertices = {}
        self.directed = directed
        self.current_vertex = None

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
        #for undirected graph, add the reverse edge
        if (self.directed == False):
            self.vertices[dest].add_neighbor (src, weight)

    def remove_edge (self, src, dest):
        self.vertices[src].remove_neighbor (dest)
        # for undirected graph, remove the reverse edge
        if (self.directed == False):
            self.vertices[dest].remove_neighbor(src)

    def has_edge (self, src, dest):
        return self.get_vertex(src).is_neighbor(dest)

    #iterate over vertices

    def __iter__ (self):
        # return iter(self.vertices.values())

        self.idx_current_vertex = 0
        return self

    def __next__ (self):
        vertices = self.vertices.values()
        if self.idx_current_vertex >= len (vertices):
            return None

        self.idx_current_vertex = self.idx_current_vertex + 1
        return list (vertices) [self.idx_current_vertex - 1]

    #print

    def print (self):
        # for v in self:
        #     print ('Vertex', v.get_key(), 'has neighbors ', end = "")
        #     for n in v.get_neighbors():
        #         print (n, ' ', end = "")
        #     print ('')
        for v in self.vertices.values():
            v.print()
            if (v.has_property('color')):
                print('print color:', v.get_property('color'))

        for v_colored in [v for v in self.vertices.values() if v.has_property('color')]:
            print (v_colored.get_id())