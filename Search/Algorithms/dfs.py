from Search.node import *
from Search.guard import *
from time import *


class DFS:

    def __init__(self, start, nr):
        self.start = start
        self.nr = nr

    def solve(self):
        # Lists for open nodes and closed nodes
        q_open = []
        q_close = []

        # Start node
        start_node = Node(self.start, nr=self.nr)

        # Add the start node
        q_open.append(start_node)
        q_close.append(start_node.guard)

        j = 0

        while len(q_open) > 0:

            current_node = q_open.pop(len(q_open) - 1)

            if current_node.guard >= (self.nr / 3) and current_node.nr == 0:
                return current_node.get_path

            if current_node.location not in q_close:

                q_close.append(current_node.location)
                possible_guard = get_possible_guard(current_node)

                possible_guard.reverse()

                for i in possible_guard:
                    child = Node(current_node.d, current_node, i)
                    delete_rectangles(child.d, child.d[i])
                    child.nr = child.nr - len(current_node.d[i])
                    q_open.append(child)

        return []
