class Node:

    def __init__(self, d, parent=None):
        """

        :param d: dictionary of vertices
        :param parent: parent of this Node
        """
        self.d = d
        self.parent = parent
        self.guard = 0

        if self.parent is not None:
            self.guard = parent.guard + 1

    @property
    def get_guard(self):
        return self.guard

    # TODO
    def _copy(self):
        pass

    # @property
    # def solved(self):
    #     return self.nr == 0
