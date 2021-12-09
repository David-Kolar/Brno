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

def cut_graph(graph, c1, c2, ax="x"):
    new_graph = deepcopy(graph)
    for node in graph:
        if not(is_it_in_interval(node[ax], c1, c2)):
            pass