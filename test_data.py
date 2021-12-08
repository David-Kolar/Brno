from re import sub


def print_path_length(graph, data):
    length = 0
    last = data[0]
    for node in data:
        length += graph[last][node]
        last = node
    return length


def get_path_data():
    data = []
    first = True
    with open("output.txt") as file:
        for line in file:
            if not (first):
                data.append(sub('[^A-Za-z0-9]+', "", line))
            else:
                first = False
    return data
