from collections import deque
from algoritms import make_graph, dijkstra, bellman_ford, negation_graph, shortest_path
from load import load

def append_list_to_deque(ls, source, queue):
    while (ls):
        queue.appendleft((ls.pop(), source))
    return queue


def output(longest, path, file="output.txt"):
    with open(file, "w") as file:
        file.write(longest + "\n")
        for line in path:
            file.write(line + "\n")


def check_node(node, graph, tree, source):
    node = list(graph[node].keys())
    for key in node:
        if (key != source) and (key in tree):
            return False
    return True


def find_longest(dc):
    max_ = 0
    max_key = None
    for key, val in dc.items():
        if (abs(val) > max_):
            max_ = abs(val)
            max_key = key
    return max_key, max_,


def check_hash_map(nodes, map):
    new = []
    for node in nodes:
        if not (node in map):
            new.append(node)
    return new


def check_sorted_dict(graph, tree, ls):
    new = []
    for node in ls:
        if (check_node(node, graph, tree)):
            new.append(node)
    return new


def make_tree(graph={}, start="0"):
    first_node = start
    tree = dict()
    queue = deque()
    queue.appendleft((first_node, first_node))
    hash_queue = dict()
    while (queue):
        node, source = queue.pop()
        if (check_node(node, graph, tree, source)):
            try:
                tree[source].update()
            except:
                tree[source] = {}
            tree[source].update({node: graph[node][source]})
            tree[node] = {source: graph[node][source]}
            sorted_dict = {k: v for k, v in sorted(graph[node].items(), key=lambda item: item[1])}
            sorted_dict = list(sorted_dict.keys())
            sorted_dict = check_hash_map(sorted_dict, hash_queue)
            hash_queue[node] = True
            queue = append_list_to_deque(sorted_dict, node, queue)
    return tree

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

graph, n = load()
center = "35000"
graph = make_graph(graph, n)
tree = make_tree(graph, center)
save_longest('1000', '35971', tree)