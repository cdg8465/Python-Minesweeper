from variables import TileType, BOMB


class Tile:
    value: int
    type: TileType

    def __init__(self, value):
        self.value = value
        self.type = TileType.FILLED

    def remove(self):
        if self.type == TileType.FLAGGED:
            return True

        self.type = TileType.EMPTY

        if self.value == BOMB:
            return False
        return True

    def flag(self):
        if self.type == TileType.FILLED:
            self.type = TileType.FLAGGED

        return self.value == BOMB
