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

