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


find_neighbors('cat', ['cot', 'rat', 'bat'])