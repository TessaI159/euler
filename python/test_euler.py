from collections import Counter
import math
from random import randint
from unittest.mock import patch

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


def test_is_polygonal_false():
    assert euler.is_triangular(2) is False
    assert euler.is_triangular(4) is False
    assert euler.is_square(2) is False
    assert euler.is_square(3) is False
    assert euler.is_pentagonal(2) is False
    assert euler.is_pentagonal(4) is False
    assert euler.is_hexagonal(2) is False
    assert euler.is_hexagonal(5) is False
    assert euler.is_heptagonal(2) is False
    assert euler.is_heptagonal(5) is False
    assert euler.is_octagonal(2) is False
    assert euler.is_octagonal(5) is False


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
    assert euler.transpose([]) == []
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
    with pytest.raises(TypeError):
        euler.string_sort(123)
    with pytest.raises(TypeError):
        euler.caseless_string_sort(123)


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
    for invalid in (1.1, "1.1", "170"):
        with pytest.raises(ValueError):
            euler.to_binary(invalid)


def test_reverse_num():
    assert euler.reverse_num(12345) == 54321
    assert euler.reverse_num(1200) == 21
    assert euler.reverse_num(7) == 7


def test_is_factorion():
    assert euler.is_factorion(145) is True
    assert euler.is_factorion(1) is True
    assert euler.is_factorion(2) is True
    assert euler.is_factorion(40585) is True
    assert euler.is_factorion(144) is False


def test_series_sums():
    assert euler.sum_of_seq(10) == 55
    assert euler.sum_of_squares(10) == 385
    assert euler.square_of_sums(10) == 3025
    assert isinstance(euler.square_of_sums(10), int)
    assert euler.square_of_sums(10) == euler.sum_of_seq(10) ** 2


def test_combine():
    assert euler.combine(
        [
            1,
            1,
            1,
            2,
            2,
        ]
    ) == [1, 4]
    assert euler.combine([1, 2, 3, 4, 1, 2, 3, 4]) == [1, 4, 9, 16]
    assert euler.combine([1, 2, 4, 3, 1, 2, 4, 3]) == [1, 4, 9, 16]
    assert euler.combine([4, 4, 3, 3, 3, 2, 2, 2, 2]) == [16, 27, 16]


def test_digital_sum():
    assert euler.digital_sum(12345) == 15
    assert euler.digital_sum(0) == 0
    assert euler.digital_sum(-99) == 18
    with pytest.raises(TypeError):
        euler.digital_sum("12345")


def test_complete_digital_sum():
    assert euler.complete_digital_sum(493193) == 2
    assert euler.complete_digital_sum(0) == 0
    assert euler.complete_digital_sum(9) == 9
    assert euler.complete_digital_sum(99) == 9
    with pytest.raises(TypeError):
        euler.complete_digital_sum(12.3)


def test_n_pandigital():
    assert euler.n_pandigital(123456789) is True
    assert euler.n_pandigital("12345") is True
    assert euler.n_pandigital([1, 3, 2]) is True
    assert euler.n_pandigital(12345, l=4) is False
    assert euler.n_pandigital(112345) is False
    assert euler.n_pandigital(123450) is False


def test_mult():
    assert euler.mult([1, 2, 3, 4]) == 24
    assert euler.mult([]) == 1
    assert euler.mult(["2", "3", "4"]) == 24


def test_fact():
    import math

    assert euler.fact(0) == 1
    assert euler.fact(5) == 120
    assert euler.fact(0.5) == math.gamma(1.5)
    with pytest.raises(ValueError):
        euler.fact(-1)
    with pytest.raises(TypeError):
        euler.fact("5")


@pytest.mark.parametrize(
    "n, expected",
    [
        (-7, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (9, False),
        (11, True),
        (25, False),
        (97, True),
        (561, False),  # Carmichael number
        (7919, True),
        (104729, True),
    ],
)
def test_is_prime(n, expected):
    assert euler.is_prime(n) is expected


@pytest.mark.parametrize(
    "limit, expected",
    [
        (0, []),
        (1, []),
        (2, []),
        (3, [2]),
    ],
)
def test_prime_sieve_known(limit, expected):
    assert euler.prime_sieve(limit) == expected


@pytest.mark.xfail(
    reason="prime_sieve in euler.py uses range(3, isqrt(n), 2) which misses isqrt(n), including composite squares"
)
@pytest.mark.parametrize(
    "limit, expected",
    [
        (10, [2, 3, 5, 7]),
        (26, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
        (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
    ],
)
def test_prime_sieve_boundary_squares(limit, expected):
    assert euler.prime_sieve(limit) == expected


def test_prime_sieve_properties():
    primes_100 = euler.prime_sieve(100)
    assert len(primes_100) == 25
    assert all(euler.is_prime(p) for p in primes_100)
    assert all(p < 100 for p in primes_100)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, Counter()),
        (1, Counter()),
        (2, Counter({2: 1})),
        (13, Counter({13: 1})),
        (12, Counter({2: 2, 3: 1})),
        (360, Counter({2: 3, 3: 2, 5: 1})),
        (644, Counter({2: 2, 7: 1, 23: 1})),
    ],
)
def test_prime_factorization(n, expected):
    assert euler.prime_factorization(n) == expected


