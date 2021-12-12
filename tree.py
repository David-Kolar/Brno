from collections import deque

def append_list_to_deque(ls, source, queue):
    while (ls):
        queue.appendleft((ls.pop(), source))
    return queue

def check_node(node, graph, tree, source):
    node = list(graph[node].keys())
    for key in node:
        if (key != source) and (key in tree):
            return False
    return True

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


def make_tree(graph={}, start=None):
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
