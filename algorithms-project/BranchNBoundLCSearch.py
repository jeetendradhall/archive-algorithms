class BranchNBoundLCSearch:

    def __init__(self):
        self.live_nodes = [] #should be a priority queue

    def search(self, root_node):
        # e_node is the live node currently being expanded / generated
        # we begin with root node as an e_node
        e_node = root_node

        #is e_node an answer node?

        #depth-first (LC) search + bounding function
            #1. introduce cost of Node (bounding function)
            #2. live nodes ordered by cost low to high
            #3. branch-n-bound = LC search + cost

        #add children of e_node to the live_nodes queue

        #loop

            #get children of e_node
                #is child an answer node? if yes, then quit: 'path of root to answer node'
                #add child to the live_nodes queue

            #are there more live_nodes? if no, then quit: 'no answer node'
            #get next live_node, now this node is the e_node

