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

    def going_through(self, stack, visited):
        while stack:
            node = stack.pop(0)
            for i in self.connections[node]:
                if i not in visited:
                    stack.append(i)
            visited.append(node)
        return visited




def is_network_connected(graph):
    a = graph.going_through([list(graph.connections.keys())[0]], [])
    print(a)
    if len(a) == len(list(graph.connections.keys())):
        return True
    else:
        return False





network = Graph()
# Add vertices and connect them
network.add_vertex("A")
network.add_vertex("B")
network.add_edge("A", "B")
print('Done')
print(is_network_connected(network))