# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# https://projecteuler.net/project/images/p015.png

# How many such routes are there through a 20×20 grid?

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer(x=20):
    c = 1
    for i in range(1, x + 1):
        c = c * (x + i) / i
    return int(c)


if __name__ == '__main__':
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
