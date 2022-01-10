from decorator import time_and_memory_decorator as tamd
from euler import is_palindrome

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
    print('euler4')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)

