from timer import Timer
from euler import factors

def tri_number(n):
    return int((n * (n + 1)) / 2)

def find_answer(n):
    x = 1
    length = len(factors(tri_number(x)))

    while length < n:
        x += 1
        length = len(factors(tri_number(x)))
        
    return tri_number(x)
        

t = Timer()
t.time(find_answer, 500)
