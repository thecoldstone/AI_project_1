from Search.node import *
from Search.guard import *


class DFS:

    """
        Depth First Search using queue instead of stack
    """

    def __init__(self, start, nr):
        """

        :param start: dictionary of vertices
        :param nr: number of rectangles
        """
        self.start = start
        self.nr = nr

    def solve(self, target, optimal=False):

        """

        :param target: in our case target equals number_of_guards >= (number_of_rectangles / 3)
        :param optimal: if optimal is True DFS will find the minimum number of guards
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

            current_node = q_open.pop(-1)

            if current_node.guard >= target and current_node.nr == 0:
                return current_node.get_path

            if current_node.location not in q_close:

                q_close.append(current_node.location)

                if optimal is True:
                    possible_guard = get_possible_guard(current_node)
                    possible_guard.reverse()

                    for i in possible_guard:
                        child = Node(current_node.d, current_node, i)
                        delete_rectangles(child.d, child.d[i])
                        child.nr = child.nr - len(current_node.d[i])
                        q_open.append(child)

                else:
                    possible_guard = get_all_guards(current_node)
                    possible_guard.reverse()

                    print(len(possible_guard))

                    for i in possible_guard:
                        child = Node(current_node.d, current_node, i)
                        delete_rectangles(child.d, child.d[i])
                        child.nr = child.nr - len(current_node.d[i])
                        q_open.append(child)

        return []
