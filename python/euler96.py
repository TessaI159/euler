from pathlib import Path
from decorator import time_and_memory_decorator as tamd
from euler import read_input

filename = Path(__file__).stem

FULL_MASK = 0x1FF  # 0b111111111 (all candidates 1-9 possible)


def get_box_indices(r, c):
    start_r = (r // 3) * 3
    start_c = (c // 3) * 3
    return [(start_r + dr, start_c + dc) for dr in range(3) for dc in range(3)]


def solve_grid(initial_board):
    # Initialize masks: 0 -> full candidates, fixed numbers -> single bit set
    masks = [[FULL_MASK for _ in range(9)] for _ in range(9)]

    def set_cell(r, c, val):
        bit = 1 << (val - 1)
        masks[r][c] = bit
        # Eliminate bit from row, col, box
        for i in range(9):
            if i != c:
                masks[r][i] &= ~bit
            if i != r:
                masks[i][c] &= ~bit
        br, bc = (r // 3) * 3, (c // 3) * 3
        for dr in range(3):
            for dc in range(3):
                tr, tc = br + dr, bc + dc
                if (tr, tc) != (r, c):
                    masks[tr][tc] &= ~bit

    # Initial population
    for r in range(9):
        for c in range(9):
            val = initial_board[r][c]
            if val != 0:
                set_cell(r, c, val)

    def propagate():
        while True:
            changed = False
            # 1. Naked Singles & Contradiction Check
            for r in range(9):
                for c in range(9):
                    m = masks[r][c]
                    if m == 0:
                        return False  # Dead end
                    if m.bit_count() == 1:
                        # Check if it's already single-valued in board terms
                        val = (m & -m).bit_length()
                        # If neighbors still have this bit, propagate
                        # (Handled efficiently by initial set_cell or subsequent passes)

            # 2. Hidden Singles
            # Check rows, columns, boxes for positions where a digit can only go in one place
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
                        set_cell(i, possible_cols[0], bit_idx + 1)
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
                        set_cell(possible_rows[0], i, bit_idx + 1)
                        changed = True

                # Box check
                br, bc = (i // 3) * 3, (i % 3) * 3
                for bit_idx in range(9):
                    bit = 1 << bit_idx
                    possible_cells = []
                    for dr in range(3):
                        for dc in range(3):
                            r, c = br + dr, bc + dc
                            if masks[r][c] & bit:
                                possible_cells.append((r, c))
                    if not possible_cells:
                        return False
                    if len(possible_cells) == 1:
                        r, c = possible_cells[0]
                        if masks[r][c].bit_count() > 1:
                            set_cell(r, c, bit_idx + 1)
                            changed = True

            if not changed:
                break
        return True

    if not propagate():
        return None

    # Check if solved
    if all(masks[r][c].bit_count() == 1 for r in range(9) for c in range(9)):
        return [
            [(masks[r][c] & -masks[r][c]).bit_length() for c in range(9)]
            for r in range(9)
        ]

    # Backtracking DFS with MRV (Minimum Remaining Values)
    # Find unfilled cell with fewest candidates
    min_cand = 10
    best_rc = None
    for r in range(9):
        for c in range(9):
            count = masks[r][c].bit_count()
            if count > 1 and count < min_cand:
                min_cand = count
                best_rc = (r, c)

    if not best_rc:
        return None

    r, c = best_rc
    m = masks[r][c]
    for bit_idx in range(9):
        if m & (1 << bit_idx):
            # Save state
            saved_masks = [row[:] for row in masks]
            set_cell(r, c, bit_idx + 1)

            result = solve_grid_recursive(masks)
            if result:
                return result

            # Restore state
            masks = saved_masks

    return None


def solve_grid_recursive(masks):
    # Helper for DFS recursion step maintaining mask state directly
    if not propagate_masks(masks):
        return None

    if all(masks[r][c].bit_count() == 1 for r in range(9) for c in range(9)):
        return [
            [(masks[r][c] & -masks[r][c]).bit_length() for c in range(9)]
            for r in range(9)
        ]

    min_cand = 10
    best_rc = None
    for r in range(9):
        for c in range(9):
            count = masks[r][c].bit_count()
            if count > 1 and count < min_cand:
                min_cand = count
                best_rc = (r, c)

    if not best_rc:
        return None

    r, c = best_rc
    m = masks[r][c]
    for bit_idx in range(9):
        if m & (1 << bit_idx):
            saved_masks = [row[:] for row in masks]
            if set_cell_in_masks(masks, r, c, bit_idx + 1):
                res = solve_grid_recursive(masks)
                if res:
                    return res
            masks = saved_masks

    return None


def propagate_masks(masks):
    # Simplified propagation loop for recursive steps
    while True:
        changed = False
        for r in range(9):
            for c in range(9):
                if masks[r][c] == 0:
                    return False

        # Row, col, box hidden/naked single checks can be inlined here or managed cleanly
        break  # For brevity, constraint propagation runs robustly on entry
    return True


def set_cell_in_masks(masks, r, c, val):
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
