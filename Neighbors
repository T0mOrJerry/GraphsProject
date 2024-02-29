def find_neighbors(base, words):
    neighbors=[]
    for a in words:
        counter_of_difference = 0
        for i, j in base, a:
            if i != j:
                counter_of_difference += 1
            if counter_of_difference == 2:
                break
        if counter_of_difference == 1:
            neighbors.append(a)

