from Search.node import *
from Search.guard import *


class IDS:
    """
        ITERATIVE DEEPENING SEARCH
    """

    def __init__(self, start, nr):
        self.start = start
        self.solution = []
        self.nr = nr

    def dls(self, node, target, limit):

        if node.guard >= target and node.nr == 0:
            self.solution = node.get_path
            return node

        if limit <= 0:
            return None

        possible_guard = get_possible_guard(node)

        for i in possible_guard:
            child = Node(node.d, node, i)
            delete_rectangles(child.d, child.d[i])
            child.nr = child.nr - len(node.d[i])
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

        # Initial depth equals [R/3] there is R number of rectangles
        for depth in range(int(target), limit):

            result = self.dls(Node(self.start, nr=self.nr), target, depth)

            if result:
                return self.solution

        return []
