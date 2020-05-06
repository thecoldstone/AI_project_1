from Search.node import *
from Search.guard import *


class IDS:
    """
        ITERATIVE DEEPENING SEARCH
    """

    def __init__(self, start):
        self.start = start
        self.solution = []

    def dls(self, node, target, limit):

        possible_guard = get_possible_guard(node)
        if node.guard >= target and possible_guard is None:
            self.solution = node.get_path
            return node

        if limit <= 0:
            return None

        for guard in possible_guard:
            child = Node(node.d, node, guard)
            delete_rectangles(child.d, child.d[guard])
            if self.dls(child, target, limit - 1):
                return child

        return None

    def solve(self, target, limit=None):
        """

        :param target: number of guards
        :param limit: level of depth
        :return: the list with guards if solution is found otherwise the empty list
        """

        if limit is None:
            limit = 99999

        for depth in range(0, limit):

            print(depth)
            result = self.dls(Node(self.start), target, depth)

            if result:
                return self.solution

        return None
