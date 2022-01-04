from timer import Timer
import euler

input_data = euler.read_input()

def product(li):
    answer = 1
    for l in li:
        answer *= int(l)

def check_horizontal(size, x, y):
    answer = 1
    if x + size >= len(input_data[y]):
        return 0

    for mod in range(size):
        answer *= int(input_data[y][x + mod])

    return answer

def check_vertical(size, x, y):
    answer = 1
    if y + size >= len(input_data):
        return 0

    for mod in range(size):
        answer *= int(input_data[y + mod][x])
        
    return answer

def check_forward_diag(size, x, y):
    answer = 1
    if y - size < 0 or x + size >= len(input_data[0]):
        return 0

    for mod in range(size):
        answer *= int(input_data[y - mod][x + mod])
        
    return answer

def check_backward_diag(size, x, y):
    answer = 1
    if y - size < 0 or x - size < 0:
        return 0

    for mod in range(size):
        answer *= int(input_data[y - mod][x - mod])
        
    return answer

def largest_arg(*args):
    ret = 0
    for a in args:
        if a > ret:
            ret = a
    return ret

def func(size):
    largest = 0
    for y, row in enumerate(input_data):
        for x, column in enumerate(row):
            pass
            horizontal = check_horizontal(size, x, y)
            vertical = check_vertical(size, x, y)
            forward_diag = check_forward_diag(size, x, y)
            backward_diag = check_backward_diag(size, x, y)
        if largest_arg(horizontal, vertical, forward_diag, backward_diag) > largest:
            largest = largest_arg(horizontal, vertical, forward_diag, backward_diag)
    return largest
            

if __name__ == '__main__':
    t = Timer()
    t.time(func, 4)
