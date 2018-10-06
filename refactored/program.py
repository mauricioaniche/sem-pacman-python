from refactored.pacman import play, total_pills, move_ghosts
from refactored.ui import ui_print, ui_key, ui_final_message

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

game_finished = False
win = False
while not game_finished:

    # print the map
    ui_print(map)

    # find where the pacman is right now
    key = ui_key()
    game_finished, win = play(map, key)

    # let's count the number of pills. Maybe we just won the game!
    if total_pills(map) == 0:
        game_finished, win = True, True
    else:
        # didnt win, let's move the ghosts
        game_finished, win = move_ghosts(map)

# print the map for the last time
ui_print(map)
ui_final_message(win)
