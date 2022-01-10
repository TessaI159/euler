from decorator import time_and_memory_decorator as tamd
from euler import proper_divisors
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def d(n):
    return sum(proper_divisors(n))

@tamd
def find_answer():
    ans = []
    
    for n in range(100, 10000):
        b = d(n)
        a = d(b)
        if a == n and a != b:
            ans.append(n)
            
    return sum(set(ans))


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
