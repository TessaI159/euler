from timer import Timer
from euler import is_prime

def find_answer(r):
    return sum([x for x in range(3,r,2) if is_prime(x)]) + 2

t = Timer()
t.time(find_answer, 2000000)
