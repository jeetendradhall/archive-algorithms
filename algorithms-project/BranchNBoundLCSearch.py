from heapq import heappush, heappop
from BranchNBoundLCSearch15Puzzle import Node

class BranchNBoundLCSearch:

    def __init__(self, root_node):
        self.heap = []
        self.root_node = root_node
        self.live_nodes = [] #should be a priority queue

    #return a list of 'list of tiles' from root to answer node
    @classmethod
    def get_answer(cls, answer_node):

        #initialize the path with answer_node,
        # append parents,
        # return the reversed list from root to answer node

        # initialize the path with answer_node
        path = []
        path.append((answer_node.parent_move, answer_node.get_tiles()))

        # append parents
        node = answer_node.get_parent()
        while node != None:
            path.append((node.parent_move, node.get_tiles()))
            node = node.get_parent()

        # return the reversed list from root to answer node
        path.reverse()
        return path

    def search(self):
        # e_node is the live node currently being expanded / generated
        # we begin with root node as an e_node
        e_node = self.root_node

        #is e_node an answer node?
        if e_node.is_answer_node():
            return BranchNBoundLCSearch.get_answer(e_node)

        #depth-first (LC) search + bounding function
            #1. introduce cost of Node (bounding function)
            #2. live nodes ordered by cost low to high
            #3. branch-n-bound = LC search + cost

        #add children of e_node to the live_nodes queue

        #loop
        while True:

            #get children of e_node
            children = e_node.get_children()
            for child in children:
                #is child an answer node? if yes, then quit: 'path of root to answer node'
                if child.is_answer_node():
                    return BranchNBoundLCSearch.get_answer(child)
                #add child to the live_nodes queue
                heappush(self.heap, child)

            #are there more live_nodes? if no, then quit: 'no answer node'
            if (len(self.heap) == 0):
                return None

            #get next live_node, now this node is the e_node
            e_node = heappop(self.heap)