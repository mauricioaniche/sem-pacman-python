import random

from getkey import getkey, keys

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


# our game runs until pacman eats everything or ghosts get the pacman
game_finished = False
win = False
while not game_finished:


    # --- print the map
    for row in map:
        for piece in range(4):
            for point in row:

                # if it's a ghost
                if point == 'G':
                    print(ui_ghost[piece], end = '')
                # if it's a wall
                elif point == '|' or point == '-':
                    print(ui_wall[piece], end = '')
                # if it's a pacman
                elif point == '@':
                    print(ui_hero[piece], end = '')
                # if it's empty
                elif point == '.':
                    print(ui_empty[piece], end = '')
                # if it's a pill
                elif point == 'P':
                    print(ui_pill[piece], end = '')

            print("", end='\n')

    # --- let's move the ghosts
    all_ghosts = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'G':
                all_ghosts.append([x,y])

    for ghost in all_ghosts:
        old_ghost_x = ghost[0]
        old_ghost_y = ghost[1]

        possible_directions = [
            [old_ghost_x, old_ghost_y + 1], # x, y+1
            [old_ghost_x + 1, old_ghost_y],  # x+1, y
            [old_ghost_x, old_ghost_y - 1],  # x, y-1
            [old_ghost_x - 1, old_ghost_y]  # x-1, y
        ]

        random_movement = random.randint(0,3)
        next_ghost_x = possible_directions[random_movement][0]
        next_ghost_y = possible_directions[random_movement][1]

        y_is_valid = next_ghost_y >= 0 and next_ghost_y <= len(map[0])
        x_is_valid = next_ghost_x >= 0 and next_ghost_x < len(map)

        if not (y_is_valid and x_is_valid):
            continue

        is_wall = map[next_ghost_x][next_ghost_y] == '|' or map[next_ghost_x][next_ghost_y] == '-'
        is_ghost = map[next_ghost_x][next_ghost_y] == 'G'
        is_pill = map[next_ghost_x][next_ghost_y] == 'P'
        is_pacman = map[next_ghost_x][next_ghost_y] == '@'

        if not is_wall and not is_ghost and not is_pill:
            if is_pacman: # if ghost gets pacman, game ends
                game_finished = True
            else:
                map[old_ghost_x] = map[old_ghost_x][0:old_ghost_y] + "." + map[old_ghost_x][old_ghost_y + 1:]
                map[next_ghost_x] = map[next_ghost_x][0:next_ghost_y] + "G" + map[next_ghost_x][next_ghost_y + 1:]

    if game_finished:
        break

    # --- find where the pacman is right now
    pacman_x = -1
    pacman_y = -1

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    # create a new pair of variables, because we need both the old and new location
    next_pacman_x = pacman_x
    next_pacman_y = pacman_y

    # --- get the key from the keyboard
    # what's pacman's next movement?
    key = input()

    if key == 'a': # left
        next_pacman_y-=1
    elif key == 's': # down
        next_pacman_x += 1
    elif key == 'w': # up
        next_pacman_x-=1
    elif key == 'd': # right
        next_pacman_y += 1
    else: # invalid key
        continue

    # --- can we really go to that position?

    # check if x and y are within the borders of the map
    y_is_valid = next_pacman_y >= 0 and next_pacman_y <= len(map[0])
    x_is_valid = next_pacman_x >= 0 and next_pacman_x <= len(map)
    if not (x_is_valid and y_is_valid):
        continue

    # check if it's not a wall or a ghost
    # if it's an invalid position, just start all over!
    is_wall = map[next_pacman_x][next_pacman_y] == '|' or map[next_pacman_x][next_pacman_y] == '-'
    if is_wall:
        continue

    # if pacman commits suicide, we loose
    is_ghost = map[next_pacman_x][next_pacman_y] == 'G'
    if is_ghost:
        game_finished = True
        win = False

    # --- move to that position
    # first, the old position (where the pacman was) becomes empty
    map[pacman_x] = map[pacman_x][0:pacman_y] + "." + map[pacman_x][pacman_y+1:]
    # then, the new position (where pacman should be) becomes the pacman
    map[next_pacman_x] = map[next_pacman_x][0:next_pacman_y] + "@" + map[next_pacman_x][next_pacman_y + 1:]

    # -- let's count the number of pills. Maybe we just won the game!
    total_pills = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'P':
                total_pills += 1

    if total_pills == 0:
        win = True
        game_finished = True
        break



# --- print the map for the last time
for row in map:
    for piece in range(4):
        for point in row:

            # if it's a ghost
            if point == 'G':
                print(ui_ghost[piece], end = '')
            # if it's a wall
            elif point == '|' or point == '-':
                print(ui_wall[piece], end = '')
            # if it's a pacman
            elif point == '@':
                print(ui_hero[piece], end = '')
            # if it's empty
            elif point == '.':
                print(ui_empty[piece], end = '')
            # if it's a pill
            elif point == 'P':
                print(ui_pill[piece], end = '')

        print("", end='\n')

if win:
    print("You win! :)")
else:
    print("You lost! :/")