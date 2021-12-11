from algoritms import make_graph, dijkstra, bellman_ford, negation_graph, shortest_path
from file import input_file, output, input_with_cordinates
from tree import make_tree
from cordinates import find_min_max_xy, count_distance, x, y
from cut_graph import del_node, cut_graph
from test_data import graph
from random import randint
from numpy import arange

def find_longest(dc):
    max_ = 0
    max_key = None
    for key, val in dc.items():
        if (abs(val) > max_):
            max_ = abs(val)
            max_key = key
    return max_key, max_

def longest_path(center, start):
    node, length = find_longest(make_path(center, start))
    if (length==float("inf")):
        return None
    return start, node, length

def save_longest(start, end, graph):
    graph = negation_graph(graph)
    length, path = shortest_path(graph, start, end)
    length = str(abs(length[end]))
    output(length, path)

def make_path(start, tree):
    dis, pred = dijkstra(tree, start)
    neg_tree = negation_graph(tree)
    dis, pred = dijkstra(neg_tree, start)
    return dis

def random_node(graph):
    nodes = list(graph.keys())
    #n = randint(0, len(nodes) - 1)
    return nodes[0]


def prepare_graph(center):
    graph, n = input_file()
    graph = make_graph(graph, n)
    tree = make_tree(graph, center)
    return graph, tree

old_graph, n, cordinates = input_with_cordinates()
x_dif = 0.008
y_dif = 0.008
s = 0
l = 0
for x_ in arange(x["min"], x["max"], x_dif):
    x_graph = cut_graph(old_graph, cordinates, x_, x_+x_dif)
    for y_ in arange(y["min"], y["max"], y_dif):
        o = 0
        y_graph = cut_graph(x_graph, cordinates, y_, y_ + y_dif, "y")
        if (len(y_graph) > 0):
            graph = make_graph(y_graph)
            tree = make_tree(graph, random_node(graph))
            tree = negation_graph(tree)
            dj, pr = dijkstra(tree, list(tree.keys())[-1])
            o = find_longest(dj)[1]
            l += len(graph)
        s += o
print(l, s)
"""
#rezani na pruhy po ose x, nalezene maximum 580000
dif = 0.034
old_graph, n, cordinates = input_with_cordinates()
s = 0
l = 0
for dif in range(3, 100):
    dif = dif/1000
    s = 0
    for i in arange(y["min"], y["max"], dif):
        graph = cut_graph(old_graph, cordinates, i, i+dif, "y")
        graph = make_graph(graph)
        tree = make_tree(graph, random_node(graph))
        tree = negation_graph(tree)
        dj, pr = dijkstra(tree, list(tree.keys())[-1])
        s += find_longest(dj)[1]
    print(dif, s)
"""
"""
graph, tree = prepare_graph("35000")
tree = negation_graph(tree)
for i in range(0, 60000, 1000):
    path, j = dijkstra(tree, str(i))
    print(find_longest(path))
"""