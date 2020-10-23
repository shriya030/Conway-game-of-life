import random
import itertools
ALL_NEIGHBOURS = [
    neighbour for neighbour in itertools.product([-1, 0, 1], repeat=2) if not neighbour == (0, 0)]
BLACK = 'B'


def add_blacks_around(grid):
    width = len(grid[0])
    new_grid = [BLACK+row+BLACK for row in grid]
    new_grid.append((width+2)*BLACK)
    new_grid.insert(0, (width+2)*BLACK)
    return new_grid


def create_grid(rows, columns):
    return add_blacks_around([''.join(str(random.randint(0, 1)) for column in range(columns)) for row in range(rows)])


def update_grid(grid, rows, columns):
    def count_living_neighbours(row, column):
        return len([1 for row_neighbour, column_neighbour in ALL_NEIGHBOURS if grid[row + row_neighbour][column + column_neighbour] == '1'])

    new_grid = grid.copy()

    for row in range(1, rows+1):
        for column in range(1, columns+1):
            living_neighbours = count_living_neighbours(row, column)
            if living_neighbours in (2, 3):
                if living_neighbours == 3 and grid[row][column] == '0':
                    new_grid[row] = new_grid[row][:column] + \
                        '1'+new_grid[row][column+1:]
            else:
                new_grid[row] = new_grid[row][:column] + \
                    '0'+new_grid[row][column+1:]
    return new_grid


def main_game(rows, columns, CYCLES=5):
    grid = create_grid(rows, columns)
    for cycle in range(CYCLES):
        grid = update_grid(grid, rows, columns)
    return grid


if __name__ == "__main__":
    print(main_game(3, 2))