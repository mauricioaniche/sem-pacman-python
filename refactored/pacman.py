def find_pacman(map):
    pacman_x = -1
    pacman_y = -1

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y


def within_borders(map, x, y):
    y_is_valid = 0 <= y < len(map[0])
    x_is_valid = 0 <= x < len(map)

    return y_is_valid and x_is_valid


def _is_character(map, character, x, y):
    return map[x][y] == character


def is_wall(map, x, y):
    return _is_character(map, '|', x, y) \
           or _is_character(map, '-', x, y)


def is_ghost(map, x, y):
    return _is_character(map, 'G', x, y)


def is_pill(map, x, y):
    return _is_character(map, 'P', x, y)


def is_pacman(map, x, y):
    return _is_character(map, '@', x, y)


def total_pills(map):
    total = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'P':
                total += 1
    return total


def move_pacman(map, pacman_x, pacman_y, next_pacman_x, next_pacman_y):
    # first, the old position (where the pacman was) becomes empty
    map[pacman_x] = map[pacman_x][0:pacman_y] + "." + map[pacman_x][pacman_y + 1:]
    # then, the new position (where pacman should be) becomes the pacman
    map[next_pacman_x] = map[next_pacman_x][0:next_pacman_y] + "@" + map[next_pacman_x][next_pacman_y + 1:]


def get_all_ghosts(map):
    all_ghosts = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'G':
                all_ghosts.append([x, y])
    return all_ghosts


def move_ghosts(map, generate_int):
    for ghost in get_all_ghosts(map):
        old_ghost_x = ghost[0]
        old_ghost_y = ghost[1]

        possible_directions = [
            [old_ghost_x, old_ghost_y + 1],  # x, y+1
            [old_ghost_x + 1, old_ghost_y],  # x+1, y
            [old_ghost_x, old_ghost_y - 1],  # x, y-1
            [old_ghost_x - 1, old_ghost_y]  # x-1, y
        ]

        random_movement = generate_int(0, 3)
        next_ghost_x = possible_directions[random_movement][0]
        next_ghost_y = possible_directions[random_movement][1]

        if not within_borders(map, next_ghost_x, next_ghost_y):
            continue

        wall = is_wall(map, next_ghost_x, next_ghost_y)
        ghost = is_ghost(map, next_ghost_x, next_ghost_y)
        pill = is_pill(map, next_ghost_x, next_ghost_y)
        pacman = is_pacman(map, next_ghost_x, next_ghost_y)

        if not wall and not ghost and not pill:
            if pacman:  # if ghost gets pacman, game ends
                return True, False
            else:
                map[old_ghost_x] = map[old_ghost_x][0:old_ghost_y] + "." + map[old_ghost_x][old_ghost_y + 1:]
                map[next_ghost_x] = map[next_ghost_x][0:next_ghost_y] + "G" + map[next_ghost_x][next_ghost_y + 1:]

    return False, False


def next_position(key, x, y):
    if key == 'a':  # left
        return x, y - 1
    elif key == 's':  # down
        return x + 1, y
    elif key == 'w':  # up
        return x - 1, y
    elif key == 'd':  # right
        return x, y + 1
    else:
        return -1, -1


def play(map, key):
    pacman_x, pacman_y = find_pacman(map)

    # what's pacman's next movement?
    next_pacman_x, next_pacman_y = next_position(key, pacman_x, pacman_y)
    invalid_key = next_pacman_x == -1 and next_pacman_x == -1
    if invalid_key:
        return False, False

    # check if x and y are within the borders of the map
    if not within_borders(map, next_pacman_x, next_pacman_y):
        return False, False

    # check if it's not a wall or a ghost
    # if it's an invalid position, just start all over!
    if is_wall(map, next_pacman_x, next_pacman_y):
        return False, False

    # if pacman commits suicide, we loose
    if is_ghost(map, next_pacman_x, next_pacman_y):
        return True, False

    # move to that position
    move_pacman(map, pacman_x, pacman_y, next_pacman_x, next_pacman_y)

    ate_all_pills = total_pills(map) == 0
    return ate_all_pills, ate_all_pills
