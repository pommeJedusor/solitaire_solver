# english version
def get_grid() -> list[list[bool]]:
    grid = []
    for y in range(7):
        row_length = 3 if y in [0, 1, 5, 6] else 7
        grid.append([True for _ in range(row_length)])
    grid[3][3] = False
    return grid


def show_grid(grid: list[list[bool]]) -> None:
    for y in range(7):
        is_short_row = True if y in [0, 1, 5, 6] else False
        row = ["#" if square else "o" for square in grid[y]]
        if is_short_row:
            print(f"  {''.join(row)}")
        else:
            print("".join(row))


def main():
    grid = get_grid()
    show_grid(grid)


if __name__ == "__main__":
    main()
