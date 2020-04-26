from simple import *
from bfs import *


class Solver:

    def __init__(self, start, method, num_of_rectangles):
        self.start = start
        self.method = method
        self.nr = num_of_rectangles

    def solve(self):
        if self.method is None:
            return guard_detect_simple(self.start)

        elif self.method == 1:
            bfs = BFS(self.start)
            return bfs.solve()

        else:
            return None
