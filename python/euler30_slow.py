# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4

# As 1 = 1**4 is not a sum, it is not included

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def written_as_x_power(x, num):
    s_num = str(num)
    powers = 0
    
    for n in s_num:
        powers += int(n)**x
    return sum([int(n)**x for n in s_num]) == num


@tamd
def find_answer(x=5):

    return sum([n for n in range(2,10**6) if written_as_x_power(x, n)])


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
