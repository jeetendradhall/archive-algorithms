import enum

class Move(enum.Enum):
    none = 0 #when the tiles are initialized, there is no parent.
             # we are at the root of the state space tree
    up = 1
    right = 2
    down = 3
    left = 4

#a tile with value '0' indicates a space tile
class Node:
    def __init__(self, tiles, parent = None, parent_move = Move.none):
        self.parent = parent
        self.parent_move = parent_move
        self.tiles = tiles
        self.calculate_cost()

    def get_children(self):
        #1 prepare a list of actions to begin with
        actions = [e.value for e in Move]
        actions.remove(Move.none.value)

        #2 remove invalid actions

        #2.1 remove compliment of parent move to avoid recursion
        if self.parent_move == Move.up:
            actions.remove(Move.down.value)
        elif self.parent_move == Move.right:
            actions.remove(Move.left.value)
        elif self.parent_move == Move.down:
            actions.remove(Move.up.value)
        # elif so that we do not remove an action for the root node when parent_action is Move.none
        elif self.parent_move == Move.left:
            actions.remove(Move.right.value)

        #2.2 remove invalid actions due to space at boundary

        #get index of 0 (space tile)
        idx_space = self.tiles.index(0)

        #no elif because 1 or even 2 conditions (when space at one of the 4 corners)
        # can be satisfied
        #if index+1 mod 4 == 0, space is in right-most column, remove Move.right
        if (idx_space + 1) % 4 == 0:
            actions.remove(Move.right.value)
        #if index mod 4 == 0, space is in left-most column, remove Move.left
        if idx_space % 4 == 0:
            actions.remove(Move.left.value)
        #if index < 4, space is in top row, remove Move.top
        if idx_space < 4:
            actions.remove(Move.top.value)
        #if index > 11, space is in bottom row, remove Move.bottom
        if idx_space > 11:
            actions.remove(Move.bottom.value)

        #3 generate child nodes for valid actions

        #each child is a list of tiles
        children = [] #list of Node's
        #for each action, create a child tile position list
        for action in actions:
            #child of this node will make a move starting from the tile positioning of this node
            tiles = self.tiles.copy()

            #make a move for this action and create a child tile position list
            if action == Move.up.value:
                tiles = Node.swap(tiles, idx_space, idx_space - 4)
            elif action == Move.right.value:
                tiles = Node.swap(tiles, idx_space, idx_space + 1)
            elif action == Move.down.value:
                tiles = Node.swap(tiles, idx_space, idx_space + 4)
            elif action == Move.left.value:
                tiles = Node.swap(tiles, idx_space, idx_space - 1)

            #add child tile position list to the list of children
            children.append(Node(tiles, self, action))

        return children

    #is the puzzle solved?
    def is_answer_node(self):
        #if space is not at end, not solved.
        if self.tiles.index(0) != 15:
            return False

        #if tiles are not sorted 1..15, not solved.
        tiles_sorted = self.tiles[:15].copy()
        tiles_sorted.sort()
        if (tiles_sorted != self.tiles[:15]):
            return False

        #tiles are sorted, with a trailing space. solved!
        return True

    #get length of path from root to this node
    def get_path_length(self):
        len = 0
        node = self
        while node.parent != None:
            len = len + 1
            node = node.parent
        return len

    #calculate cost of this node
    #cost = length of path from root + number of tiles not in their position
    def calculate_cost(self):
        cost = self.get_path_length()
        for pos in range(15):
            #if tile number not equal to (zero based) tile position
            #if tile is not at its correct position
            if self.tiles[pos] != pos+1:
                cost += 1

        if self.tiles[15] != 0:
            cost += 1

        self.cost = cost

    #get cost of this node
    def get_cost(self):
        return self.cost

    #'less than' method for priority queue
    def __lt__(self, other):
        #compare cost of self with other
        if self.cost < other.get_cost():
            return True
        return False

    #class method
    #implementing a move
    #swap the space tile with a numeric tile
    @classmethod
    def swap(cls, tiles, idx_space, idx_numeric):
        temp = tiles[idx_space]
        tiles[idx_space] = tiles[idx_numeric]
        tiles[idx_numeric] = temp
        return tiles