from termcolor import colored


def get_valid_key():
    valid_keys = ['a', 's', 'w', 'd']
    while True:
        key = input()
        if key in valid_keys:
            return key


class SimpleUI:
    def print(self, map):
        for row in map.map():
                for point in row:

                    # if it's a ghost
                    if point.is_ghost():
                        print('G', end='')
                    # if it's a wall
                    elif point.is_wall():
                        print('|', end='')
                    # if it's a pacman
                    elif point.is_pacman():
                        print('@', end='')
                    # if it's empty
                    elif point.is_empty():
                        print('.', end='')
                    # if it's a pill
                    elif point.is_pill():
                        print('P', end='')
                print("", end='\n')


class AsciiArtUI:
    # We want to print our game using beautiful ASCII-art images.
    # There they go.
    # Boolean used to determine if colors should be added to UI elements
    def __init__(self, add_colors_to_ui_elements=False):
        # Choose a color for UI elements
        # Possible colors can be found on https://pypi.org/project/termcolor/
        wall_color = "blue"
        ghost_color = "red"
        pacman_color = "yellow"
        pill_color = "grey"

        self.ui_wall = [
            "||||||",
            "||||||",
            "||||||",
            "||||||"
        ]

        self.ui_ghost = [
            " .-.  ",
            "| OO| ",
            "|   | ",
            "'^^^' "
        ]

        self.ui_pacman = [
            " .--. ",
            "/ _.-'",
            "\\  '-.",
            " '--' "
        ]

        self.ui_empty = [
            "      ",
            "      ",
            "      ",
            "      "
        ]

        self.ui_pill = [
            "      ",
            " .''. ",
            " '..' ",
            "      "
        ]

        # How many rows does the UI element consist of
        rows_per_ui_element = len(self.ui_wall)

        if add_colors_to_ui_elements:
            for i in range(rows_per_ui_element):
                self.ui_wall[i] = colored(self.ui_wall[i], wall_color)
                self.ui_ghost[i] = colored(self.ui_ghost[i], ghost_color)
                self.ui_pacman[i] = colored(self.ui_pacman[i], pacman_color)
                self.ui_pill[i] = colored(self.ui_pill[i], pill_color)


    def print(self, map):
        for row in map.map():
            for piece in range(4):
                for point in row:

                    # if it's a ghost
                    if point.is_ghost():
                        print(self.ui_ghost[piece], end='')
                    # if it's a wall
                    elif point.is_wall():
                        print(self.ui_wall[piece], end='')
                    # if it's a pacman
                    elif point.is_pacman():
                        print(self.ui_pacman[piece], end='')
                    # if it's empty
                    elif point.is_empty():
                        print(self.ui_empty[piece], end='')
                    # if it's a pill
                    elif point.is_pill():
                        print(self.ui_pill[piece], end='')
                print("", end='\n')