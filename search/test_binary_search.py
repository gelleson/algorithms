from search.binary_search import binary_search


def test_benchmark_binary(benchmark):
    benchmark(binary_search, 5, [1, 2, 3, 4, 5, 6, 7, 8])


def test_binary_search():
    result = binary_search(5, [1, 2, 3, 4, 5, 6, 7, 8])
    assert result is not None
    assert result == 5
