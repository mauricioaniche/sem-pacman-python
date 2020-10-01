from refactored.pacman import play, total_pills, move_ghosts
from refactored.randomgen import generate_int
from refactored.ui import ui_print, ui_key, ui_final_message


def run(map, ui_print, ui_key, ui_final_message, generate_int):
    game_finished = False
    win = False
    while not game_finished:

        ui_print(map)

        key = ui_key()
        game_finished, win, invalid_key = play(map, key)

        if not game_finished and not invalid_key:
            game_finished, win = move_ghosts(map, generate_int)

    # print the map for the last time
    ui_print(map)
    ui_final_message(win)

    return game_finished, win


if __name__ == "__main__":
    # Initialize the map
    # . -> empty space (ghosts and pacman can walk)
    # | and - -> wall, no one can go through it
    # @ -> our hero: pacman
    # G -> ghosts, they are the bad folks
    # P -> pills. Pacman needs to eat them
    map = [
        "|--------|",
        "|G..|..G.|",
        "|...PP...|",
        "|G....@|.|",
        "|...P..|.|",
        "|--------|"
    ]

    run(map, ui_print, ui_key, ui_final_message, generate_int)
