# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# Trivial in Python

from decorator import time_and_memory_decorator as tamd
from pathlib import Path

filename = Path(__file__).stem

@tamd
def find_answer():
    x = 1
    champernowne = ''
    while len(champernowne) < 10**6 + 1:
        champernowne += str(x)
        x += 1

    i = 1
    answer = 1
    while i <= 10**6:
        answer *= int(champernowne[i - 1])
        i *= 10
        
    return answer


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
