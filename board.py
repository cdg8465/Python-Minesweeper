from tile import Tile


class Board:
    grid: list

    def __init__(self, gridSize: tuple):
        self.grid = initialize_grid(gridSize)

    def remove_tile(self, row: int, column: int):
        self.grid[row][column].remove()

    def flag_tile(self, row: int, column: int):
        self.grid[row][column].flag()


def initialize_grid(gridSize):
    grid = list()

    for row in range(gridSize[1]):
        temp = list()
        for col in range(gridSize[0]):
            temp.append(Tile(0))

        grid.append(temp)

    return grid
