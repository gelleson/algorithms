from recursion import fibonacci


def test_fibonacci():
    result = [fibonacci(x) for x in range(10)]
    assert [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] == result


def test_fibonacci_benchmark(benchmark):
    benchmark(fibonacci, 10)
