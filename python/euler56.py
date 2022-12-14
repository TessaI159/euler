# A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

from euler import digital_sum
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    max_digital = 0
    
    for a in range(1,100):
        for b in range(1,100):
            if (temp := digital_sum(a**b)) > max_digital:
                max_digital = temp
    return max_digital


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
