from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def repitition(num):
    if len(num) == 1:
        return 0
    for i in range(-1, (len(num) * -1) - 1, -1):
        if num[i:] == num[2 * i:i]:
            return num[i:]
    return 0

def long_division_unit_fraction(b, a=1):
    decimals = ''
    presumed_pattern = ''
    loops = 0
    while a != 0:
        a *= 10
        next_digit = str(a // b)
        decimals += next_digit
        if len(decimals) >= 10000:
            if (ret := repitition(decimals)) != 0:
                return ret
        a = a - (b * (a // b))
    return decimals

@tamd
def find_answer():
    ans, longest = 0, 0
    for d in range(2, 1000):
        if (temp := len(long_division_unit_fraction(d))) > longest:
            longest = temp
            ans = d
    return ans



if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
