from parser import *

if __name__ == "__main__":

    # Check stdin
    try:
        SRC_FILE = sys.argv[1]

    except IndexError:
        print("[ERROR]: Not Enough Arguments")
        sys.exit(1)

    # Open file and parse it from input
    with open(SRC_FILE, 'r') as file:
        # Here you can choose the search method
        parse(file)

