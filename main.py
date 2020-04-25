from parser import *

if __name__ == "__main__":

    # Check stdin
    try:
        SRC_FILE = sys.argv[1]

    except IndexError:
        print("[ERROR]: Not Enough Arguments")
        sys.exit(4)

    # Parse input file
    with open(SRC_FILE, 'r') as file:
        parse(file, 1)
