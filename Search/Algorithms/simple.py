def compareAndDelete(list, listTwo):
    return [x for x in list if x not in listTwo]

def deleteVertices(dictOfLists, listOfVertices, guardKey):
    for key in dictOfLists:
        if key == guardKey:
            continue
        dictOfLists[key] = compareAndDelete(dictOfLists[key], listOfVertices)


def getMax(dictOfLists):

    l_tmp = []
    tmp_key = ""

    for key in dictOfLists:
        if len(l_tmp) <= len(dictOfLists[key]):
            l_tmp = dictOfLists[key]
            tmp_key = key
            if len(l_tmp) == 3:
                break

    return l_tmp, tmp_key


def guard_detect_simple(dictOfLists):

    # Vertices there can be located guard
    guardRectangles = []

    for key in dictOfLists:
        if len(dictOfLists[key]) >= 1:
            listOfVertices, key = getMax(dictOfLists)
            deleteVertices(dictOfLists, listOfVertices, key)
            guardRectangles.append(key)
            dictOfLists[key] = compareAndDelete(dictOfLists[key], dictOfLists[key])
    return guardRectangles
