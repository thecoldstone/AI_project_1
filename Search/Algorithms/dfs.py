from Search.node import *
from Search.guard import *

class DFS:

    def __init__(self, start, number_of_instances):
        self.start = start
        self.nr = number_of_instances

    def solve(self):
        # Lists for open nodes and closed nodes
        q_open = []
        q_close = []

        # Start node
        start_node = Node(self.start)

        # Add the start node
        q_open.append(start_node)
        q_close.append(start_node.guard)

        while len(q_open) > 0:

            current_node = q_open.pop(len(q_open) - 1)

            possible_guard = get_possible_guard(current_node)

            if possible_guard is None and current_node.guard >= (self.nr / 3):
                return current_node.get_path

            for i in possible_guard:

                child = Node(current_node.d, current_node, i)

                delete_rectangles(child.d, child.d[i])

                if child not in q_close:
                    q_open.append(child)
                    q_close.append(child.guard)
