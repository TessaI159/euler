# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from decorator import time_and_memory_decorator as tamd
from euler import is_prime
import math
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    return prime_factors(600851475143)[-1]

def find_answer_no_time():
    return prime_factors(600851475143)[-1]

def prime_factors(n):
    answers = []

    if is_prime(n):
        return [n]
    
    while n % 2 == 0:
        answers.append(2)
        n /= 2
        
    for i in range(3,int(math.sqrt(n) + 1), 2):
        while n % i == 0:
            answers.append(i)
            n /= i
    if n > 2:
        answers.append(int(n))
            
    return answers


if __name__ == '__main__':
    print(filename, ': ', end='')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
