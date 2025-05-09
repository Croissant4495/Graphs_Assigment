from Graphs import *

print("________Question 1________")
g1 = directed_tree()

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
    g1.add_edge(u, v)

g1.topological_print()

print("________Question 2________")

g2 = Graph()
g2.add_edge('a', 'b', 4)
g2.add_edge('b', 'c', 8)
g2.add_edge('c', 'd', 7)
g2.add_edge('d', 'e', 9)
g2.add_edge('a', 'h', 8)
g2.add_edge('b', 'h', 11)
g2.add_edge('c', 'i', 2)
g2.add_edge('c', 'f', 4)
g2.add_edge('d', 'f', 14)
g2.add_edge('e', 'f', 10)
g2.add_edge('h', 'i', 7)
g2.add_edge('i', 'g', 6)
g2.add_edge('f', 'g', 2)
g2.add_edge('h', 'g', 1)


print(g2.get_MST_prims('a'))