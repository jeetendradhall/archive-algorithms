import unittest

from BranchNBoundLCSearch15Puzzle import Node, Move

from BranchNBoundLCSearch import BranchNBoundLCSearch


class BranchNBoundLCSearchTest(unittest.TestCase):
    def test_something(self):
        bnb = BranchNBoundLCSearch(Node ([1, 2, 3, 4, 5, 6, 0, 8, 9, 10, 7, 11, 13, 14, 15, 12]))
        for move, tiles in bnb.search():
            print (Move(move), tiles)

        #create a root
        #puzzle = Node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12], None, Move.right)
        #get children
        #children = puzzle.get_children()
        #get path from root to child, assuming child is the answer
        #print(BranchNBoundLCSearch.get_answer(children[0]))
        #print(BranchNBoundLCSearch.get_answer(children[1]))
        #self.assertEqual(True, False)
        #print(BranchNBoundLCSearch(children[0]).search())
        #print(BranchNBoundLCSearch(children[1]).search())

if __name__ == '__main__':
    unittest.main()
