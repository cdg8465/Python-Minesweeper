import pygame

from variables import TileType, FILLED_IMAGE, FLAG_IMAGE


class Tile:
    value: int
    type: TileType
    topImage: pygame.Surface
    hiddenImage: pygame.Surface

    def __init__(self, value: int, hiddenImage: pygame.Surface):
        self.value = value
        self.type = TileType.FILLED
        self.topImage = FILLED_IMAGE
        self.hiddenImage = hiddenImage

    def remove(self):
        if self.type != TileType.FLAGGED:
            self.type = TileType.REVEALED

    def flag(self, count: int, cap: int):
        if self.type != TileType.FLAGGED and count < cap:
            self.type = TileType.FLAGGED
            self.topImage = FLAG_IMAGE
            return count + 1
        elif self.type == TileType.FLAGGED:
            self.type = TileType.FILLED
            self.topImage = FILLED_IMAGE
            return count - 1

        return count
