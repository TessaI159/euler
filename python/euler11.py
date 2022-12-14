# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

# Grid in data/euler11_input.txt

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

from decorator import time_and_memory_decorator as tamd
from euler import read_input, transpose, mult
import inspect


filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'
MAGIC_NUM = 4

def vertical(x, y, data):
    m = []
    if y + MAGIC_NUM < len(data[x]):
        for j in range(MAGIC_NUM):
            m.append(data[x][y + j])
    return mult(m)

def horizontal(x, y, data):
    m = []
    if x + MAGIC_NUM < len(data):
        for j in range(MAGIC_NUM):
            m.append(data[x + j][y])
    return mult(m)

def down_right(x, y, data):
    m = []
    if x + MAGIC_NUM < len(data) and y + MAGIC_NUM < len(data[x]):
        for j in range(MAGIC_NUM):
            m.append(data[x + j][y + j])
    return mult(m)

def down_left(x, y, data):
    m = []
    if x - MAGIC_NUM < len(data) and y + MAGIC_NUM < len(data[x]):
        for j in range(MAGIC_NUM):
            m.append(data[x - j][y + j])
    return mult(m)

@tamd
def find_answer():
    input_data = transpose(list(map(lambda x : x.split(' '), read_input(filename))))
    
    answer = 0
    for yi, y in enumerate(input_data):
        for xi, x in enumerate(input_data[yi]):
            vert = vertical(xi, yi, input_data)
            horiz = horizontal(xi, yi, input_data)
            dl = down_left(xi, yi, input_data)
            dr = down_right(xi, yi, input_data)
            if max([vert, horiz, dl, dr]) > answer:
                answer = max([vert, horiz, dl, dr])
    return answer
            


if __name__ == '__main__':
    print(filename, ": ", end="")
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
