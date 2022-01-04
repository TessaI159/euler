from timer import Timer
from euler import fact

def find_answer(n):
    return sum([int(x) for x in str(fact(n))])

t = Timer()
t.time(find_answer, 100)
