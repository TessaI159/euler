# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1**2
# 15 = 7 + 2×2**2
# 21 = 3 + 2×3**2
# 25 = 7 + 2×3**2
# 27 = 19 + 2×2**2
# 33 = 31 + 2×1**2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from timer import Timer
from euler import is_prime, read_input, is_prime

def find_answer():
    input_data = read_input()

    odd_comps = []
    real_odd_comps = [x for x in range(3,10**6,2) if not is_prime(x)]
    for a in input_data:
        for b in range(1,76):
            odd_comps.append(int(a) + (2 * (b**2)))
    odd_comps = list(filter(lambda x : x % 2 != 0 and not is_prime(x), odd_comps))
    odd_comps.sort()
    odd_comps = set(odd_comps)
    real_odd_comps.sort()

    print("Testing")
    for a,b in zip(odd_comps, real_odd_comps):
        if a != b:
            return b
        
    

    

t = Timer()
t.time(find_answer)
