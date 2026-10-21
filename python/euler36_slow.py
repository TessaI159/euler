# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

from euler import is_palindrome, to_binary
from decorator import time_and_memory_decorator as tamd
from pathlib import Path

filename = Path(__file__).stem

@tamd
def find_answer():
    sum_of_palindromes = 0

    for i in range(1, 10**6):
        if is_palindrome(i) and is_palindrome(to_binary(i)):
            sum_of_palindromes += i
    return sum_of_palindromes


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
