from random import randint

from tile import Tile
from variables import EMPTY_IMAGE, MINE_VALUE, MINE_IMAGE, IMAGE_VALUES


class Board:
    grid: list
    mineCount: int
    flagCount: int
    revealCount: int

    def __init__(self, gridSize: tuple, mineCount: int):
        self.mineCount = mineCount
        self.flagCount = 0
        self.revealCount = 0
        self.grid = initialize_grid(gridSize, mineCount)

    def remove_tile(self, row: int, column: int):
        self.revealCount += self.grid[row][column].remove()
        return self.grid[row][column].value == MINE_VALUE

    def flag_tile(self, row: int, column: int):
        self.flagCount = self.grid[row][column].flag(self.flagCount, self.mineCount)


def update_surrounding_squares(grid: list, row: int, column: int):
    # Check the row above
    if 0 <= row - 1:
        # Check the left column
        if 0 <= column - 1 and grid[row - 1][column - 1].value != MINE_VALUE:
            grid[row - 1][column - 1].value += 1
            grid[row - 1][column - 1].hiddenImage = IMAGE_VALUES[grid[row - 1][column - 1].value]

        # Check the same column
        if grid[row - 1][column].value != MINE_VALUE:
            grid[row - 1][column].value += 1
            grid[row - 1][column].hiddenImage = IMAGE_VALUES[grid[row - 1][column].value]

        # Check the right column
        if column + 1 < len(grid[0]) and grid[row - 1][column + 1].value != MINE_VALUE:
            grid[row - 1][column + 1].value += 1
            grid[row - 1][column + 1].hiddenImage = IMAGE_VALUES[grid[row - 1][column + 1].value]

    # Check the same row
    if 0 <= column - 1 and grid[row][column - 1].value != MINE_VALUE:
        grid[row][column - 1].value += 1
        grid[row][column - 1].hiddenImage = IMAGE_VALUES[grid[row][column - 1].value]
    if column + 1 < len(grid[0]) and grid[row][column + 1].value != MINE_VALUE:
        grid[row][column + 1].value += 1
        grid[row][column + 1].hiddenImage = IMAGE_VALUES[grid[row][column + 1].value]

    # Check the row below
    if row + 1 < len(grid):
        # Check the left column
        if 0 <= column - 1 and grid[row + 1][column - 1].value != MINE_VALUE:
            grid[row + 1][column - 1].value += 1
            grid[row + 1][column - 1].hiddenImage = IMAGE_VALUES[grid[row + 1][column - 1].value]

        # Check the same column
        if grid[row + 1][column].value != MINE_VALUE:
            grid[row + 1][column].value += 1
            grid[row + 1][column].hiddenImage = IMAGE_VALUES[grid[row + 1][column].value]

        # Check the right column
        if column + 1 < len(grid[0]) and grid[row + 1][column + 1].value != MINE_VALUE:
            grid[row + 1][column + 1].value += 1
            grid[row + 1][column + 1].hiddenImage = IMAGE_VALUES[grid[row + 1][column + 1].value]


def update_grid(grid: list, mineLocations: list):
    for location in mineLocations:
        update_surrounding_squares(grid, location[0], location[1])


def generate_random_numbers(grid: list, mineCount: int, randomRow=None, randomCol=None, mineLocations=None):
    if mineCount == 0:
        return mineLocations

    if randomRow is None:
        randomRow = randint(0, len(grid) - 1)
        randomCol = randint(0, len(grid[0]) - 1)
        mineLocations = list()

    for i in mineLocations:
        if i[0] == randomRow and i[1] == randomCol:
            return generate_random_numbers(grid, mineCount, randint(0, len(grid) - 1),
                                           randint(0, len(grid[0]) - 1), mineLocations)

    grid[randomRow][randomCol].value = MINE_VALUE
    grid[randomRow][randomCol].hiddenImage = MINE_IMAGE

    mineLocations.append((randomRow, randomCol))

    return generate_random_numbers(grid, mineCount - 1, randint(0, len(grid) - 1),
                                   randint(0, len(grid[0]) - 1), mineLocations)


def initialize_grid(gridSize: tuple, mineCount: int):
    grid = list()

    # Set up the initial grid
    for row in range(gridSize[0]):
        temp = list()
        for col in range(gridSize[1]):
            temp.append(Tile(0, EMPTY_IMAGE))

        grid.append(temp)

    # Generate mines
    mineLocations = generate_random_numbers(grid, mineCount)

    update_grid(grid, mineLocations)

    return grid
