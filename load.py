def load(name="input"):
    with open(name) as file:
        n_crosses = None
        n_streets = None
        graph = []
        for key, line in enumerate(file):
            if (key == 0):
                n_crosses, n_streets = [int(i) for i in line.split()]
            if (key > n_crosses):
                l = line.split()
                l[2] = int(l[2])
                graph.append(l)
        return graph, n_streets
