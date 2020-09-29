import random

from sort.bubble_sort import bubble_sort


def test_bubble_sort():
    ordered_list = [x for x in range(100)]
    shuffled_list = ordered_list[:]
    random.shuffle(shuffled_list)

    sorted_list = bubble_sort(shuffled_list)

    assert ordered_list == sorted_list


def test_bubble_sort_benchmark(benchmark):
    ordered_list = [x for x in range(100)]
    shuffled_list = ordered_list[:]
    random.shuffle(shuffled_list)

    benchmark(bubble_sort, shuffled_list)
