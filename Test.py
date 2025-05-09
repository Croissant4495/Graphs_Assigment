from Graphs import *

# # Question 1
# print("________Question 1________")
# myG = Graph()
# myG.add_vertex('a')
# myG.add_vertex('v')
# myG.add_vertex('c')
# myG.add_vertex('d')
# myG.add_edge('a', 'v', 10)
# myG.add_edge('c', 'v', 5)
# myG.add_edge('a', 'c', 4)
# myG.add_edge('c', 'd', 4)
# print(myG.graph)    
# myG.delete_edge('c', 'd')
# myG.delete_edge('c', 'd')

# print(myG.has_edge('a', 'v'))
# print(myG.get_edge_weight('a', 'z'))
# print(myG.has_edge('a', 'd'))
# print(myG.has_edge('a', 'z'))
# print(myG.graph)

# Question 2
print("________Question 2________")
g = directed_tree()
# edges = [
#     (0, 4),
#     (0, 3),
#     (0, 2),
#     (1, 2),
#     (1, 5),
#     (1, 6),
#     (2, 4),
#     (4, 7),
#     (5, 7),
#     (6, 7)
# ]

# assignemnt example
edges = [
    (7, 5),
    (7, 6),
    (5, 2),
    (5, 4),
    (6, 4),
    (6, 3),
    (2, 1),
    (3, 1),
    (1, 0),
]

for u, v in edges:
    g.add_edge(u, v)

# g.show()
g.topological_print()
# print(g.has_edge(4 , 7))
# print(g.has_edge(7 , 4))