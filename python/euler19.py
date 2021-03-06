# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from decorator import time_and_memory_decorator as tamd
from enum import Enum
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

week = 7

months = dict()
months['january'] = 31
months['february'] = 28
months['march'] = 31
months['april'] = 30
months['may'] = 31
months['june'] = 30
months['july'] = 31
months['august'] = 31
months['september'] = 30
months['october'] = 31
months['november'] = 30
months['december'] = 31

month_names = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']



class Day(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


@tamd
def find_answer():
    today = 365
    answer = 0
    for x in range(1901, 2001):
        if x % 4 == 0:
            months['february'] = 29
        else:
            months['february'] = 28
    
        for month in month_names:
            if today % week == Day.SUNDAY.value:
                answer += 1

            today += months[month]
            
    return answer

if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
