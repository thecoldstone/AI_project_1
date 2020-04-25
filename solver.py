from guard_simple import *
from guard_bfs import *


class Solver:

    def __init__(self, start, method):
        self.start = start
        self.method = method

    def solve(self):
        if self.method is None:
            return guard_detect_simple(self.start)

        elif self.method == 1:
            bfs = BFS(self.start)
            return bfs.solve()

        else:
            return None
