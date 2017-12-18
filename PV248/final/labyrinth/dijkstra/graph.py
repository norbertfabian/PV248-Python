from collections import defaultdict


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = defaultdict(list)
        self.distances = {}
        if len(edges) == 0:
            raise Exception('Invalid input')

        for edge in edges:
            if edge[0] not in nodes or edge[1] not in nodes:
                raise Exception('Invalid input')

            self.add_edge(edge[0], edge[1], 1)

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
