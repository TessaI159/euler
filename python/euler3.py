from timer import Timer
from euler import is_prime
import math


# def find_answer(n):
#     return prime_factors(n)[-1]


# t = Timer()
# t.time(find_answer, 600851475143)



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


            
t = Timer()
t.time(prime_factors, 427)
