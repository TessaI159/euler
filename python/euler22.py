# Using data/euler22_input.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

from decorator import time_and_memory_decorator as tamd
from euler import read_input
import string
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    input_data = read_input(filename)
    
    input_data = input_data[0]
    input_data = input_data.split(',')
    input_data = [x.replace('"', '') for x in input_data]
    input_data.sort()

    alphabet = list(string.ascii_lowercase)

    total_score = 0
    for n_index, name in enumerate(input_data):
        name_score = 0
        for c in name:
            name_score += alphabet.index(c.lower()) + 1
        total_score += name_score * (n_index + 1)
        
    return total_score

            

if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
