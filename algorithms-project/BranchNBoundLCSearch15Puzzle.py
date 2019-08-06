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
    def __init__(self, tiles, parent_move = Move.none):
        self.tiles = tiles
        self.parent_move = parent_move

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

        #generate child nodes for valid actions
        return actions
