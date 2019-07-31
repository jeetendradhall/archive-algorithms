import unittest

from BacktrackingGraphColoring import BacktrackingGraphColoring
from GraphTest import GraphTest


class BacktrackingGraphColoringTest(unittest.TestCase):

    def test_backtracking_graph_coloring(self):
        #create a graph using GraphTest
        graphTest = GraphTest()
        graphTest.setUp()
        graph = graphTest.create_graph_from_stream(graphTest.planar_edge_stream)

        #iterate graph
        it = iter (graph)
        while True:
            #print (v.get_id())
            v = next (it)
            if v is None:
                break
            print(v.get_id())

        # color the graph using BacktrackingGraphColoring
        gc = BacktrackingGraphColoring(graph)
        gc.mColoring(1)

    # #test the graph coloring class
    # def test_graph_coloring(self):
    #
    #     #create a graph using GraphTest
    #     #this graph corresponds to the "Watering Hole JoJo Princeton University" road intersection
    #     # described in section 1.1 of Ullman - Data Structures and Algorithms
    #     graphTest = GraphTest()
    #     graph = graphTest.create_graph_from_stream()
    #
    #     #color the graph using GraphColoring
    #     gc = GreedyGraphColoring(graph)
    #     gc.color_graph()
    #     gc.print()



if __name__ == '__main__':
    unittest.main()
