# By counting carefully it can be seen that a rectangular grid measuring $3$ by
# $2$ contains eighteen rectangles
# Although there exists no rectangular grid that contains exactly two million
# rectangles, find the area of the grid with the nearest solution.


from pathlib import Path

from decorator import time_and_memory_decorator as tamd

from math import prod

filename = Path(__file__).stem


def count_rectangles(w, h):
    return (w * h * (w + 1) * (h + 1)) >> 2


@tamd
def find_answer():
    # Smallest w with arith_sum(w)>target
    # count_rectangles(w,h)=target+1000
    w = 2000
    h = 1
    least = 10000
    least_dim = (w, h)

    while True:
        # There has to be a formula for the maximal w given h, yeah? Find it.
        w = 2000
        h += 1

        while count_rectangles(w, h) > target:
            w -= 1
        if abs(count_rectangles(w, h) - target) < least:
            least = abs(count_rectangles(w, h) - target)
            least_dim = (w, h)
        if abs(count_rectangles(w + 1, h) - target) < least:
            least = abs(count_rectangles(w + 1, h) - target)
            least_dim = (w + 1, h)

        if h > w:
            break
    return prod(least_dim)


if __name__ == "__main__":
    target = 2000000
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
