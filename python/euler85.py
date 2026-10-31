# By counting carefully it can be seen that a rectangular grid measuring $3$ by
# $2$ contains eighteen rectangles
# Although there exists no rectangular grid that contains exactly two million
# rectangles, find the area of the grid with the nearest solution.


from pathlib import Path

from decorator import time_and_memory_decorator as tamd

from math import prod, sqrt

filename = Path(__file__).stem


def count_rectangles(w, h):
    return int(w * h * (w + 1) * (h + 1)) >> 2


@tamd
def find_answer():
    target = 2000000
    # Smallest w with arith_sum(w)>target
    # Generalizing for any target would essentially equate to
    # w = (isqrt(target)+1) * 2
    # It wouldn't be the smallest such w, but it would be close enough
    w = 2000
    h = 0
    least = 10000
    least_dim = (w, h)

    while h <= w:
        h += 1

        a = h * (h + 1)
        b = h * (h + 1)
        c = -4 * target
        w = int((-b + sqrt(b**2 - 4 * a * c)) // (2 * a))
        if abs(count_rectangles(w, h) - target) < least:
            least = abs(count_rectangles(w, h) - target)
            least_dim = (w, h)
        if abs(count_rectangles(w + 1, h) - target) < least:
            least = abs(count_rectangles(w + 1, h) - target)
            least_dim = (w + 1, h)

    return prod(least_dim)


if __name__ == "__main__":
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
