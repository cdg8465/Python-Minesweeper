import pygame

from board import Board
from variables import Difficulty, TileType

# Constants
TITLE = "Python Minesweeper"  # Title of the window

SQUARE_SIZE = 40  # Size of each grid square

BACKGROUND_COLOR = (255, 255, 255)  # White

# Difficulty-Specific Constants
GRID_SIZE = {
    Difficulty.EASY: (8, 8),
    Difficulty.INTERMEDIATE: (16, 16),
    Difficulty.HARD: (16, 30)
}

MINE_COUNT = {
    Difficulty.EASY: 10,
    Difficulty.INTERMEDIATE: 40,
    Difficulty.HARD: 99
}


class MinesweeperGame:
    board: Board
    difficulty: Difficulty
    window: pygame.Surface

    def __init__(self, difficulty: Difficulty):
        pygame.init()

        SCREEN_SIZE = (SQUARE_SIZE * GRID_SIZE[difficulty][0], SQUARE_SIZE * GRID_SIZE[difficulty][1])

        self.window = pygame.display.set_mode(SCREEN_SIZE)

        self.board = Board(GRID_SIZE[difficulty], MINE_COUNT[difficulty])
        self.difficulty = difficulty

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= event.pos[0] < SQUARE_SIZE * GRID_SIZE[self.difficulty][0] \
                    and 0 <= event.pos[1] < SQUARE_SIZE * GRID_SIZE[self.difficulty][1]:
                if event.button == pygame.BUTTON_LEFT:
                    column = event.pos[1] // SQUARE_SIZE
                    row = event.pos[0] // SQUARE_SIZE
                    self.board.remove_tile(row, column)
                elif event.button == pygame.BUTTON_RIGHT:
                    column = event.pos[1] // SQUARE_SIZE
                    row = event.pos[0] // SQUARE_SIZE
                    self.board.flag_tile(row, column)

    def render_grid(self):
        for row in range(len(self.board.grid)):
            for col in range(len(self.board.grid[0])):
                if self.board.grid[row][col].type == TileType.REVEALED:
                    self.window.blit(self.board.grid[row][col].hiddenImage,
                                     pygame.Rect(row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    self.window.blit(self.board.grid[row][col].topImage,
                                     pygame.Rect(row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def main():
    game = MinesweeperGame(Difficulty.INTERMEDIATE)

    pygame.display.set_caption(TITLE)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            game.handle_event(event)
        game.render_grid()

        pygame.display.update()


if __name__ == "__main__":
    main()
