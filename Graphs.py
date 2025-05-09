# Undirected Weighted Graph
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight = None):
        self.graph[vertex1][vertex2] = weight
        self.graph[vertex2][vertex1] = weight

    def delete_vertex(self, vertex):
        try:
            for i in self.graph[vertex]:
                self.graph[i].pop(vertex)
            self.graph.pop(vertex)
        except KeyError:
            print("Vertex not found")
    
    def delete_edge(self, vertex1, vertex2):
        try:
            self.graph[vertex1].pop(vertex2)
            self.graph[vertex2].pop(vertex1)
        except KeyError:
            print("Edge not found")

    def has_vertex(self, vertex):
        if vertex in self.graph:
            return True
        return False

    def has_edge(self, vertex1, vertex2):
        if vertex2 in self.graph[vertex1]:
            return True
        return False
    
    def get_edge_weight(self, vertex1, vertex2):
        if self.has_edge(vertex1, vertex2):
            return self.graph[vertex1][vertex2]
        return None

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        for i in self.children:
            if i.value == child.value:        
                return
        self.children.append(child)

    def remove_child(self, value):
        for child in self.children:
            if child.value == value:
                self.children.remove(child)
                return

    def show_children(self):
        print("Children: ")
        for child in self.children:
            print(child)
        print("_________")

    def __str__(self):
        return f"Value: {self.value}"
    
    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value


x = Node(5)
x.add_child(Node(1))
x.add_child(Node(23))
x.add_child(Node(1))
print(x)
x.show_children()
