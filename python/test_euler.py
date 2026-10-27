from random import randint

import pytest

import euler


@pytest.mark.parametrize(
    "n, expected",
    [(1, 1), (2, 3), (3, 6), (4, 10), (5, 15), (6, 21)],
)
def test_triangle_numbers_known(n, expected):
    assert euler.triangle_number(n) == expected


def test_triangle_numbers_recurrence_relation():
    for _ in range(20):
        a = randint(10, 50)
        assert euler.triangle_number(a) == euler.triangle_number(a - 1) + a


@pytest.mark.parametrize(
    "n, expected", [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]
)
def test_square_numbers_known(n, expected):
    assert euler.square_number(n) == expected


def test_square_numbers_recurrence_relation():
    for _ in range(20):
        a = randint(10, 50)
        assert euler.square_number(a) == euler.square_number(a - 1) + 2 * a - 1


@pytest.mark.parametrize(
    "n, expected", [(1, 1), (2, 5), (3, 12), (4, 22), (5, 35), (6, 51)]
)
def test_pentagonal_numbers_known(n, expected):
    assert euler.pentagon_number(n) == expected


def test_pentagonal_numbers_recurrence_relation():
    for _ in range(20):
        a = randint(10, 50)
        assert euler.pentagon_number(a) == euler.pentagon_number(a - 1) + 3 * a - 2


@pytest.mark.parametrize(
    "n, expected", [(1, 1), (2, 6), (3, 15), (4, 28), (5, 45), (6, 66)]
)
def test_hexagonal_numbers_known(n, expected):
    assert euler.hexagon_number(n) == expected


def test_hexagonal_numbers_recurrence_relation():
    for _ in range(20):
        a = randint(10, 50)
        assert euler.hexagon_number(a) == euler.hexagon_number(a - 1) + 4 * a - 3


@pytest.mark.parametrize(
    "n, expected", [(1, 1), (2, 7), (3, 18), (4, 34), (5, 55), (6, 81)]
)
def test_heptagonal_numbers_known(n, expected):
    assert euler.heptagon_number(n) == expected


def test_heptagonal_numbers_recurrence_relation():
    for _ in range(20):
        a = randint(10, 50)
        assert euler.heptagon_number(a) == euler.heptagon_number(a - 1) + 5 * a - 4


@pytest.mark.parametrize(
    "n, expected", [(1, 1), (2, 8), (3, 21), (4, 40), (5, 65), (6, 96)]
)
def test_octagonal_numbers_known(n, expected):
    assert euler.octagon_number(n) == expected


def test_octagonal_numbers_recurrence_relation():
    for _ in range(20):
        a = randint(10, 50)
        assert euler.octagon_number(a) == euler.octagon_number(a - 1) + 6 * a - 5


def test_is_triangular():
    for _ in range(20):
        a = randint(10, 50)
        assert euler.is_triangular(euler.triangle_number(a)) is True


def test_is_square():
    for _ in range(20):
        a = randint(10, 50)
        assert euler.is_square(euler.square_number(a)) is True


def test_is_pentagonal():
    for _ in range(20):
        a = randint(10, 50)
        assert euler.is_pentagonal(euler.pentagon_number(a)) is True


def test_is_hexagonal():
    for _ in range(20):
        a = randint(10, 50)
        assert euler.is_hexagonal(euler.hexagon_number(a)) is True


def test_is_heptagonal():
    for _ in range(20):
        a = randint(10, 50)
        assert euler.is_heptagonal(euler.heptagon_number(a)) is True


def test_is_octagonal():
    for _ in range(20):
        a = randint(10, 50)
        assert euler.is_octagonal(euler.octagon_number(a)) is True


def test_convert_to_base_invalid_input():
    with pytest.raises(TypeError):
        euler.convert_to_base("10", 2)
    with pytest.raises(TypeError):
        euler.convert_to_base(10, "2")
    with pytest.raises(ValueError):
        euler.convert_to_base(10, 1)


def test_convert_to_base():
    assert euler.convert_to_base(0, 2) == [0]
    assert euler.convert_to_base(750, 16) == [2, 14, 14]
    assert euler.convert_to_base(-12, 2) == ["-", 1, 1, 0, 0]


def test_jagged_array_transpose():
    with pytest.raises(ValueError):
        euler.transpose([[1, 2, 3], [1, 2]])
    with pytest.raises(TypeError):
        euler.transpose([1])
    with pytest.raises(TypeError):
        euler.transpose([[1, 2, 3], [2, 3, 4], 1])


def test_transpose():
    assert euler.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert euler.transpose([[[1, 2], [3, 4]], [5, 6]]) == [[[1, 2], 5], [[3, 4], 6]]
    assert euler.transpose(euler.transpose([[[1, 2], [3, 4]], [5, 6]])) == [
        [[1, 2], [3, 4]],
        [5, 6],
    ]


def test_is_permutation():
    assert euler.is_permutation("", "") is True
    assert euler.is_permutation("abc", "cba") is True
    assert euler.is_permutation("Abc", "cba") is False
    assert euler.is_permutation(12345, 52341) is True


def test_string_sort():
    assert euler.string_sort("ciwldigj") == "cdgiijlw"
    assert euler.string_sort("CIWldiGj") == "CGIWdijl"
    assert euler.caseless_string_sort("CIWldiGj") == "cdgiijlw"


def test_infinite_primes():
    import itertools

    first_10 = list(itertools.islice(euler.infinite_primes(), 10))
    assert first_10 == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Test boundary starting conditions
    assert next(euler.infinite_primes(start=7)) == 7
    assert next(euler.infinite_primes(start=8)) == 11
    assert next(euler.infinite_primes(start=10)) == 11

    # 1,000th prime is 7919
    thousandth = next(itertools.islice(euler.infinite_primes(), 999, 1000))
    assert thousandth == 7919

    # 10,000th prime is 104729
    ten_thousandth = next(itertools.islice(euler.infinite_primes(), 9999, 10000))
    assert ten_thousandth == 104729


def test_is_palindrome():
    assert euler.is_palindrome("racecar") is True
    assert euler.is_palindrome("Abcba") is False
    assert euler.is_palindrome(12321) is True
    assert euler.is_palindrome(12345) is False
    assert euler.is_palindrome([1, 2, 3, 2, 1]) is True
    assert euler.is_palindrome([1, 2, 3]) is False


def test_to_binary():
    assert euler.to_binary(0) == "0"
    assert euler.to_binary(-1) == "-1"
    assert euler.to_binary(170) == "10101010"
    with pytest.raises(ValueError):
        euler.to_binary(1.1)
        euler.to_binary("1.1")
        euler.to_binary("170")
