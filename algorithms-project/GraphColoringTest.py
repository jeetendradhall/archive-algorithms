import unittest

from GraphColoring import GraphColoring, Color
from GraphTest import GraphTest

class GraphColoringTest(unittest.TestCase):

    #test the graph coloring class
    def test_graph_coloring(self):

        #create a graph using GraphTest
        #this graph corresponds to the "Watering Hole JoJo Princeton University" road intersection
        # described in section 1.1 of Ullman - Data Structures and Algorithms
        graphTest = GraphTest()
        graph = graphTest.create_graph_from_stream()

        #color the graph using GraphColoring
        gc = GraphColoring(graph)
        gc.color_graph()
        gc.print()

if __name__ == '__main__':
    unittest.main()
