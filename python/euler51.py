# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family:
# 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

from euler import is_prime
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

# The repeating digit must be a 0, 1, or 2
# The digit must be repeated 3 times
# The non-repeating digits must not have a digit sum % 3 == 0
# The repeating digit cannot replace the last digit of our prime

# pattern = list of True/False values
# unreplaced = list with -1 in place of other digits
# potential = list with -1 replaced by replacement_num
   

def check_if_family(potential, pattern, family_length=None):
    """Check if the potential number is part of a prime family of length family_length

    potential is the number generated by generate_potential, pattern is the list of True/False values
    representing whether to replace the num, replaced num is the digit which was used to replace.
    """
    if not family_length:
        family_length = 8
        
    if len(pattern) != len(str(potential)):
        print("Pattern must be the same length as potential")
        return False

    smallest_prime = 0
        
    counter = 0
    potential = list(str(potential))
    
    for new_replacement in range(0, 10):
        potential = [str(new_replacement) if p else potential[i] for i, p in enumerate(pattern)]
        
        if potential[0] == '0':
            continue

        potential = int(''.join(potential))
        if is_prime(potential):
            
            if smallest_prime > potential or smallest_prime == 0:
                smallest_prime = potential
                
            counter += 1
        potential = list(str(potential))
        available_potential = 10 - new_replacement
        needed_potential = family_length - counter
        
        if new_replacement >= 3 and available_potential < needed_potential:
            return False, 0

    if counter == family_length:
        return True, smallest_prime
    else:
        return False, 0


@tamd
def find_answer():
    with open('data/primes.txt') as fptr:
        primes = [int(p.strip()) for p in fptr if int(p.strip()) in range(10000, 1000000)]


    replace_5_patterns = [[True, True, True, False, False], [True, True, False, True, False], [True, False, True, True, False], [False, True, True, True, False]]
    
    # I know it's hideous. Shut up.
    replace_6_patterns = [[True, True, True, False, False, False], [True, True, False, True, False, False], [True, True, False, False, True, False], [True,  False, True, True, False, False], [True, False, True, False, True, False],[True, False, False, True, True, False], [False, False, True, True, True, False], [False, True, False, True, True, False], [False, True, True, False, True, False], [False, True, True, True, False, False]]

    
    for prime in primes:
        if len(str(prime)) == 5:
            for pattern in replace_5_patterns:
                family = check_if_family(prime, pattern)
                if family[0]:
                    return family[1]
        else:
            for pattern in replace_6_patterns:
                family = check_if_family(prime, pattern)
                if family[0]:
                    return family[1]
                    
    return f'Not found'
    
    
    

    


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
