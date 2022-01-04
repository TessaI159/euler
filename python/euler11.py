from timer import Timer
from euler import read_input, transpose, mult

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

def find_answer():
    input_data = transpose(list(map(lambda x : x.split(' '), read_input())))
    
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
            


t = Timer()
t.time(find_answer)
