# Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
# Its origin is thought to lie in the game of Latin Squares, first invented by Euler!
# The objective of Su Doku puzzles is to replace the blanks (or zeros) in a 9x9 grid with
# the numbers 1 to 9 so that each row, column, and 3x3 box contains each of the numbers 1 to 9.
#
# The file data/euler96_input.txt contains fifty different Su Doku puzzles ranging in
# difficulty, but all with unique solutions.
#
# By solving all fifty puzzles, find the sum of the 3-digit numbers found in the top left
# corner of each solution grid; for example, 483 is the 3-digit number found in the top
# left corner of the first solution grid (row 0, columns 0, 1, 2).

from decorator import time_and_memory_decorator as tamd
from euler import read_input
from pathlib import Path

filename = Path(__file__).stem

@tamd
def find_answer():
    raw_lines = read_input()
    # TODO: Parse 50 grids and solve each puzzle
    pass


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
