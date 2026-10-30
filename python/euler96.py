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

from pathlib import Path

from decorator import time_and_memory_decorator as tamd
from euler import read_input

filename = Path(__file__).stem

FULL_MASK = 0x1FF  # 0b111111111 (all candidates 1-9 possible)


def solve_grid(initial_board):
    masks = [[FULL_MASK for _ in range(9)] for _ in range(9)]

    def set_cell(masks, r, c, val):
        bit = 1 << (val - 1)
        if not (masks[r][c] & bit):
            return False
        masks[r][c] = bit
        for i in range(9):
            if i != c:
                masks[r][i] &= ~bit
                if masks[r][i] == 0:
                    return False
            if i != r:
                masks[i][c] &= ~bit
                if masks[i][c] == 0:
                    return False
        br, bc = (r // 3) * 3, (c // 3) * 3
        for dr in range(3):
            for dc in range(3):
                tr, tc = br + dr, bc + dc
                if (tr, tc) != (r, c):
                    masks[tr][tc] &= ~bit
                    if masks[tr][tc] == 0:
                        return False
        return True

    for r in range(9):
        for c in range(9):
            val = initial_board[r][c]
            if val != 0 and not set_cell(masks, r, c, val):
                return None

    def propagate(masks):
        while True:
            changed = False

            # 1. Naked Singles & Contradiction Check
            for r in range(9):
                for c in range(9):
                    m = masks[r][c]
                    if m == 0:
                        return False
                    if m.bit_count() == 1:
                        bit = m
                        for i in range(9):
                            if i != c and (masks[r][i] & bit):
                                masks[r][i] &= ~bit
                                if masks[r][i] == 0:
                                    return False
                                changed = True
                            if i != r and (masks[i][c] & bit):
                                masks[i][c] &= ~bit
                                if masks[i][c] == 0:
                                    return False
                                changed = True
                        br, bc = (r // 3) * 3, (c // 3) * 3
                        for dr in range(3):
                            for dc in range(3):
                                tr, tc = br + dr, bc + dc
                                if (tr, tc) != (r, c) and (masks[tr][tc] & bit):
                                    masks[tr][tc] &= ~bit
                                    if masks[tr][tc] == 0:
                                        return False
                                    changed = True

            # 2. Hidden Singles
            for i in range(9):
                # Row check
                for bit_idx in range(9):
                    bit = 1 << bit_idx
                    possible_cols = [c for c in range(9) if masks[i][c] & bit]
                    if not possible_cols:
                        return False
                    if (
                        len(possible_cols) == 1
                        and masks[i][possible_cols[0]].bit_count() > 1
                    ):
                        if not set_cell(masks, i, possible_cols[0], bit_idx + 1):
                            return False
                        changed = True

                # Column check
                for bit_idx in range(9):
                    bit = 1 << bit_idx
                    possible_rows = [r for r in range(9) if masks[r][i] & bit]
                    if not possible_rows:
                        return False
                    if (
                        len(possible_rows) == 1
                        and masks[possible_rows[0]][i].bit_count() > 1
                    ):
                        if not set_cell(masks, possible_rows[0], i, bit_idx + 1):
                            return False
                        changed = True

                # Box check
                br, bc = (i // 3) * 3, (i % 3) * 3
                for bit_idx in range(9):
                    bit = 1 << bit_idx
                    possible_cells = [
                        (br + dr, bc + dc)
                        for dr in range(3)
                        for dc in range(3)
                        if masks[br + dr][bc + dc] & bit
                    ]
                    if not possible_cells:
                        return False
                    if (
                        len(possible_cells) == 1
                        and masks[possible_cells[0][0]][
                            possible_cells[0][1]
                        ].bit_count()
                        > 1
                    ):
                        r, c = possible_cells[0]
                        if not set_cell(masks, r, c, bit_idx + 1):
                            return False
                        changed = True

            if not changed:
                break
        return True

    def search(masks):
        if not propagate(masks):
            return None

        if all(masks[r][c].bit_count() == 1 for r in range(9) for c in range(9)):
            return [
                [(masks[r][c] & -masks[r][c]).bit_length() for c in range(9)]
                for r in range(9)
            ]

        # Minimum Remaining Values (MRV)
        min_cand = 10
        best_rc = None
        for r in range(9):
            for c in range(9):
                count = masks[r][c].bit_count()
                if 1 < count < min_cand:
                    min_cand = count
                    best_rc = (r, c)
                    if min_cand == 2:
                        break
            if min_cand == 2:
                break

        r, c = best_rc
        m = masks[r][c]
        for bit_idx in range(9):
            if m & (1 << bit_idx):
                saved_masks = [row[:] for row in masks]
                if set_cell(saved_masks, r, c, bit_idx + 1):
                    res = search(saved_masks)
                    if res:
                        return res

        return None

    return search(masks)


@tamd
def find_answer():
    raw_lines = read_input()
    boards = []
    current_board = []

    for line in raw_lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("Grid"):
            if current_board:
                boards.append(current_board)
                current_board = []
        else:
            current_board.append([int(c) for c in line])
    if current_board:
        boards.append(current_board)

    total_sum = 0
    for board in boards:
        solved = solve_grid(board)
        if solved:
            top_left_3 = solved[0][0] * 100 + solved[0][1] * 10 + solved[0][2]
            total_sum += top_left_3

    return total_sum


if __name__ == "__main__":
    print(filename, ": ", end="")
    answer, mem, time = find_answer()
    print(answer)
    print(mem)
    print(time)
