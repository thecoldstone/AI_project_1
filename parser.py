from solver import *

#TODO Parser has drawbacks
def checkInt(file, i):

    try:
        intToCheck = int(file.readline())
        return intToCheck
    except ValueError:
        print("[ERROR]: Type Error for iteration", i)
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

def analyseInstances(file, instances):
    """

    :param file: the current file with that we work
    :param instances: amount of rectangles that we will analyse
    """

    # TODO MAIN ALGORITHM
    # HASH_TABLE is used for quick access to the coordinates
    # There is a need to implement another abstract data structure
    # to solve this problem. That data structure will help us to define
    # where we have to put the "GUARD" and how many guards will be used overally

    # Probably: Queue with possibility to enqueue and dequeue (?)
    # Cause we need to update every time that data structure with reading a new line from the text file

    verticesDict = {}

    #Main Algorithm
    for i in range(1, instances):

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
            if key not in verticesDict.keys():
                verticesDict[key] = []  # List for insertion number of rectangles
                verticesDict[key].append(indexOfRectangle)
            else:
                verticesDict[key].append(indexOfRectangle)
                # print(verticesDict[key])

    return verticesDict
    # 4. Find guards
    # numOfGuard = guardDetect(verticesDict)
    # print(numOfGuard)

    # print(verticesDict)

    # if numOfGuard % 3 == 0:
    #     print("The number of guard is: ", numOfGuard)
    #     return numOfGuard
    # else:
    #     print("[WRONG]: The rule [ %i / 3 ] == 0 is not obeyed!", numOfGuard)
    #     return numOfGuard


def parse(file, search_method=None):
    """Read the file line by line to get vertices of each rectangle"""
    """First line: The number of instances
       Second...Number of instances: The vertices of each rectangle"""

    #Read number of repetition of a program
    numIterations = checkInt(file, None)

    # Read all lines numIterations times
    for i in range(0, numIterations):

        #Get vertices
        numInstances = checkInt(file, i)
        verticesDict = analyseInstances(file, numInstances + 1)

        # print(verticesDict)
        #Find solution
        solve = Solver(verticesDict, search_method, numInstances + 1)
        solve.solve()

        if(i + 1 == numIterations):
            break

        if(i < numIterations):
            decision = input("Do you want to continue: [y/n]")
            if decision is "n":
                break
