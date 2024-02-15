class Graph:
    def __init__(self):
        self.people = {}
        self.relations = {}

    def add_member(self, name, age=None, location=None):
        self.people[name] = [age, location]
        self.relations[name] = []

    def add_relationship(self, name1, name2):
        if name1 not in self.people or name2 not in self.people:
            print('ERROR: A person is not in the network')
        else:
            self.relations[name1].append(name2)
            self.relations[name2].append(name1)

    def find_friends(self, name):
        return self.relations[name]


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
print(alice_friends) # Output: ["Bob"]