from timer import Timer
from euler import read_input
import string




def find_answer():
    input_data = read_input()
    
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

            

t = Timer()
t.time(find_answer)
