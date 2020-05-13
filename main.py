from parser import *
from Search.solver import *
import sys

if __name__ == "__main__":

    try:
        SRC_FILE = sys.argv[1]

    except IndexError:
        print("[ERROR]: Not Enough Arguments")
        sys.exit(1)

    try:
        method = int(sys.argv[2])
    except Exception:
        method = None

    try:
        optimal = sys.argv[3]
        if optimal is 'o':
            optimal = True
    except Exception:
        optimal = False



    # Open file and parse it from input
    with open(SRC_FILE, 'r') as file:

        # Number of iterations
        n_i = int(file.readline().split().pop(0))

        for i in range(0, n_i):

            # Number of rectangles
            n_r = int(file.readline().split().pop(0))

            vertices = parse(file, n_r+1)

            print("###########################")
            print("Iteration:", i+1)
            if method is None:
                print("Simple")
            elif method == 1:
                print("BFS Algorithm")
            elif method == 2:
                if optimal is True:
                    print("Optimized", end=' ')
                print("DFS Algorithm")
            elif method == 3:
                print("Iterative Deepening Search Algorithm")
            elif method == 4:
                print("A* Algorithm")
            elif method == 5:
                print("Branch-and-Bound")
            else:
                print("Method does not exist")
                break

            solution = Solver(vertices)
            solution.solve(n_r, method, optimal)

            print("Probable guards: ", solution.solution)
            print("Number of guards: ", len(solution.solution))

            if i + 1 is n_i:
                break

            decision = input("Do you want to continue: [y/n]")
            if decision is "n":
                    break



