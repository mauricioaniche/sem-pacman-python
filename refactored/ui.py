
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

ui_pacman = [
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


def ui_print(map):
    for row in map:
        for piece in range(4):
            for point in row:

                # if it's a ghost
                if point == 'G':
                    print(ui_ghost[piece], end='')
                # if it's a wall
                elif point == '|' or point == '-':
                    print(ui_wall[piece], end='')
                # if it's a pacman
                elif point == '@':
                    print(ui_pacman[piece], end='')
                # if it's empty
                elif point == '.':
                    print(ui_empty[piece], end='')
                # if it's a pill
                elif point == 'P':
                    print(ui_pill[piece], end='')

            print("", end='\n')


def ui_final_message(win):
    if win:
        print("You win! :)")
    else:
        print("You lost! :/")

def ui_key():
    return input()