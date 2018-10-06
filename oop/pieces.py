import random


class Piece:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def is_ghost(self):
        return False

    def is_wall(self):
        return False

    def is_pill(self):
        return False

    def is_pacman(self):
        return False

    def is_empty(self):
        return False

class Pacman(Piece):

    def move(self, map, game, new_x, new_y):
        if not map.is_valid(new_x, new_y):
            return

        piece_in_new_position = map.get(new_x, new_y)

        # pacman can't walk over the wall
        if piece_in_new_position.is_wall():
            return

        map.move(self, new_x, new_y)

        # if pacman commits suicide, we loose
        if piece_in_new_position.is_ghost():
            game.lost()

        # if we ate all of the pills, we win!
        if map.pills() == 0:
            game.win()

    def is_pacman(self):
        return True


class Ghost(Piece):

    def move(self, map, game):
        possible_directions = [
            [self.x, self.y + 1],  # x, y+1
            [self.x + 1, self.y],  # x+1, y
            [self.x, self.y - 1],  # x, y-1
            [self.x - 1, self.y]  # x-1, y
        ]

        random_movement = random.randint(0, 3)
        new_x = possible_directions[random_movement][0]
        new_y = possible_directions[random_movement][1]

        if not map.is_valid(new_x, new_y):
            return

        piece_in_new_position = map.get(new_x, new_y)

        if not piece_in_new_position.is_wall() and not piece_in_new_position.is_ghost() and not piece_in_new_position.is_pill():
            if piece_in_new_position.is_pacman():  # if ghost gets pacman, game ends
                game.lost()
            else:
                map.move(self, new_x, new_y)

    def is_ghost(self):
        return True


class Pill(Piece):
    def is_pill(self):
        return True


class Wall(Piece):
    def is_wall(self):
        return True


class Empty(Piece):
    def is_empty(self):
        return True


def build_piece(piece: str, x, y) -> Piece:
    if piece == '.':
        return Empty(x, y)
    if piece == '|' or piece == '-':
        return Wall(x, y)
    if piece == '@':
        return Pacman(x, y)
    if piece == 'G':
        return Ghost(x, y)
    if piece == 'P':
        return Pill(x, y)

