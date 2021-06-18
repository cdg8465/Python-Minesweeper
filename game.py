import pygame

from board import Board
from variables import Difficulty, TileType, GRID_SIZE, MINE_COUNT, SQUARE_SIZE, TITLE, STRING_DIFFICULTIES


class MinesweeperGame:
    board: Board
    difficulty: Difficulty
    window: pygame.Surface
    gameOver: bool
    tileSize: int

    def __init__(self, difficulty: Difficulty):
        pygame.init()

        self.tileSize = SQUARE_SIZE[difficulty]

        SCREEN_SIZE = (self.tileSize * GRID_SIZE[difficulty][0], self.tileSize * GRID_SIZE[difficulty][1])

        self.window = pygame.display.set_mode(SCREEN_SIZE)

        self.board = Board(GRID_SIZE[difficulty], MINE_COUNT[difficulty])
        self.difficulty = difficulty

        self.gameOver = False

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= event.pos[0] < self.tileSize * GRID_SIZE[self.difficulty][0] \
                    and 0 <= event.pos[1] < self.tileSize * GRID_SIZE[self.difficulty][1]:
                if event.button == pygame.BUTTON_LEFT:
                    column = event.pos[1] // self.tileSize
                    row = event.pos[0] // self.tileSize

                    self.gameOver = self.board.remove_tile(row, column) or \
                                    (self.board.revealCount == (GRID_SIZE[self.difficulty][0] *
                                                                GRID_SIZE[self.difficulty][1]) - self.board.mineCount
                                     and self.board.flagCount == self.board.mineCount)
                elif event.button == pygame.BUTTON_RIGHT:
                    column = event.pos[1] // self.tileSize
                    row = event.pos[0] // self.tileSize

                    self.board.flag_tile(row, column)

    def render_grid(self):
        for row in range(len(self.board.grid)):
            for col in range(len(self.board.grid[0])):
                if self.board.grid[row][col].type == TileType.REVEALED:
                    self.window.blit(pygame.transform.scale(self.board.grid[row][col].hiddenImage, (self.tileSize, self.tileSize)),
                                     pygame.Rect(row * self.tileSize, col * self.tileSize, self.tileSize, self.tileSize))
                else:
                    self.window.blit(pygame.transform.scale(self.board.grid[row][col].topImage, (self.tileSize, self.tileSize)),
                                     pygame.Rect(row * self.tileSize, col * self.tileSize, self.tileSize, self.tileSize))


def main():
    game = MinesweeperGame(STRING_DIFFICULTIES[input("Difficulty (EASY, INTERMEDIATE, HARD): ").upper()])

    pygame.display.set_caption(TITLE)
    pygame.display.flip()

    while not game.gameOver:
        for event in pygame.event.get():
            game.handle_event(event)
        game.render_grid()

        pygame.display.update()


if __name__ == "__main__":
    main()
