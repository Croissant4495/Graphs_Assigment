from Graphs import *

def get_MST_prims(graph, start_vertex):
    MST_edges = []
    visited = set()
    all_vertices = graph.get_vertices()

    visited.add(start_vertex)

    while visited != all_vertices:
        min_weight = float('inf')
        min_edge = None

        for vertex in visited:
            edges = graph.get_edges(vertex)

            for (vertex2, weight) in edges:

                if vertex2 not in visited and weight < min_weight:
                    min_edge = (vertex, vertex2, weight)
                    min_weight = weight

        if min_edge is None:
            break  # Graph is disconnected

        MST_edges.append(min_edge)
        visited.add(min_edge[1])

    return MST_edges

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge('A', 'B', 2)
g.add_edge('B', 'C', 1)
g.add_edge('A', 'C', 4)

print(get_MST_prims(g, 'A'))
# Correct output: [('A', 'B', 2), ('B', 'C', 1)]