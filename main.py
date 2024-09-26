OUT = 0
VOID = 1
FULL = 2

Move = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]


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


def main():
    grid = get_grid()
    print(grid)
    show_grid(grid)
    for move in get_moves(grid):
        print(move)
        make_move(grid, move)
        show_grid(grid)
        cancel_move(grid, move)


if __name__ == "__main__":
    main()
