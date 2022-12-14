# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def calc(constraint, step=None):
    """Calculates the smallest number divisible by all numbers from 1 to constraint"""
    if constraint == 1:
        return 1
    
    if not step:
        step = constraint
        div = 2
        loop = True
        current = step
    else:
        div = constraint
        loop = False
        current = step

    if loop:
        while True:
            if current % div != 0:
                div = 2
                current += step
            elif current % div == 0 and div == constraint:
                return current
            div += 1
    else:
        while True:
            if current % div != 0:
                current += step
            else:
                return current
            

@tamd
def find_answer():
    s = calc(1)
    for x in range(2, 21):
        s = calc(x, s)
    return s

if __name__ == '__main__':
    print(filename, ': ', end='')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)

    
