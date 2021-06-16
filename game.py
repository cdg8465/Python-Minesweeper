import pygame
from board import Board
from variables import TileType

TITLE = "Python Minesweeper"        # Title of the window
SCREEN_SIZE = (1280, 720)           # Width, Height
GRID_SIZE = (10, 10)                # Columns, Rows
SQUARE_SIZE = 40                    # Size of each grid square
BACKGROUND_COLOR = (255, 255, 255)  # White
TILES = {
    TileType.EMPTY: BACKGROUND_COLOR,
    TileType.FILLED: (0, 255, 0),
    TileType.FLAGGED: (255, 0, 0),
}

board = Board(GRID_SIZE)


def handle_event(event: pygame.event.Event):
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if 0 <= event.pos[0] < SQUARE_SIZE * GRID_SIZE[0] and 0 <= event.pos[1] < SQUARE_SIZE * GRID_SIZE[1]:
            if event.button == pygame.BUTTON_LEFT:
                column = event.pos[1] // SQUARE_SIZE
                row = event.pos[0] // SQUARE_SIZE
                board.remove_tile(row, column)
            elif event.button == pygame.BUTTON_RIGHT:
                column = event.pos[1] // SQUARE_SIZE
                row = event.pos[0] // SQUARE_SIZE
                board.flag_tile(row, column)


def render_grid(window: pygame.surface.Surface):
    for row in range(len(board.grid)):
        for col in range(len(board.grid)):
            window.fill(TILES[board.grid[row][col].type],
                        pygame.rect.Rect(row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def main():
    pygame.init()
    window = pygame.display.set_mode(SCREEN_SIZE)
    window.fill(BACKGROUND_COLOR)

    pygame.display.set_caption(TITLE)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            handle_event(event)
        pygame.display.update()
        
        render_grid(window)


if __name__ == "__main__":
    main()
