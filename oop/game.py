from oop.ui import get_valid_key


class Game:

    def __init__(self, map, ui):
        self._map = map
        self._game_finished = False
        self._win = False
        self._ui = ui

        self._pacman = map.pacman()

    def win(self):
        self._game_finished = True
        self._win = True

    def lost(self):
        self._game_finished = True
        self._win = False

    def play(self):
        while not self._game_finished:
            self._ui.print(self._map)

            self._move_ghosts()
            key = get_valid_key()
            self._move_pacman(key)

        self.end_game()

    def end_game(self):
        # game is over!
        self._ui.print(self._map)
        if self._win:
            print("You win! :)")
        else:
            print("You lost! :/")

    def _move_ghosts(self):
        for ghost in self._map.ghosts():
            ghost.move(self._map, self)

    def _move_pacman(self, key):
        x = self._pacman.x
        y = self._pacman.y
        if key == 'a':  # left
            y -= 1
        elif key == 's':  # down
            x += 1
        elif key == 'w':  # up
            x -= 1
        elif key == 'd':  # right
            y += 1

        self._pacman.move(self._map, self, x, y)


