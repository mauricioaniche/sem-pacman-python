

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
    # We wanna print our game using beautiful ASCII-art images.
    # There they go.
    ui_wall = [
        "......",
        "......",
        "......",
        "......"
    ]

    ui_ghost = [
        " .-.  ",
        "| OO| ",
        "|   | ",
        "'^^^' "
    ]

    ui_hero = [
        " .--. ",
        "/ _.-'",
        "\\  '-.",
        " '--' "
    ]

    ui_empty = [
        "      ",
        "      ",
        "      ",
        "      "
    ]

    ui_pill = [
        "      ",
        " .-.  ",
        " '-'  ",
        "      "
    ]

    def print(self, map):
        for row in map.map():
            for piece in range(4):
                for point in row:

                    # if it's a ghost
                    if point.is_ghost():
                        print(AsciiArtUI.ui_ghost[piece], end='')
                    # if it's a wall
                    elif point.is_wall():
                        print(AsciiArtUI.ui_wall[piece], end='')
                    # if it's a pacman
                    elif point.is_pacman():
                        print(AsciiArtUI.ui_hero[piece], end='')
                    # if it's empty
                    elif point.is_empty():
                        print(AsciiArtUI.ui_empty[piece], end='')
                    # if it's a pill
                    elif point.is_pill():
                        print(AsciiArtUI.ui_pill[piece], end='')
                print("", end='\n')