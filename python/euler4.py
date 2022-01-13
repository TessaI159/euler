# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from decorator import time_and_memory_decorator as tamd
from euler import is_palindrome
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

products_of_three = []

for x in range(100,1000):
    for y in range(x + 1,1000):
        products_of_three.append(x * y)

products_of_three = [x for x in products_of_three if is_palindrome(x)]
products_of_three = set(products_of_three)


@tamd
def find_answer():
    num = 10000000
    while True:
        if num in products_of_three:
            return num
        num -= 1


if __name__ == '__main__':            
    print(filename, ': ', end='')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)

