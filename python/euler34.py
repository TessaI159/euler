# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

from decorator import time_and_memory_decorator as tamd
import inspect
from euler import fact, sum_of_fact

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    ans = 0
    for i in range(3, 50000):
        if sum_of_fact(i):
            ans += i
    return ans

if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
