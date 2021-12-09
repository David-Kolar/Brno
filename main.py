from algoritms import make_graph, dijkstra, bellman_ford, negation_graph, shortest_path
from file import input_file, output, input_with_cordinates
from tree import make_tree
from cordinates import find_min_max_xy, count_distance, x, y
from cut_graph import del_node, cut_graph
from test_data import graph

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

def prepare_graph(center):
    graph, n = input_file()
    graph = make_graph(graph, n)
    tree = make_tree(graph, center)
    return graph, tree

"""
old_graph, n, cordinates = input_with_cordinates()
graph = cut_graph(old_graph, cordinates, x["min"], x["min"]+0.005)
graph = make_graph(graph)
print(graph)
print(len(old_graph), len(graph))
"""

"""
graph, tree = prepare_graph("35000")
tree = negation_graph(tree)
for i in range(0, 60000, 1000):
    path, j = dijkstra(tree, str(i))
    print(find_longest(path))
"""