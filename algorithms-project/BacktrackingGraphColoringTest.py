import unittest

from BacktrackingGraphColoring import BacktrackingGraphColoring
from Color import Color
from GraphTest import GraphTest


class BacktrackingGraphColoringTest(unittest.TestCase):

    def color_graph(selfself, graph):
        # #iterate graph
        # it = iter (Color.cyan)
        # while True:
        #     #print (v.get_id())
        #     c = next (it)
        #     if c is None:
        #         break
        #     print(c)

        # color the graph using BacktrackingGraphColoring
        gc = BacktrackingGraphColoring(graph)
        gc.mColoring(iter(graph))
        gc.print()

    def test_backtracking_graph_coloring(self):
        # initialize the graph creation class
        graphTest = GraphTest()
        graphTest.setUp()

        # color the planar graph
        graph = graphTest.create_graph_from_stream(graphTest.planar_edge_stream)
        self.color_graph(graph)

        # color the  graph
        #graph = graphTest.create_graph_from_stream(graphTest.princeton_edge_stream, graphTest.princeton_vertex_stream)
        #self.color_graph(graph)

if __name__ == '__main__':
    unittest.main()
