# Insert question description here

from decorator import time_and_memory_decorator as tamd
import inspect
from euler import fact

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def digital_factorial(n):
    total = 0
    n_str = str(n)
    for letter in n_str:
        total += fact(int(letter))
        
    return total

def chain_length(n):
    chain = [n]
    cur_chain = digital_factorial(n)
    while cur_chain not in chain:
        chain.append(cur_chain)
        cur_chain = digital_factorial(cur_chain)
    return len(chain)
    
    

@tamd
def find_answer():
    ans = 0
    for i in range(1,10**6):
        if chain_length(i) == 60:
            ans += 1
    return ans


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
