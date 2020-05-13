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


def guard_detect_simple(dictOfLists, nr):

    # Vertices there can be located guard
    guards = []
    rr = nr

    for key in dictOfLists:
        if len(dictOfLists[key]) >= 1:
            listOfVertices, key = getMax(dictOfLists)
            deleteVertices(dictOfLists, listOfVertices, key)
            guards.append(key)
            rr = rr - len(listOfVertices)
            dictOfLists[key] = compareAndDelete(dictOfLists[key], dictOfLists[key])

    if rr != 0 or not len(guards) >= nr / 3:
        print(rr)
        return []

    return guards
