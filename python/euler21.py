from timer import Timer
from euler import proper_divisors

def d(n):
    return sum(proper_divisors(n))

def find_answer():
    ans = []
    
    for n in range(100, 10000):
        b = d(n)
        a = d(b)
        if a == n and a != b:
            ans.append(n)
            
    return sum(set(ans))


t = Timer()
t.time(find_answer)
