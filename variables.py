from enum import Enum

BOMB = -1


class TileType(Enum):
    EMPTY = 0
    FILLED = 1
    FLAGGED = 2
