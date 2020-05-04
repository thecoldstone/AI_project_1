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

    # Open file and parse it from input
    with open(SRC_FILE, 'r') as file:

        # Read number of repetition of a program
        numIterations = checkInt(file, None)

        for i in range(0, numIterations):

            vertices, nr = parse(file, i)

            problem = Solver(vertices, nr)
            problem.solve(method)

            if i + 1 == numIterations:
                break

            if i < numIterations:
                decision = input("Do you want to continue: [y/n]")
                if decision is "n":
                    break



