from Search.Algorithms import simple, bfs, dfs


class Solver:

    def __init__(self, start, num_of_rectangles):
        self.start = start
        self.nr = num_of_rectangles
        self.solution = []

    def solve(self, method=None):

        def solvable(num_guards):
            return num_guards >= self.nr / 3

        if method is None:

            self.solution= simple.guard_detect_simple(self.start)

            if not solvable(len(self.solution)):
                print("Solution is not find")

            print("Simple")
            print("Probable guards: ", self.solution)
            print("Number of guards: ", len(self.solution))

        elif method == 1:

            self.solution = bfs.BFS(self.start, self.nr).solve()

            print("BFS Algorithm")
            print("Probable guards: ", self.solution)
            print("Number of guards: ", len(self.solution))

        elif method == 2:

            self.solution = dfs.DFS(self.start, self.nr).solve()

            print("DFS Algorithm")
            print("Probable guards: ", self.solution)
            print("Number of guards: ", len(self.solution))

        else:
            return None
