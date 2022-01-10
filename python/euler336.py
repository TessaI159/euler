from timer import Timer
from string import ascii_lowercase
from itertools import permutations

memo = dict()
magic_number = 97

def rearrange(carriage):
    swaps = 0
    original_setup  = carriage
    carriage = list(carriage)
    chop_here = ''

    # Save the original pattern to memo once you are done
    # Start sorting the naive way
    # Once you reach a permutation that's in the memo, stop
    while carriage != list(ascii_lowercase[:len(carriage)]):
        for l in range(len(carriage)):
            print(carriage[l], ascii_lowercase[l])
            if carriage[l] != ascii_lowercase[l]:
                chop_here = ascii_lowercase[l]
                print(chop_here)
                input()
                

def find_answer(num_carriages):
    carriages = ascii_lowercase[:num_carriages]
    perms = [''.join(x) for x in permutations(carriages)]
    memo[perms[1]] = 1

    for carriage in perms:
        rearrange(carriage)
    
    


t = Timer()
t.time(find_answer, 4)

# 6 carriages
# 24 miximax
# 10th arrangement is DFAECB

# 4 carriages
# 2 miximax
# DACB, DBAC
# 5 rotations
