from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    n = len(array)

    array = array[:]

    for j in range(n - 1):
        for i in range(n - 1 - j):
            f = 0
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                f = 1
            if not f:
                continue

    return array
