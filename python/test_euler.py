import pytest, euler
from random import randint


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
