# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximise?

from decorator import time_and_memory_decorator as tamd
from pathlib import Path

filename = Path(__file__).stem
    

@tamd
def find_answer():
    solution = 0
    max_solutions = 0
    for p in range(2, 1000, 2):
        num_solutions = 0
        for a in range(2, (p//3) + 1):
            if (p * (p - (2 * a))) % (2 * (a - p)) == 0:
                num_solutions += 1
        if num_solutions > max_solutions:
            max_solutions = num_solutions
            solution = p
    return solution
            
        


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)



