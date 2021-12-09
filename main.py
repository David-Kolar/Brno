from algoritms import make_graph, dijkstra, bellman_ford, negation_graph, shortest_path
from file import input_file, output, input_with_cordinates
from tree import make_tree
from cordinates import find_min_max_xy, count_distance
from cut_graph import del_node

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

#graph, tree = prepare_graph("2000")
graph = [
    ("0", "1", 2),
    ("1", "2", 5),
    ("2", "3", 4),
    ("2", "0", 11)
]
graph = make_graph(graph, 4)
print(graph)
graph = del_node("0", graph)
print(graph)