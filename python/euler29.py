# Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

# 2**2 = 4, 2**3 = 8, 2**4 = 16, 2**5 = 32
# 3**2 = 9, 3**3 = 27, 3**4 = 81, 3**5 = 243
# 4**2 = 16, 4**3 = 64, 4**4 = 256, 4**5 = 256
# 5**2 = 25, 5**3 = 125, 5**4 = 625, 5**5 = 3125

# If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

# How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer(a_l=2, a_u=100, b_l=2, b_u=100):
    numbers = []
    for a in range(a_l, a_u+1):
        for b in range(b_l, b_u+1):
            numbers.append(a**b)

    numbers = set(numbers)
    return len(numbers)
    
    


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)