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
graph = make_graph(old_graph)
x_dif = 0.008
y_dif = 0.008
i = 0
j = 0
data = list()
for x_ in arange(x["min"], x["max"], x_dif):
    x_graph = cut_graph(old_graph, cordinates, x_, x_+x_dif)
    data.append(list())
    j = 0
    for y_ in arange(y["min"], y["max"], y_dif):
        y_graph = cut_graph(x_graph, cordinates, y_, y_ + y_dif, "y")
        y_graph = make_graph(y_graph)
        if (len(y_graph) > 0):
            y_graph = make_tree(y_graph, random_node(y_graph))
            pass
        data[i].append(0)
        data[i][j] = y_graph
        j += 1
    i += 1
key_x = 0
key_y = 0
x_velocity = 1
y_velocity = 1
border = len(data) - 1
def next_node(x, y, x_v, y_v, border):
    if (x+x_v > border) or (x+x_v < 0):
        y += y_v
        x_v *= -1
    else:
        x += x_v
    return x, y, x_v, y_v
new_tree = {}
def detect_end(x, y, x_v, y_v, border):
    x, y, x_v, y_v = next_node(x + x_v, y, x_v, y_v, border)
    if (y > len(data[0]) - 1):
        return False
    return True
i = 0
while(detect_end(key_x, key_y, x_velocity, y_velocity, border)):
    done = False
    for key, node in data[key_x][key_y].items():
        if(len(node) < len(graph[key])):
            for key2, val2 in graph[key].items():
                if not(key2 in node):
                    nx, ny, _, __ = next_node(key_x, key_y, x_velocity, y_velocity, border)
                    if (key2 in data[nx][ny]):
                        data[key_x][key_y][key].update({key2: graph[key][key2]})
                        i += 1
                        done = True
                        data[nx][ny][key2].update({key: graph[key][key2]})
    new_tree.update(data[key_x][key_y])
    key_x, key_y, x_velocity, y_velocity = next_node(key_x, key_y, x_velocity, y_velocity, border)
new_tree = negation_graph(new_tree)
dis, pred = dijkstra(new_tree, random_node(new_tree))
print(find_longest(dis))
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