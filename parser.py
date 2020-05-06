import sys
import re

#TODO Parser has drawbacks
def checkInt(file, i):

    try:
        intToCheck = int(file.readline())
        return intToCheck
    except ValueError as e:
        print("[ERROR]: Type Error for iteration", i, e)
        sys.exit(1)

def checkIntByChar(file):

    try:
        intToCheck = file.read(1)

        if intToCheck.isdigit():

            intToCheck += file.read(1)
            # print(intToCheck)

            # return checkIntByChar(file)

        if intToCheck.isspace():
            return checkIntByChar(file)

        if intToCheck == "\n":
            return None

        return int(intToCheck)

    except ValueError:
        print("[ERROR]: Type Error")
        sys.exit(1)


def analyse(file, nr):
    """

    :param file: the current file with that we work
    :param nr: amount of rectangles that we will be analysed
    """

    vertices_dict = {}

    #Main Algorithm
    for i in range(1, nr):

        # 1. Read index of current rectangle
        indexOfRectangle = checkIntByChar(file)
        # 2. Read number of vertices
        numVertices = checkIntByChar(file)

        # 3. Read vertices of current rectangle numVertices times
        for i in range(0, numVertices):

            # Read x and y coordinates
            x_coord = checkIntByChar(file)
            y_coord = checkIntByChar(file)

            if x_coord is not None and y_coord is None:
                print("[ERROR]: Coordinate does not exist")
                sys.exit(2)

            key = ""
            key += "(" + str(x_coord) + "," + str(y_coord) + ")"

            # Insert into the dictionary of lists
            # Where the key is a coordinate of a vertex and list is the all adjacent rectangles
            # TODO Sort after each insertion
            if key not in vertices_dict.keys():
                vertices_dict[key] = []  # List for insertion number of rectangles
                vertices_dict[key].append(indexOfRectangle)
            else:
                vertices_dict[key].append(indexOfRectangle)
                # print(verticesDict[key])

    return vertices_dict


def parse(file, i):
    """
    Read the file line by line to get vertices of each rectangle

    :param file:
    :param i:

    :return:
    """

    # Get number of rectangles
    nr = checkInt(file, i)

    return analyse(file, nr + 1), nr

