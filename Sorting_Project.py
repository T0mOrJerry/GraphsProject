def binary_search(data: list[int], value: int) -> bool:
    while data:
        cursor = len(data) // 2
        if data[cursor] == value:
            return True
        elif data[cursor] < value:
            data = data[cursor + 1:]
        else:
            data = data[:cursor]
    return False


def sequential_search(data: list[int], value: int) -> tuple[bool, int]:
    for i in range(len(data)):
        if data[i] == value:
            return True, i
    return False, -1


def bubble_sort(data: list[int]) -> list[int]:
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def selection_sort(data: list[int]) -> list[int]:
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j] < data[i]:
                data[j], data[i] = data[i], data[j]
    return data


def insertion_sort(data: list[int]) -> list[int]:
    for i in range(1, len(data)):
        a = i
        storage = data[i]
        while a > 0 and data[a - 1] > storage:
            data[a] = data[a - 1]
            a -= 1
        data[a] = storage
    return data
