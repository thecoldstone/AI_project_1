from Search.node import *
from Search.guard import *


class BFS:

    """
        Breadth First Search using queue
    """

    def __init__(self, start, nr):

        """

        :param start: dictionary of vertices
        :param nr: number of rectangles
        """
        self.start = start
        self.nr = nr

    def solve(self, target):

        """

        :param target: in our case target equals number_of_guards >= (number_of_rectangles / 3)
        :return: list of possible guards
        """
        # Lists for open nodes and closed nodes
        q_open = []
        # Closed node stores the location of guards
        q_close = []

        # Start node
        start_node = Node(self.start, nr=self.nr)

        # Add the start node
        q_open.append(start_node)

        while len(q_open) > 0:

            current_node = q_open.pop(0)

            q_close.append(current_node.location)
            possible_guard = get_possible_guard(current_node)

            for i in possible_guard:
                child = Node(current_node.d, current_node, i)
                delete_rectangles(child.d, child.d[i])
                child.nr = child.nr - len(current_node.d[i])

                if i not in q_close or q_open:

                    if child.guard >= target and child.nr == 0:
                        return child.get_path

                    q_open.append(child)

        return []
