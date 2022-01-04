from timer import Timer
from euler import read_input

def find_answer():
    input_data = read_input()
    input_data.reverse()
    input_data = [x.split(' ') for x in input_data]

    for index_r, row in enumerate(input_data):
        for index_n, num in enumerate(row):
            if index_n == len(row) - 1:
                pass
            else:
                input_data[index_r + 1][index_n] = \
                max(int(input_data[index_r][index_n]), int(input_data[index_r][index_n + 1])) + \
                int(input_data[index_r + 1][index_n])
    return input_data[-1][-1]


t = Timer()
t.time(find_answer)
