with open("words_alpha.txt") as file:
    DATA = [i.strip() for i in file.readlines()]


def find_neighbors(base, words):
    neighbors = []
    for a in words:
        counter_of_difference = 0
        for i in range(len(a)):
            if base[i] != a[i]:
                counter_of_difference += 1
            if counter_of_difference == 2:
                break
        if counter_of_difference == 1:
            neighbors.append(a)
    return neighbors


def create_graph(root):
    li = list(filter(lambda x: len(x) == len(root), DATA))
    res = {}
    for i in li:
        res[i] = find_neighbors(i, li)
    return res


mainloop = True
while mainloop:
    start_word = input('Input your start word: ').lower()
    target_word = input('Input your target word: ').lower()
    if len(start_word) != len(target_word):
        print('Your words have different length - the algorithm is impossible. Try again!')
    elif start_word not in DATA or target_word not in DATA:
        print('For my best knowledge one of this words doesnt exists. try again!')
    else:
        graph = create_graph(start_word)
        success = False
        visited = set()
        queue = [(start_word, 0, f'{start_word}')]
        while queue:
            current_member, distance, path = queue.pop(0)
            if current_member == target_word:
                print(distance)
                print(path)
                success = True
                break
            if current_member not in visited:
                visited.add(current_member)
                neighbors = graph[current_member]
                queue.extend((neighbor, distance + 1, path + ' ' + neighbor) for neighbor in neighbors)
        mainloop = False
        if not success:
            print('There is no path')