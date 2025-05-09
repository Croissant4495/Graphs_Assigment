# # from Graphs import *

# def get_MST_prims(graph, start_vertex):
#     MST_edges = []
#     visited = set()
#     all_vertices = graph.get_vertices()

#     visited.add(start_vertex)

#     while visited != all_vertices:
#         min_weight = float('inf')
#         min_edge = None

#         for vertex in visited:
#             edges = graph.get_edges(vertex)

#             for (vertex2, weight) in edges:

#                 if vertex2 not in visited and weight < min_weight:
#                     min_edge = (vertex, vertex2, weight)
#                     min_weight = weight

#         if min_edge is None:
#             break  # Graph is disconnected

#         MST_edges.append(min_edge)
#         visited.add(min_edge[1])

#     return MST_edges

# g = Graph()
# g.add_edge('a', 'b', 4)
# g.add_edge('b', 'c', 8)
# g.add_edge('c', 'd', 7)
# g.add_edge('d', 'e', 9)
# g.add_edge('a', 'h', 8)
# g.add_edge('b', 'h', 11)
# g.add_edge('c', 'i', 2)
# g.add_edge('c', 'f', 4)
# g.add_edge('d', 'f', 14)
# g.add_edge('e', 'f', 10)
# g.add_edge('h', 'i', 7)
# g.add_edge('i', 'g', 6)
# g.add_edge('f', 'g', 2)
# g.add_edge('h', 'g', 1)


# print(get_MST_prims(g, 'a'))
# # Correct output: [('A', 'B', 2), ('B', 'C', 1)]