import unittest

from GreedyGraphColoring import GreedyGraphColoring, Color
from GraphTest import GraphTest

class GreedyGraphColoringTest(unittest.TestCase):

    #test the graph coloring class
    def test_greedy_graph_coloring(self):

        #create a graph using GraphTest
        #this graph corresponds to the "Watering Hole JoJo Princeton University" road intersection
        # described in section 1.1 of Ullman - Data Structures and Algorithms
        graphTest = GraphTest()
        graphTest.setUp()
        graph = graphTest.create_graph_from_stream(graphTest.princeton_edge_stream, graphTest.princeton_vertex_stream)

        #color the graph using GreedyGraphColoring
        gc = GreedyGraphColoring(graph)
        gc.color_graph()
        gc.print()

if __name__ == '__main__':
    unittest.main()
