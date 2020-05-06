from Search.node import *
from Search.guard import *


class AStar:

    def __init__(self, start, nr):
        self.start = start
        self.nr = nr

    def solve(self):
        # Lists for open nodes and closed nodes
        q_open = []
        q_close = []

        # Start node
        start_node = Node(self.start)

        # Add the start node
        q_open.append(start_node)
        q_close.append(start_node.guard)

        return []
