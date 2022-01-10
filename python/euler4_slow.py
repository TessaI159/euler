# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from decorator import time_and_memory_decorator as tamd
from euler import is_palindrome
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def product_of_three(n):
    for x in range(100, 1000):
        if n % x == 0 and len(str(int(n / x))) == 3:
            return True
    return False

@tamd
def find_answer():
    num = 10000000
    while True:
        if is_palindrome(num) and product_of_three(num):
            return num
        num -= 1


if __name__ == '__main__':            
    print(filename, ': ', end='')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)

