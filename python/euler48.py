# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

#Trivial in Python

from decorator import time_and_memory_decorator as tamd
from pathlib import Path

filename = Path(__file__).stem

@tamd
def find_answer():
    total = 0

    for i in range(1,1001):
        total += i**i
        
    return str(total)[-10:]


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
