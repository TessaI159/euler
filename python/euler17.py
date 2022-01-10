from decorator import time_and_memory_decorator as tamd

ones_place = \
    {
        0 : '',
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine'
    }

tens_place = \
    {
        0 : '',
        1 : 'ten',
        2 : 'twenty',
        3 : 'thirty',
        4 : 'forty',
        5 : 'fifty',
        6 : 'sixty',
        7 : 'seventy',
        8 : 'eighty',
        9 : 'ninety'
    }

hundreds_place = \
    {
        0 : '',
        1 : 'onehundred',
        2 : 'twohundred',
        3 : 'threehundred',
        4 : 'fourhundred',
        5 : 'fivehundred',
        6 : 'sixhundred',
        7 : 'sevenhundred',
        8 : 'eighthundred',
        9 : 'ninehundred'
    }

teens = \
    {
        0 : 'ten',
        1 : 'eleven',
        2 : 'twelve',
        3 : 'thirteen',
        4 : 'fourteen',
        5 : 'fifteen',
        6 : 'sixteen',
        7 : 'seventeen',
        8 : 'eighteen',
        9 : 'nineteen'
    }



@tamd
def find_solution(*args, **kwargs):
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
    print(find_solution())
