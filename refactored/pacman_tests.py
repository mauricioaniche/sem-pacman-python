from refactored.pacman import within_borders, is_wall, total_pills, find_pacman, next_position, move_pacman, is_pacman, \
    is_pill, is_ghost, play, get_all_ghosts


def get_map():
    return [
        "|--------|",
        "|G..|..G.|",
        "|...PP...|",
        "|G....@|.|",
        "|...P..|.|",
        "|--------|"
    ]


def get_simple_map():
    return ["|G@|"]


def get_simple_map_2():
    return ["|G....@P|"]


def test_within_borders():
    map = get_map()

    assert within_borders(map, 1, 2) is True
    assert within_borders(map, 5, 4) is True

    # boundaries
    assert within_borders(map, 0, 0) is True
    assert within_borders(map, 5, 9) is True

    # y boundaries
    assert within_borders(map, 1, -1) is False
    assert within_borders(map, 1, 9) is True
    assert within_borders(map, 1, 10) is False
    assert within_borders(map, 1, 11) is False

    # x boundaries
    assert within_borders(map, -1, 2) is False
    assert within_borders(map, 0, 2) is True
    assert within_borders(map, 5, 2) is True
    assert within_borders(map, 6, 2) is False


def test_is_wall():
    map = get_map()

    assert is_wall(map, 0, 0) is True
    assert is_wall(map, 0, 1) is True
    assert is_wall(map, 1, 1) is False


def test_is_pill():
    map = get_map()

    assert is_pill(map, 2, 4) is True
    assert is_pill(map, 2, 5) is True
    assert is_pill(map, 1, 1) is False


def test_is_ghost():
    map = get_map()

    assert is_ghost(map, 1, 1) is True
    assert is_ghost(map, 2, 2) is False


def test_total_pills():
    map = get_map()

    assert total_pills(map) == 3

    map_no_pills = [
        "|--------|",
        "|G..|..G.|",
        "|........|",
        "|G....@|.|",
        "|......|.|",
        "|--------|"
    ]

    assert total_pills(map_no_pills) == 0


def test_find_pacman():
    map = get_map()

    assert find_pacman(map) == (3, 6)

    map_no_pacman = ["..", ".."]
    assert find_pacman(map_no_pacman) == (-1, -1)


def test_next_position():
    x, y = 2, 2
    assert next_position('a', x, y) == (2, 1)
    assert next_position('s', x, y) == (3, 2)
    assert next_position('w', x, y) == (1, 2)
    assert next_position('d', x, y) == (2, 3)

    assert next_position('b', x, y) == (-1, -1)


def test_move_pacman():
    map = get_map()

    x, y = find_pacman(map)

    assert is_pacman(map, x, y) is True

    new_x, new_y = x, y - 1
    move_pacman(map, x, y, new_x, new_y)

    assert is_pacman(map, x, y) is False
    assert is_pacman(map, new_x, new_y) is True


def test_play_move():
    map = get_map()

    x, y = find_pacman(map)
    play(map, 'a')

    assert find_pacman(map) == (x, y - 1)


def test_play_eat_pills():
    map = get_map()

    x, y = find_pacman(map)
    play(map, 'a')

    assert find_pacman(map) == (x, y - 1)
    assert total_pills(map) == 3

    play(map, 'w')

    assert find_pacman(map) == (x - 1, y - 1)
    assert total_pills(map) == 2


def test_play_die():
    simple_map = get_simple_map()

    game_finished, win = play(simple_map, 'a')

    assert game_finished is True
    assert win is False


def test_play_win():
    simple_map_2 = get_simple_map_2()

    game_finished, win = play(simple_map_2, 'd')

    assert game_finished is True
    assert win is True


def test_play_invalid():
    map = get_map()

    x, y = find_pacman(map)
    play(map, 'x')

    assert find_pacman(map) == (x, y)


def test_play_outside_borders():
    map = ["@..P"]

    x, y = find_pacman(map)
    play(map, 'a')

    assert find_pacman(map) == (x, y)


def test_play_wall():
    map = ["|@..P"]

    x, y = find_pacman(map)
    play(map, 'a')

    assert find_pacman(map) == (x, y)


def test_get_all_ghosts():
    map = get_map()

    ghosts = get_all_ghosts(map)

    assert ghosts[0] == [1, 1]
    assert ghosts[1] == [1, 7]
    assert ghosts[2] == [3, 1]

    map = ["....."]

    ghosts = get_all_ghosts(map)
    assert ghosts == []
