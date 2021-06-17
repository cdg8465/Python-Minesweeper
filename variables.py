import os
import pygame
from enum import Enum

# # Images
# Revealed Images
EMPTY_IMAGE = pygame.image.load(os.path.join("resources", "empty.png"))
MINE_IMAGE = pygame.image.load(os.path.join("resources", "mine.png"))

# Unrevealed Images
FLAG_IMAGE = pygame.image.load(os.path.join("resources", "flag.png"))
FILLED_IMAGE = pygame.image.load(os.path.join("resources", "tile.png"))

# # Hidden Mine Value
MINE_VALUE = -1


class TileType(Enum):
    REVEALED = 0
    FILLED = 1
    FLAGGED = 2


class Difficulty(Enum):
    EASY = 0
    INTERMEDIATE = 1
    HARD = 2
