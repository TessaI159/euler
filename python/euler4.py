from timer import Timer
from euler import is_palindrome

def product_of_three(n):
    for x in range(100, 1000):
        if n % x == 0 and len(str(int(n / x))) == 3:
            return True
    return False

def three_digit_products(lim):
    num = lim
    while True:
        if is_palindrome(num) and product_of_three(num):
            return num
        num -= 1


t = Timer()
t.time(three_digit_products, 10000000)

