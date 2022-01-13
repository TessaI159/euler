# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# Answer is 233168

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def sum_arith_seq(b, e):
    """Returns the sum of all multiples of b below e"""
    return ((((e-1) // b) * (((e-1) // b) + 1)) >> 1) * b

@tamd
def find_answer(n=1000):
    return sum_arith_seq(3,n) + sum_arith_seq(5,n) - sum_arith_seq(15,n)

if __name__ == '__main__':
    print(filename, ': ', end='')

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)

