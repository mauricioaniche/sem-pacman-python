from termcolor import colored


# We want to print our game using beautiful ASCII-art images.
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

# Define UI colors
wall_color = "blue"
ghost_color = "red"
pacman_color = "yellow"
pill_color = "grey"

def ui_print(map):
    for row in map:
        for piece in range(4):
            for point in row:

                # if it's a ghost
                if point == 'G':
                    print(colored(ui_ghost[piece], ghost_color), end='')
                # if it's a wall
                elif point == '|' or point == '-':
                    print(colored(ui_wall[piece], wall_color), end='')
                # if it's a pacman
                elif point == '@':
                    print(colored(ui_pacman[piece], pacman_color), end='')
                # if it's empty
                elif point == '.':
                    print(ui_empty[piece], end='')
                # if it's a pill
                elif point == 'P':
                    print(colored(ui_pill[piece], pill_color), end='')

            print("", end='\n')


def ui_final_message(win):
    if win:
        print("You win! :)")
    else:
        print("You lost! :/")

def ui_key():
    return input()