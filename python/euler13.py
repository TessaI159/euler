# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

# Numbers in data/euler13_input.txt

from decorator import time_and_memory_decorator as tamd
from euler import read_input
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    return str(sum([int(x) for x in read_input(filename)]))[:10]

if __name__ == '__main__':
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
