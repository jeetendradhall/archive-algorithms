import unittest

from BranchNBoundLCSearch15Puzzle import Node, Move


class BranchNBoundLCSearch15PuzzleTest(unittest.TestCase):
    def test_something(self):
        #puzzle1 = Node ([1, 2, 3, 4, 5, 6, 0, 8, 9, 10, 7, 11, 13, 14, 15, 12])
        puzzle = Node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12], Move.right)

        print (puzzle.get_children())

if __name__ == '__main__':
    unittest.main()
