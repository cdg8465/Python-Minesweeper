from random import randint

from tile import Tile
from variables import EMPTY_IMAGE, MINE_VALUE, MINE_IMAGE

IMAGE_VALUES = {
    MINE_VALUE: MINE_IMAGE,
    0: EMPTY_IMAGE,
    1: EMPTY_IMAGE,
    2: EMPTY_IMAGE,
    3: EMPTY_IMAGE,
    4: EMPTY_IMAGE,
    5: EMPTY_IMAGE,
    6: EMPTY_IMAGE,
    7: EMPTY_IMAGE,
    8: EMPTY_IMAGE,
}


class Board:
    grid: list
    mineCount: int
    flagCount: int

    def __init__(self, gridSize: tuple, mineCount: int):
        self.mineCount = mineCount
        self.flagCount = 0
        self.grid = initialize_grid(gridSize, mineCount)

    def remove_tile(self, row: int, column: int):
        self.grid[row][column].remove()

    def flag_tile(self, row: int, column: int):
        self.flagCount = self.grid[row][column].flag(self.flagCount, self.mineCount)


def initialize_grid(gridSize: tuple, mineCount: int):
    grid = list()

    # Set up the initial grid
    for row in range(gridSize[1]):
        temp = list()
        for col in range(gridSize[0]):
            temp.append(Tile(0, EMPTY_IMAGE))

        grid.append(temp)

    # Generate mines
    for i in range(mineCount):
        randomRow = randint(0, len(grid) - 1)
        randomCol = randint(0, len(grid[0]) - 1)

        grid[randomRow][randomCol].value = MINE_VALUE
        grid[randomRow][randomCol].hiddenImage = MINE_IMAGE

    return grid
