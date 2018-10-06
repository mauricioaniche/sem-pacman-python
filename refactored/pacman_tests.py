from refactored.pacman import within_borders, is_wall, total_pills, find_pacman

map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G....@|.|",
    "|...P..|.|",
    "|--------|"
]

def test_within_borders():
    assert (within_borders(map, 1, 2) is True)
    assert (within_borders(map, 5, 4) is True)

    # boundaries
    assert (within_borders(map, 0, 0) is True)
    assert (within_borders(map, 5, 10) is True)

    # y boundaries
    assert (within_borders(map, 1, -1) is False)
    assert (within_borders(map, 1, 10) is True)
    assert (within_borders(map, 1, 11) is False)

    # x boundaries
    assert (within_borders(map, -1, 2) is False)
    assert (within_borders(map, 0, 2) is True)
    assert (within_borders(map, 5, 2) is True)
    assert (within_borders(map, 6, 2) is True)


def test_is_wall():
    assert (is_wall(map, 0, 0) is True)
    assert (is_wall(map, 0, 1) is True)
    assert (is_wall(map, 1, 1) is False)


def test_total_pills():
    assert (total_pills(map) == 3)

    map_no_pills = [
        "|--------|",
        "|G..|..G.|",
        "|........|",
        "|G....@|.|",
        "|......|.|",
        "|--------|"
    ]

    assert (total_pills(map_no_pills) == 0)


def test_find_pacman():
    assert(find_pacman(map) == 3, 6)

    map_no_pacman = ["..", ".."]
    assert (find_pacman(map_no_pacman) == -1, -1)
