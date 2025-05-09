# Undirected Weighted Graph
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight = None):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
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
    
    def get_edges(self, vertex):
        edges = []
        if vertex in self.graph:
            for vertex2, weight in self.graph[vertex].items():
                edges.append((vertex2, weight))
        return edges
    
    def get_vertices(self):
        return set(self.graph.keys())
    
    def get_MST_prims(self, start_vertex):
        MST_edges = []
        visited = set()
        all_vertices = self.get_vertices()

        visited.add(start_vertex)

        while visited != all_vertices:
            min_weight = float('inf')
            min_edge = None

            for vertex in visited:
                edges = self.get_edges(vertex)

                for (vertex2, weight) in edges:

                    if vertex2 not in visited and weight < min_weight:
                        min_edge = (vertex, vertex2, weight)
                        min_weight = weight

            if min_edge is None:
                break  # Graph is disconnected

            MST_edges.append(min_edge)
            visited.add(min_edge[1])

        return MST_edges

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.in_deg = 0
    
    def add_child(self, child):
        for i in self.children:
            if i.value == child.value:        
                return
        self.children.append(child)
        child.in_deg += 1

    def remove_child(self, value):
        for child in self.children:
            if child.value == value:
                self.children.remove(child)
                child.in_deg -= 1
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

# Directed Acylcic Graph
class directed_tree:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)
        return self.nodes[value]
    
    def add_edge(self, from_value, to_value):
        from_node = self.add_node(from_value)
        to_node = self.add_node(to_value)
        from_node.add_child(to_node)

    def remove_node(self, value):
        try:
            for child in self.nodes[value].children:
                child.in_deg -= 1
            self.nodes.pop(value)
        except KeyError:
            print("node not in tree")

    def show(self):
        for node in self.nodes.values():
            children_values = [child.value for child in node.children]
            print(f"{node.value} → {children_values} | in degree = {node.in_deg}")
    
    def has_node(self, value):
        return value in self.nodes

    def has_edge(self, from_value, to_value):
        if not self.has_node(from_value) or not self.has_node(to_value):
            return False
        for child in self.nodes[from_value].children:
            if child.value == to_value:
                return True
        return False
    
    def topological_print(self):
        for node in self.nodes.values():
            if node.in_deg == 0:
                print(node.value, end=" ")
                self.remove_node(node.value)
                self.topological_print()
                return
        print("")
        return
