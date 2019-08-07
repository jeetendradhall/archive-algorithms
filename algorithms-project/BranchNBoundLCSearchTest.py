import unittest

from BranchNBoundLCSearch15Puzzle import Node
from BranchNBoundLCSearch import BranchNBoundLCSearch


class BranchNBoundLCSearchTest(unittest.TestCase):
    def test_something(self):
        bnb = BranchNBoundLCSearch()
        bnb.search(Node ([1, 2, 3, 4, 5, 6, 0, 8, 9, 10, 7, 11, 13, 14, 15, 12]))
        #self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
