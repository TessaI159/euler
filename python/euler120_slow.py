# Insert question description here

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def remainder(a, n):
    return (((a-1)**n)+((a+1)**n)) % (a**2)

def max_remainder(a):
    terms = []
    n = 1
    terms.append(remainder(a, n))
    n += 1
    while remainder(a, n) != terms[0]:
        terms.append(remainder(a, n))
        n += 1
    return max(terms)
    
        
        
        
    
@tamd
def find_answer():
    total = 0
    for a in range(3, 1001):
        total += max_remainder(a)
    return total


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
