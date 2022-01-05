from timer import Timer
from euler import n_pandigital, is_prime
from itertools import permutations

def find_answer():
    for x in range(9,0,-1):
        string = ''.join([str(c) for c in range(1,x + 1)])
        permutions = sorted(int(''.join(chars)) for chars in permutations(string))
        permutions.reverse()
        for p in permutions:
            if is_prime(p):
                return p
        

t = Timer()
t.time(find_answer)
