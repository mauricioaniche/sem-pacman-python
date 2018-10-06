from oop.pieces import build_piece, Empty


class Map:
    def __init__(self, map):
        self._map = map
        self._rows = len(map)
        self._columns = len(map[0])

    def is_valid(self, x, y):
        return 0 <= y <= len(self._map[0]) and 0 <= x <= len(self._map)

    def rows(self):
        return self._rows

    def columns(self):
        return self._columns

    def map(self):
        return self._map

    def get(self, x, y):
        return self._map[x][y]

    def move(self, piece, new_x, new_y):
        if not self.is_valid(new_x, new_y):
            return False

        self._map[piece.x][piece.y] = Empty(piece.x, piece.y)
        self._map[new_x][new_y] = piece
        piece.x = new_x
        piece.y = new_y
        return True

    def pacman(self):
        for x in range(self._rows):
            for y in range(self._columns):
                if self._map[x][y].is_pacman():
                    return self._map[x][y]

        return None

    def ghosts(self):
        all_ghosts = []
        for x in range(self._rows):
            for y in range(self._columns):
                if self._map[x][y].is_ghost():
                    all_ghosts.append(self._map[x][y])

        return all_ghosts

    def pills(self):
        pills = 0
        for x in range(self._rows):
            for y in range(self._columns):
                if self._map[x][y].is_pill():
                    pills += 1
        return pills


# . -> empty space (ghosts and pacman can walk)
# | and - -> wall, no one can go through it
# @ -> our hero: pacman
# G -> ghosts, they are the bad folks
# P -> pills. Pacman needs to eat them
def create_map(mapArray) -> Map:
    new_map = []

    for x in range(len(mapArray)):
        row = []
        for y in range(len(mapArray[x])):
            row.append(build_piece(mapArray[x][y], x, y))
        new_map.append(row)

    return Map(new_map)

