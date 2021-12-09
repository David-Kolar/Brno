from cordinates import is_it_in_interval
from copy import deepcopy

def del_node(name, graph):
    new = deepcopy(graph)
    for key in graph.keys():
        if (key == name):
            del new[key]
        elif (name in graph[key]):
            del new[key][name]
    return new

def cut_graph(graph, cordinates, c1, c2, ax="x"):
    new = deepcopy(graph)
    for key, node in graph.items():
        print(key)
        if not(is_it_in_interval(cordinates[key][ax], c1, c2)):
            new = del_node(key, new)
    return node

def cut_graph(graph, cordinates, c1, c2, ax="x"):
    new = []
    for path in graph:
        if (all((is_it_in_interval(cordinates[path[0]][ax], c1, c2), is_it_in_interval(cordinates[path[1]][ax], c1, c2)))):
            new.append(path)
    return new
