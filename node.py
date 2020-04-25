class Node:

    def __init__(self, dict, guard=None, parent=None):
        self.dict = dict
        self.parent = parent

        if(self.parent != None):
            self.guard = parent.guard + 1
        else:
            self.guard = 0
