class Graph:
    def __init__(self):
        self.people = {}
        self.relations = {}

    def add_member(self, name, age=None, location=None):
        self.people[name] = [age, location, 0]
        self.relations[name] = []

    def add_relationship(self, name1, name2):
        if name1 not in self.people or name2 not in self.people:
            print('ERROR: A person is not in the network')
        else:
            self.relations[name1].append(name2)
            self.people[name1][2] += 1
            self.relations[name2].append(name1)
            self.people[name2][2] += 1

    def find_friends(self, name):
        return self.relations[name]

    def shortest_path(self, start, end):
        visited = set()
        queue = [(start, 0)]
        while queue:
            current_member, distance = queue.pop(0)
            if current_member == end:
                return distance
            if current_member not in visited:
                visited.add(current_member)
                friends = self.relations[current_member]
                queue.extend((friend, distance + 1) for friend in friends)
        return 0


network = Graph()
# Add some members to the network
network.add_member("Alice", age=25, location="New York")
network.add_member("Bob", age=30, location="Los Angeles")
network.add_member("Charlie", age=35, location="Chicago")
network.add_member("David", age=40, location="Seattle")
# Add some relationships between members
network.add_relationship("Alice", "Bob")
network.add_relationship("Bob", "Charlie")
network.add_relationship("Charlie", "David")
alice_friends = network.find_friends("Alice")
print(alice_friends)  # Output: ["Bob"]

# Find the shortest path of each member
shortest_path = network.shortest_path("Alice", "David")
print(shortest_path)  # Output: 3
