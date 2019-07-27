import unittest
import Graph

class GraphTest(unittest.TestCase):

    #setup
    def setUp(self):

        # this graph corresponds to the "Watering Hole JoJo Princeton University" road intersection
        # described in section 1.1 of Ullman - Data Structures and Algorithms
        self.princeton_edge_stream = [('AB', 'BC', 1), ('AB', 'BD', 1), ('AB', 'DA', 1), ('AB', 'EA', 1),
                  ('AC', 'BD', 1), ('AC', 'DA', 1), ('AC', 'DB', 1), ('AC', 'EA', 1), ('AC', 'EB', 1),
                  ('AD', 'EA', 1), ('AD', 'EB', 1), ('AD', 'EC', 1),
                  ('BC', 'AB', 1), ('BC', 'DB', 1), ('BC', 'EB', 1),
                  ('BD', 'AB', 1), ('BD', 'AC', 1), ('BD', 'DA', 1), ('BD', 'EB', 1), ('BD', 'EC', 1),
                  ('DA', 'AB', 1), ('DA', 'AC', 1), ('DA', 'BD', 1), ('DA', 'EB', 1), ('DA', 'EC', 1),
                  ('DB', 'AC', 1), ('DB', 'BC', 1), ('DB', 'EC', 1),
                  ('EA', 'AB', 1), ('EA', 'AC', 1), ('EA', 'AD', 1),
                  ('EB', 'AC', 1), ('EB', 'AD', 1), ('EB', 'BC', 1), ('EB', 'BD', 1), ('EB', 'DA', 1),
                  ('EC', 'AD', 1), ('EC', 'BD', 1), ('EC', 'DA', 1), ('EC', 'DB', 1)]
        self.princeton_vertex_stream = ['BA', 'DC', 'ED']

        #this graph corresponds to the planar graph in Fundamentals of Computer Algorithms - Horowitz, Sahni - section 7.4 fig 7.12
        self.planar_edge_stream = [(1,2,1), (1,3,1), (1,4,1), (2,3,1), (2,4,1), (2,5,1), (3,4,1), (4,5,1)]

    #helper functions

    #create a graph using the Vertex class
    def create_graph_using_Vertex(self):
        v1 = Graph.Vertex ('v1')
        v2 = Graph.Vertex ('v2')
        v3 = Graph.Vertex ('v3')
        v4 = Graph.Vertex ('v4')
        v1.add_neighbor('v2')
        v1.add_neighbor('v3')
        v2.add_neighbor('v4')
        v3.add_neighbor('v4')
        v1.set_property('color', 'red')
        v2.set_property('color', 'blue')
        v3.set_property('color', 'blue')
        v4.set_property('color', 'red')

        return v1, v2, v3, v4

    # create graph using the Graph class
    def create_graph_using_Graph(self):
        graph = Graph.Graph()
        graph.add_vertex('v1')
        graph.add_vertex('v2')
        graph.add_vertex('v3')
        graph.add_vertex('v4')
        graph.add_edge('v1', 'v2')
        graph.add_edge('v1', 'v3')
        graph.add_edge('v2', 'v4')
        graph.add_edge('v3', 'v4')

        return graph

    #create graph from stream, using the Graph class
    def create_graph_from_stream(self, edge_stream, vertex_stream = []):
        graph = Graph.Graph()
        for src, dest, weight in edge_stream:
            if src not in graph:
                graph.add_vertex(src)
            if dest not in graph:
                graph.add_vertex(dest)

            graph.add_edge(src, dest, weight)

        for v in vertex_stream:
            if v not in graph:
                graph.add_vertex(v)

        return graph

    # #define a stream, and create graph from stream
    # # this graph corresponds to the "Watering Hole JoJo Princeton University" road intersection
    # # described in section 1.1 of Ullman - Data Structures and Algorithms
    # def create_graph_from_stream(self):
    #     edge_stream = [('AB', 'BC', 1), ('AB', 'BD', 1), ('AB', 'DA', 1), ('AB', 'EA', 1),
    #               ('AC', 'BD', 1), ('AC', 'DA', 1), ('AC', 'DB', 1), ('AC', 'EA', 1), ('AC', 'EB', 1),
    #               ('AD', 'EA', 1), ('AD', 'EB', 1), ('AD', 'EC', 1),
    #               ('BC', 'AB', 1), ('BC', 'DB', 1), ('BC', 'EB', 1),
    #               ('BD', 'AB', 1), ('BD', 'AC', 1), ('BD', 'DA', 1), ('BD', 'EB', 1), ('BD', 'EC', 1),
    #               ('DA', 'AB', 1), ('DA', 'AC', 1), ('DA', 'BD', 1), ('DA', 'EB', 1), ('DA', 'EC', 1),
    #               ('DB', 'AC', 1), ('DB', 'BC', 1), ('DB', 'EC', 1),
    #               ('EA', 'AB', 1), ('EA', 'AC', 1), ('EA', 'AD', 1),
    #               ('EB', 'AC', 1), ('EB', 'AD', 1), ('EB', 'BC', 1), ('EB', 'BD', 1), ('EB', 'DA', 1),
    #               ('EC', 'AD', 1), ('EC', 'BD', 1), ('EC', 'DA', 1), ('EC', 'DB', 1)]
    #     vertex_stream = ['BA', 'DC', 'ED']
    #     return self.create_graph_from_stream_inner(edge_stream, vertex_stream)

    #test the Vertex class
    def test_Vertex(self):
        v1, v2, v3, v4 = self.create_graph_using_Vertex()

        #neighbors
        self.assertEqual(v1.get_neighbors(), {'v3', 'v2'})
        self.assertEqual(v3.get_neighbors(), {'v4'})
        self.assertEqual(len(v4.get_neighbors()), 0)
        self.assertEqual(v3.is_neighbor('v4'), True)

        v3.remove_neighbor('v4')
        self.assertEqual(len(v3.get_neighbors()), 0)

        #properties
        self.assertEqual(v3.get_id(), 'v3')
        self.assertEqual(v4.get_property('color'), 'red')

    # test the Graph and Vertex class
    def test_Graph(self):
        graph = self.create_graph_using_Graph()
        v1 = graph.get_vertex('v1')
        v2 = graph.get_vertex('v2')
        v3 = graph.get_vertex('v3')
        v4 = graph.get_vertex('v4')

        #neighbors
        self.assertEqual(v1.get_neighbors(), {'v3', 'v2'})
        self.assertEqual(v3.get_neighbors(), {'v4', 'v1'})
        #self.assertEqual(len(v4.get_neighbors()), 0)
        self.assertEqual(v4.get_neighbors(), {'v2', 'v3'})
        self.assertEqual(v3.is_neighbor('v4'), True)

        #v3.remove_neighbor('v4')
        self.assertEqual(graph.has_edge('v3', 'v4'), True)
        self.assertEqual(graph.has_edge('v4', 'v3'), True)
        graph.remove_edge('v3', 'v4')
        self.assertEqual(v3.get_neighbors(), {'v1'})
        self.assertEqual(graph.has_edge('v3', 'v4'), False)
        self.assertEqual(graph.has_edge('v4', 'v3'), False)
        self.assertEqual(graph.has_edge('v2', 'v1'), True)
        self.assertEqual(graph.has_edge('v3', 'v1'), True)
        self.assertEqual(graph.has_edge('v2', 'v4'), True)

        #properties
        self.assertEqual(v3.get_id(), 'v3')
        #self.assertEqual(v4.get_property('color'), 'red')

        #print
        print('Inside test_Graph:')
        graph.print()

    #test code to create graph from stream
    def test_graph_creation_from_stream(self):
        #create princeton graph
        graph = self.create_graph_from_stream(self.princeton_edge_stream, self.princeton_vertex_stream)

        #graph = self.create_graph()
        AB = graph.get_vertex('AB')
        BC = graph.get_vertex('BC')
        BD = graph.get_vertex('BD')
        DA = graph.get_vertex('DA')
        EA = graph.get_vertex('EA')
        AC = graph.get_vertex('AC')

        #neighbors
        self.assertEqual(AB.get_neighbors(), {'BC', 'BD', 'DA', 'EA'})
        self.assertEqual(AC.get_neighbors(), {'DB', 'BD', 'DA', 'EA', 'EB'})

        #print
        print('Inside test_graph_creation_from_stream:')
        graph.print()

if __name__ == '__main__':
    unittest.main()
