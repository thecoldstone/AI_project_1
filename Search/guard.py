def compare_and_delete(l_one, l_two):
    """

    Compare two lists and delete identical elements
    """
    return [x for x in l_one if x not in l_two]

def delete_rectangles(d, l):

    for key in d:

        d[key] = compare_and_delete(d[key], l)

def get_possible_guard(node):

    l_1 = []
    l_2 = []
    l_3 = []

    for i in node.d:
        if len(node.d[i]) is 1:
            l_1.append(i)

        if len(node.d[i]) is 2:
            l_2.append(i)

        if len(node.d[i]) is 3:
            l_3.append(i)

    if len(l_3) is not 0:
        return l_3

    elif len(l_2) is not 0:
        return l_2

    elif len(l_1) is not 0:
        return l_1
    else:
        return []


def get_guard(node):
    """

    Get the first and having the most adjacent rectangles vertex
    We consider only vertices that have at maximum 3 adjacent rectangles
    """

    list_tmp = []
    vertex_tmp = ""

    for i in node.d:

        if len(list_tmp) < len(node.d[i]):
            if len(node.d[i]) <= 3:
                list_tmp = node.d[i]
                vertex_tmp = i

        if len(list_tmp) == 3:
            break

    # Delete all rectangles adjacent to this vertex
    delete_rectangles(node.d, list_tmp)

    return vertex_tmp, list_tmp
