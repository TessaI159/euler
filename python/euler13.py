from timer import Timer
from euler import read_input

def find_answer():
    return str(sum([int(x) for x in read_input()]))[:10]

t = Timer()
t.time(find_answer)
