# The nth term of the sequence of triangle numbers is given by, t(n) = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using data/euler42_input.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

from math import sqrt
from euler import read_input
from decorator import time_and_memory_decorator as tamd
import inspect

MAGIC_NUMBER = 96

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def triangular(n):
    return ((-1 + sqrt(1 + (8 * n))) / 2) % 1 == 0

@tamd
def find_answer():
    input_data = read_input(filename)
    input_data = input_data[0]
    total_triangles = 0
    
    for word in input_data.split(','):
        this_number = 0
        word = word.replace('"', '').lower()
        for letter in word:
            this_number += ord(letter) - MAGIC_NUMBER
        if triangular(this_number):
            total_triangles += 1
            
    return total_triangles
        
if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
