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
