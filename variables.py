import os
import pygame
from enum import Enum


class TileType(Enum):
    REVEALED = 0
    FILLED = 1
    FLAGGED = 2


class Difficulty(Enum):
    EASY = 0
    INTERMEDIATE = 1
    HARD = 2


# # Basics
TITLE = "Python Minesweeper"  # Title of the window

SQUARE_SIZE = 40  # Size of each grid square

BACKGROUND_COLOR = (255, 255, 255)  # White

# # Hidden Mine Value
MINE_VALUE = -1

# # Images
# Revealed Images
EMPTY_IMAGE = pygame.image.load(os.path.join("resources", "empty.png"))
ONE_IMAGE = pygame.image.load(os.path.join("resources", "one.png"))
TWO_IMAGE = pygame.image.load(os.path.join("resources", "two.png"))
THREE_IMAGE = pygame.image.load(os.path.join("resources", "three.png"))
FOUR_IMAGE = pygame.image.load(os.path.join("resources", "four.png"))
FIVE_IMAGE = pygame.image.load(os.path.join("resources", "five.png"))
SIX_IMAGE = pygame.image.load(os.path.join("resources", "six.png"))
SEVEN_IMAGE = pygame.image.load(os.path.join("resources", "seven.png"))
EIGHT_IMAGE = pygame.image.load(os.path.join("resources", "eight.png"))
MINE_IMAGE = pygame.image.load(os.path.join("resources", "mine.png"))

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

IMAGE_VALUES = {
    MINE_VALUE: MINE_IMAGE,
    0: EMPTY_IMAGE,
    1: ONE_IMAGE,
    2: TWO_IMAGE,
    3: THREE_IMAGE,
    4: FOUR_IMAGE,
    5: FIVE_IMAGE,
    6: SIX_IMAGE,
    7: SEVEN_IMAGE,
    8: EIGHT_IMAGE,
}

# Unrevealed Images
FLAG_IMAGE = pygame.image.load(os.path.join("resources", "flag.png"))
FILLED_IMAGE = pygame.image.load(os.path.join("resources", "tile.png"))
