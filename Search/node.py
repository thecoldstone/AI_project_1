import copy


class Node:

    def __init__(self, d, parent=None, location=None, nr=None):
        """

        :param d: dictionary of vertices
        :param parent: parent of this Node
        :param nr: number of rectangles remained to cover
        """

        self.parent = parent

        if self.parent is not None:
            self.d = copy.deepcopy(parent.d)
            self.guard = parent.guard + 1
            self.location = location
            self.nr = self.parent.nr
            self.f = self.heuristic_one
        else:
            self.d = d
            self.guard = 0
            self.location = None
            self.nr = nr
            self.f = 0

    @property
    def heuristic_one(self):
        return self.nr + self.guard

    # Worse than heuristic_one
    @property
    def heuristic_two(self):
        return round(self.nr / 3) + self.guard

    @property
    def get_guard(self):
        return self.guard

    @property
    def get_dict(self):
        return self.d

    @property
    def get_path(self):
        node, path = self, []
        while node:
            if node.location is not None:
                path.append(node.location)
            node = node.parent

        return path[::-1]

    def __str__(self):
        return str(self.d)

