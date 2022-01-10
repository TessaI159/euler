# The sum of the squares of the first ten natural numbers is,

# 1**2 + 2**2 + ... + 10**2 = 385

# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)**2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 

# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

from decorator import time_and_memory_decorator as tamd
from euler import square_of_sums, sum_of_squares
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer(n=100):
    return int(square_of_sums(n) - sum_of_squares(n))

if __name__ == '__main__':
    print(filename, ": ", end="")
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
    
