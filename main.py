OUT = 0
VOID = 1
FULL = 2

Move = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]

loosing_hash_table = {}
winning_hash_table = {}
global_counter = 0


def get_hash(grid: list[list[int]]) -> int:
    hash = 0
    for y in range(7):
        for x in range(7):
            i = y * 7 + x
            if grid[y][x] == FULL:
                hash |= 1 << i

    return hash


# english version
def get_grid() -> list[list[int]]:
    grid = []
    for y in range(7):
        if y in [0, 1, 5, 6]:
            row = [FULL if i in [2, 3, 4] else OUT for i in range(7)]
        else:
            row = [FULL for _ in range(7)]
        grid.append(row)
    grid[3][3] = VOID
    return grid


def show_grid(grid: list[list[int]]) -> None:
    for y in range(7):
        str_row = ""
        for x in range(7):
            if grid[y][x] == OUT:
                str_row += " "
            if grid[y][x] == VOID:
                str_row += "o"
            if grid[y][x] == FULL:
                str_row += "#"
        print(str_row)


def get_square_moves(grid: list[list[int]], x: int, y: int) -> list[Move]:
    if grid[y][x] != FULL:
        return []
    moves = []
    # up
    if y > 1 and grid[y - 1][x] == FULL and grid[y - 2][x] == VOID:
        moves.append(((x, y), (x, y - 1), (x, y - 2)))
    # down
    if y < 5 and grid[y + 1][x] == FULL and grid[y + 2][x] == VOID:
        moves.append(((x, y), (x, y + 1), (x, y + 2)))
    # left
    if x > 1 and grid[y][x - 1] == FULL and grid[y][x - 2] == VOID:
        moves.append(((x, y), (x - 1, y), (x - 2, y)))
    # right
    if x < len(grid[y]) - 3 and grid[y][x + 1] == FULL and grid[y][x + 2] == VOID:
        moves.append(((x, y), (x + 1, y), (x + 2, y)))
    return moves


def get_moves(grid: list[list[int]]) -> list[Move]:
    moves = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            moves.extend(get_square_moves(grid, x, y))
    return moves


def is_won(grid: list[list[int]]) -> bool:
    for y in range(7):
        for x in range(7):
            if grid[y][x] == FULL and not (y == 3 and x == 3):
                return False
    return True


def make_move(grid: list[list[int]], move: Move) -> list[list[int]]:
    for i in range(3):
        x = move[i][0]
        y = move[i][1]
        grid[y][x] = FULL if i == 2 else VOID
    return grid


def cancel_move(grid: list[list[int]], move: Move) -> list[list[int]]:
    for i in range(3):
        x = move[i][0]
        y = move[i][1]
        grid[y][x] = FULL if i != 2 else VOID
    return grid


def solve(grid: list[list[int]], moves: list[Move]) -> int:
    global global_counter
    if loosing_hash_table.get(get_hash(grid)):
        return 0
    if is_won(grid):
        global_counter += 1
        print(f"-- new solution {global_counter} --")
        return 1
    if winning_hash_table.get(get_hash(grid)):
        global_counter += winning_hash_table[get_hash(grid)]
        print(f"-- new solution {global_counter} --")
        return winning_hash_table[get_hash(grid)]

    nb_result = 0
    for move in get_moves(grid):
        make_move(grid, move)
        moves.append(move)

        result = solve(grid, moves)
        if result:
            nb_result += result

        moves.pop()
        cancel_move(grid, move)

    if not nb_result:
        loosing_hash_table[get_hash(grid)] = True
    else:
        winning_hash_table[get_hash(grid)] = nb_result
    return nb_result


def main():
    grid = get_grid()
    result = solve(grid, [])
    show_grid(grid)
    print(result)


if __name__ == "__main__":
    main()
