# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

from pathlib import Path

from decorator import time_and_memory_decorator as tamd
from euler import is_permutation

filename = Path(__file__).stem


@tamd
def find_answer():
    x = 0
    while True:
        x += 1
        multiples = [x * a for a in range(2, 7)]

        if all([is_permutation(multiple, multiples[0]) for multiple in multiples]):
            return x


if __name__ == "__main__":
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
