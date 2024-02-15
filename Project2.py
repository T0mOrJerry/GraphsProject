class Graph:
    def __init__(self):
        self.connections = {}

    def add_vertex(self, node):
        self.connections[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.connections or node2 not in self.connections:
            print('ERROR: Node does not exist')
        else:
            self.connections[node1].append(node2)
            self.connections[node2].append(node1)


network = Graph()
# Add vertices and connect them
network.add_vertex("A")
network.add_vertex("B")
network.add_edge("A", "B")
print('Done')