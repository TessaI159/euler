# The example for this one is impossible to copy and paste here easily
# Find it at https://projecteuler.net/problem=57

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    expansions = 1000
    pn = 1
    pd = 1
    n = 3
    d = 2
    answer = 0

    for x in range(expansions):
        pn, n = n, 2 * n + pn
        pd, d = d, 2 * d + pd
        if len(str(n)) > len(str(d)):
            answer += 1
            
    return answer

if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
