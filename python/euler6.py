from timer import Timer
from euler import *

def euler_6(n):
    return square_of_sums(1, n) - sum_of_squares(1, n)

t = Timer()
t.time(euler_6, 100)
    
