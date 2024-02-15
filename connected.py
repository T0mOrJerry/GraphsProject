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
    def shortest_path(self, start, end):
        visited = set()
        queue = [(start, 0)]

        while queue:
            current_member, distance = queue.pop(0)

            if current_member == end:
                return distance

            if current_member not in visited:
                visited.add(current_member)
                friends = self.connection[current_member]
                queue.extend((friend, distance + 1) for friend in friends)

        return 0
    
    def is_connected(self):
        x = len(self.connections)
        key_con = list(self.connections.keys())
        for i in key_con:
            for j in key_con:
                if i != j:
                    if self.shortest_path(i, j) == 0:
                        return "The graph it is not connected"
        return "the graph is connected"
                
            
        


network = Graph()
# Add vertices and connect them
network.add_vertex("A")
network.add_vertex("B")
network.add_edge("A", "B")
network.is_connected()
print('Done')
