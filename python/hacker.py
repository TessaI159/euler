# Insert question description here

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'



@tamd
def find_answer():
    year = 2100
    programmer_day = 256
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year < 1918:
        if year % 4 == 0:
            month_lengths[1] = 29
        else:
            month_lengths[1] = 28
    else:
        if year % 400 == 0:
            month_lengths[1] = 29
        elif year % 4 == 0 and year % 100 != 0:
            month_lengths[1] = 29
        else:
            month_lengths[1] = 28

    current_month = 0
    if year == 1918:
        current_month = 2
        programmer_day -= 46
        for i, month in enumerate(month_lengths):
            if i < 2:
                continue
            if programmer_day > month:
                programmer_day -= month
            else:
                if programmer_day > 9 and current_month > 9:
                    return f'{programmer_day}.{current_month + 1}.{year}'
                elif programmer_day <= 9 and current_month <= 9:
                    return f'0{programmer_day}.0{current_month + 1}.{year}'
                elif programmer_day <= 9:
                    return f'0{programmer_day}.{current_month + 1}.{year}'
                elif current_month <= 9:
                    return f'{programmer_day}.0{current_month + 1}.{year}'
            current_month += 1
        
        
    for month in month_lengths:
        if programmer_day > month:
            programmer_day -= month
        else:
            if programmer_day > 9 and current_month > 9:
                return f'{programmer_day}.{current_month + 1}.{year}'
            elif programmer_day <= 9 and current_month <= 9:
                return f'0{programmer_day}.0{current_month + 1}.{year}'
            elif programmer_day <= 9:
                return f'0{programmer_day}.{current_month + 1}.{year}'
            elif current_month <= 9:
                return f'{programmer_day}.0{current_month + 1}.{year}'
                
        current_month += 1
        
    
if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
