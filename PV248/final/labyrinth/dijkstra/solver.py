def solve(graph, start, end):
    visited, path = calculate_skeleton(graph, start)

    path_to_end = []
    current = end
    while current != start:
        path_to_end = [current] + path_to_end
        try:
            current = path[current]
        except KeyError:
            return 'No solution found'
    return [current] + path_to_end


def calculate_skeleton(graph, start):
    visited = {start: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path
