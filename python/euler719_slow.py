# We define an S-number to be a natural number, n, that is a perfect square and its square root
# can be obtained by splitting the decimal representation of n into 2 or more numbers
# then adding the numbers

# For example, 81 is an S-number because sqrt(81) = 8 + 1
# 6724 is an S-number because sqrt(6724) = 6 + 72 + 4
# 8281 is an S-number because sqrt(8281) = 8 + 2 + 81
# 9801 is an S-number because sqrt(9801) = 98 + 0 + 1

# Further, we define T(n) as the sum of all S-numbers n <= N.
# You are given T(10**4) = 41333

# Find T(10**12)

from math import sqrt
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

# small_number, large_number
def s_number(sn, ln):
    pwr = 1
    
    while True:
        pwr *= 10

        # The far right digit of ln, if pwr is 10
        right = ln % pwr
        if right > sn:
            return False

        # All the digits except the digits in right
        left = ln // pwr
        if left + right == sn:
            return True

        

        # If left has more than two digits, we continue.
        # Otherwise, we do not.
        if left < 10:
            return False

        # We subtract right from sn because we are assuming that right is a piece of the sum
        # And then we are testing the combinations of all the other digits
        # Against the number we are left with after subtraction
        if sn > right and (s_number(sn - right, left)):
            return True
        


def square_generator(lim):
    for num in range(4, int(sqrt(lim) + 1)):
        yield num**2
        

@tamd
def find_answer(lim=10**12):
    square_gen = square_generator(lim)

    answer = 0
    for square in square_gen:
        if s_number(int(sqrt(square)), square):
            answer += square
    return answer


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
