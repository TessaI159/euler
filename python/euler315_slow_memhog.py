from decorator import time_and_memory_decorator as tamd
from euler import is_prime, read_input
import inspect

# These are represented as 1 == on, 0 == off
# Each number cooresponds with the following lines, in order
# Top mid, top left, top right, mid mid, bottom left, bottom right, bottom mid

numbers = \
    {
        1 : "0010010",
        2 : "1011101",
        3 : "1011011",
        4 : "0111010",
        5 : "1101011",
        6 : "1101111",
        7 : "1110010",
        8 : "1111111",
        9 : "1111011",
        0 : "1110111"
    }

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def string_and(string1, string2):
    """
    Takes two strings of arbitrary length and returns a single string the same length as the longer string
    """
    
    string1 = str(string1)
    string2 = str(string2)
    
    if len(string1) > len(string2):
        length_diff = len(string1) - len(string2)
        string2 = list(string2)
        string2.reverse()
        string2.extend(['0' for _ in range(length_diff)])
        string2.reverse()
        string2 = ''.join(string2)
    elif len(string2) > len(string1):
        length_diff = len(string2) - len(string1)
        string1 = list(string1)
        string1.reverse()
        string1.extend(['0' for _ in range(length_diff)])
        string1.reverse()
        string1 = ''.join(string1)
    else:
        length_diff = None

    new_string = []
    for a, b in zip(string1, string2):
        if a == '1' and b == '1':
            new_string.append('1')
        else:
            new_string.append('0')
    return ''.join(new_string)
    

def digital_sum(n):
    n = str(n)
    if len(n) == 1:
        return 0
    ans = 0
    for c in n:
        ans += int(c)
    return ans


def segments(n):
    count = 0
    s = str(n)
    for c in s:
        count += count_segments(c)
    return count


def count_segments(n):
    return list(numbers[int(n)]).count('1')

def count_segments_str(n):
    return sum([1 for c in n if c == '1'])
        


# a is the number we will display, b is the last number we displayed
def change(a, b=None):
    a_str = ''
    b_str = ''
    
    if b:
        for i in str(a):
            a_str += numbers[int(i)]
        for i in str(b):
            b_str += numbers[int(i)]
        
    else:
        for i in str(a):
            a_str += numbers[int(i)]

    return count_segments_str(a_str) - count_segments_str(string_and(a_str, b_str))
            
class Clock:
    def __init__(self, efficient):
        self.efficient = efficient

    def toggle(self, n):
        if self.efficient:
            return self.efficient_toggle(n)
        else:
            return self.inefficient_toggle(n)

            
    def inefficient_toggle(self, num):
        toggles = 0
        
        while num != 0:
            toggles += segments(num)
            num = digital_sum(num)
        
        return toggles * 2

    
    def efficient_toggle(self, num):
        toggles = 0
        numbers_to_display = []

        while num != 0:
            numbers_to_display.append(num)
            num = digital_sum(num)

        for i, n in enumerate(numbers_to_display):
            if i == 0:
                toggles += change(n)
            else:
                toggles += change(n, numbers_to_display[i - 1])

            if i == len(numbers_to_display) - 1:
                toggles += change(n)
            else:
                toggles += change(n, numbers_to_display[i + 1])
        return toggles

    
@tamd            
def find_answer():
    input_data = read_input(filename)
    
    inefficient_clock = Clock(False)
    efficient_clock = Clock(True)

    total = 0

    for prime in input_data:
        total += inefficient_clock.toggle(prime) - efficient_clock.toggle(prime)

    return total
    
    


if __name__ == '__main__':
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
