from timer import Timer
from enum import Enum

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

t = Timer()
t.time(find_answer)
    