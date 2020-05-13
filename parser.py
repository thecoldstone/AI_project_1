def parse(file, nr):
    """

    :param file: the current file with that we work
    :param nr: amount of rectangles that we will be analysed
    """

    v_d = {}

    for i in range(1, nr):

        line = file.readline().split()
        i_r, n_v, vertices = int(line[0]), int(line[1]), line[2:]

        # Store as vertex and adjacent rectangles to that vertex
        for i in range(0, len(vertices), 2):

            key = vertices[i] + ',' + vertices[i + 1]

            if key not in v_d.keys():
                v_d[key] = []  # List for insertion number of rectangles
                v_d[key].append(i_r)
            else:
                v_d[key].append(i_r)

    return v_d
