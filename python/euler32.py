from decorator import time_and_memory_decorator as tamd
from itertools import permutations
import inspect
import sys

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def sub_string_multiplication(perm):
    perm = ''.join(perm)
    if int(perm[:2]) * int(perm[2:5]) == int(perm[5:]):
        return int(perm[5:])
    
    if int(perm[:1]) * int(perm[1:5]) == int(perm[5:]):
        return int(perm[5:])

    
@tamd
def find_answer():
    ans = []
    perms = (x for x in permutations('123456789'))
    
    for p in perms:
        if (temp := sub_string_multiplication(p)):            
            ans.append(temp)
    ans = set(ans)
    return sum(ans)

if __name__ == '__main__':
    print(filename, ': ', end='')

    answer, mem, time = find_answer()
    print(answer)
    print(mem)
    print(time)
