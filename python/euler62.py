# <p>The cube, $41063625$ ($345^3$), can be permuted to produce two other cubes: $56623104$ ($384^3$) and $66430125$ ($405^3$). In fact, $41063625$ is the smallest cube which has exactly three permutations of its digits which are also cube.</p>
# <p>Find the smallest cube for which exactly five permutations of its digits are cube.</p>


from pathlib import Path

from decorator import time_and_memory_decorator as tamd

filename = Path(__file__).stem


@tamd
def find_answer():
    pass


if __name__ == "__main__":
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
