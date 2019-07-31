#colors
import enum

class Color(enum.Enum):
    turquoise = 1
    indigo = 2
    magenta = 3
    cyan = 4
    teal = 5
    azure = 6
    rose = 7
    amber = 8
    vermillon = 9
    plum = 10
    russet = 11
    slate = 12

    def __iter__(self):
        self.idx_current = self.value
        return self

    def __next__(self):
        if (self.idx_current > 4):#depends on the graph. 4 for planar, 5 for princeton
            return None

        self.idx_current = self.idx_current + 1
        return Color (self.idx_current - 1)