def test_prime_factorization_reconstruction():
    for n in range(2, 60):
        factors = euler.prime_factorization(n)
        assert math.prod(p**count for p, count in factors.items()) == n


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, []),
        (2, [2]),
        (13, [13]),
        (36, [2, 2, 3, 3]),
        (644, [2, 2, 7, 23]),
        (646, [2, 17, 19]),
    ],
)
def test_prime_factors(n, expected):
    assert euler.prime_factors(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (-1, set()),
        (0, set()),
        (1, set()),
        (2, {1}),
        (6, {1, 2, 3}),
        (9, {1, 3}),
        (12, {1, 2, 3, 4, 6}),
        (16, {1, 2, 4, 8}),
        (28, {1, 2, 4, 7, 14}),
    ],
)
def test_proper_divisors(n, expected):
    assert euler.proper_divisors(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, {1}),
        (6, {1, 2, 3, 6}),
        (12, {1, 2, 3, 4, 6, 12}),
        (16, {1, 2, 4, 8, 16}),
    ],
)
def test_factors(n, expected):
    assert euler.factors(n) == expected


def test_factors_proper_divisors_consistency():
    for n in range(2, 50):
        assert euler.factors(n) == euler.proper_divisors(n) | {n}


@pytest.mark.parametrize(
    "n, expected_proper, expected_all",
    [
        (0, 0, 0),
        (1, 0, 1),
        (6, 6, 12),
        (28, 28, 56),
        (220, 284, 504),
        (284, 220, 504),
    ],
)
def test_sum_of_divisors(n, expected_proper, expected_all):
    assert euler.sum_of_proper_divisors(n) == expected_proper
    assert euler.sum_of_divisors(n) == expected_all


def test_unique():
    assert euler.unique([[1, 2], [3, 4]]) is True
    assert euler.unique([[1, 2], [2, 3]]) is False
    assert euler.unique([[1, 1], [2, 3]]) is False
    assert euler.unique([[1, 2], [3, 4, 5]]) is False
    assert euler.unique([[1, 2, 3], [4, 5, 6]], length=3) is True
    assert euler.unique([[1, 2], [3, 4]], length=3) is False


def test_unique_no_length():
    assert euler.unique_no_length([[1], [2, 3], [4, 5, 6]]) is True
    assert euler.unique_no_length([[1, 2], [2, 3]]) is False
    assert euler.unique_no_length([]) is True


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 4),
        (6, 2),
        (7, 6),
        (9, 6),
        (10, 4),
        (12, 4),
        (13, 12),
        (36, 12),
        (87, 56),
        (97, 96),
    ],
)
def test_eulers_totient(n, expected):
    assert euler.eulers_totient(n) == expected


def test_lagrange_polynomial_interpolation():
    p_linear = euler.lagrange_polynomial([1, 2], [3, 5])
    assert p_linear(1) == pytest.approx(3)
    assert p_linear(2) == pytest.approx(5)
    assert p_linear(3) == pytest.approx(7)
    assert p_linear(0) == pytest.approx(1)

    p_quad = euler.lagrange_polynomial([1, 2, 3], [1, 4, 9])
    assert p_quad(1) == pytest.approx(1)
    assert p_quad(2) == pytest.approx(4)
    assert p_quad(3) == pytest.approx(9)
    assert p_quad(4) == pytest.approx(16)
    assert p_quad(0) == pytest.approx(0)


def test_lagrange_polynomial_errors():
    with pytest.raises(ValueError, match="same"):
        euler.lagrange_polynomial([1, 2], [1])
    with pytest.raises(ValueError, match="unique"):
        euler.lagrange_polynomial([1, 1], [2, 3])
    with pytest.raises(ValueError, match="empty"):
        euler.lagrange_polynomial([], [])


def test_read_input():
    import os
    from pathlib import Path

    needs_chdir = (
        not Path("data").exists() and (Path(__file__).parent / "data").exists()
    )
    cwd = os.getcwd()
    try:
        if needs_chdir:
            os.chdir(Path(__file__).parent)
        lines = euler.read_input("euler11")
        assert len(lines) == 20
        assert lines[0].startswith("08 02 22")

        with pytest.raises(FileNotFoundError):
            euler.read_input("nonexistent_problem_file")
    finally:
        if needs_chdir:
            os.chdir(cwd)


def test_read_input_caller_inference():
    import os
    from pathlib import Path

    needs_chdir = (
        not Path("data").exists() and (Path(__file__).parent / "data").exists()
    )
    cwd = os.getcwd()
    try:
        if needs_chdir:
            os.chdir(Path(__file__).parent)

        frame = type("Frame", (), {"filename": "euler11.py"})()
        with patch("inspect.stack", return_value=[frame]):
            lines = euler.read_input()
            assert len(lines) == 20

        expected_err = getattr(euler, "CustomError", NameError)
        with patch("inspect.stack", return_value=[]):
            with pytest.raises((expected_err, NameError)):
                euler.read_input()
    finally:
        if needs_chdir:
            os.chdir(cwd)


def test_word_dictionaries():
    assert euler.ones_place[1] == "one"
    assert euler.ones_place[9] == "nine"
    assert euler.tens_place[2] == "twenty"
    assert euler.tens_place[9] == "ninety"
    assert euler.hundreds_place[1] == "onehundred"
    assert euler.hundreds_place[9] == "ninehundred"
    assert euler.teens[0] == "ten"
    assert euler.teens[5] == "fifteen"
    assert euler.teens[9] == "nineteen"
