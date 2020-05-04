import copy


class Node:

    def __init__(self, d, parent=None, location=None):
        """

        :param d: dictionary of vertices
        :param parent: parent of this Node
        """

        self.parent = parent

        if self.parent is not None:
            self.d = copy.deepcopy(parent.d)
            self.guard = parent.guard + 1
            self.location = location
        else:
            self.d = d
            self.guard = 0
            self.location = None

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

