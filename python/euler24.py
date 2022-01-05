from timer import Timer
from itertools import permutations

def find_answer(string, ind):
    permutions = sorted(''.join(chars) for chars in permutations(string))
    return permutions[ind - 1]

t = Timer()
t.time(find_answer, '0123456789', 10**6)
