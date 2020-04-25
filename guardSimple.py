import sys

def compareAndDelete(list, listTwo):
    return [x for x in list if x not in listTwo]

def deleteVertices(dictOfLists, listOfVertices, guardKey):
    for key in dictOfLists:
        if key == guardKey:
            continue
        dictOfLists[key] = compareAndDelete(dictOfLists[key], listOfVertices)


def getMax(dictOfLists):

    listTmp = []

    for key in dictOfLists:
        if len(listTmp) <= len(dictOfLists[key]):
            # 1. Check if there are vertices with 3 rectangles
            if len(dictOfLists[key]) >= 3:
                return dictOfLists[key], key
            # 2. If not, let's find the maximum length
            listTmp = dictOfLists[key]

    # Returns if there is not list with 3 rectangles
    return listTmp, key


def guard_detect_simple(dictOfLists):

    guardCounter = 0

    # Vertices there can be located guard
    guardRectangles = []

    for key in dictOfLists:
        # DEBUG
        # print(dictOfLists)
        # sys.exit(0)
        if len(dictOfLists[key]) >= 1:
            listOfVertices, key = getMax(dictOfLists)
            # DEBUG
            # print(listOfVertices)
            # sys.exit(0)
            deleteVertices(dictOfLists, listOfVertices, key)
            guardRectangles.append(key)
            dictOfLists[key] = compareAndDelete(dictOfLists[key], dictOfLists[key])
            # DEBUG
            # print(dictOfLists[key])
            # sys.exit(0)
            guardCounter += 1

    print("Probable vertices:", guardRectangles)
    return guardCounter