# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from decorator import time_and_memory_decorator as tamd
from euler import is_palindrome
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'





@tamd
def find_answer():
    products_of_three = []
    for x in range(100,1000):
        for y in range(x + 1,1000):
            if is_palindrome(x * y):
                products_of_three.append(x * y)
                
    products_of_three.sort()
    return products_of_three[-1]


if __name__ == '__main__':            
    print(filename, ': ', end='')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)

