from timer import Timer
from euler import *

def euler_6(n):
    return int(square_of_sums(n) - sum_of_squares(n))

t = Timer()
t.time(euler_6, 100)
    
