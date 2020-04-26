from collections import *
from node import *
from guard import *
import copy

class BFS:

    def __init__(self, start):
        self.start = start

    # def copy

    def solve(self):
        # Lists for open nodes and closed nodes
        q_open = []
        q_close = []

        # Start node
        start_node = Node(self.start)

        # Add the start node
        q_open.append(start_node)
        q_close.append(start_node)

        while len(q_open) > 0:

            current_node = (q_open.pop(0))

            possible_guard = get_possible_guard(current_node)

            if possible_guard is None:
                return current_node

            for i in possible_guard:

                new_node = Node(current_node.d, current_node)
                # delete_rectangles(tmp.d, tmp.d[i])

                # child = Node(parent=current_node)
                #
                # if child not in q_close:
                #     q_open.append(start_node)
                #     q_close.append(child)



        # print(queue[0].d)
