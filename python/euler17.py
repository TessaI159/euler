# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

from euler import ones_place, tens_place, hundreds_place, teens
from decorator import time_and_memory_decorator as tamd
import inspect


filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'


@tamd
def find_answer(*args, **kwargs):
    letters = 0
    for x in range(1,1001):
        add = ''
        if x < 10:
            add += ones_place[x]
            
            
        elif x in range(10,20):
            add += teens[int(str(x)[-1])]
            
            
        elif x in range(20,100):
            add += tens_place[int(str(x)[0])]
            add += ones_place[int(str(x)[1])]
            

        elif x in range(100,1000):
            add += hundreds_place[int(str(x)[0])]


            if x % 100 != 0:
                add += 'and'
                
            if str(x)[1] == '1':
                add += teens[int(str(x)[-1])]

            else:
                add += tens_place[int(str(x)[1])]
                add += ones_place[int(str(x)[-1])]
                

                
        letters += len(add)
    letters += len('onethousand')

                
            
    return letters
        


if __name__ == '__main__':
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
