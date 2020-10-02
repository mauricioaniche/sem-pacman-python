import unittest

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


class Tests(unittest.TestCase):
    def test_within_borders(self):
        map = get_map()

        self.assertTrue(within_borders(map, 1, 2))
        self.assertTrue(within_borders(map, 5, 4))

        # boundaries
        self.assertTrue(within_borders(map, 0, 0))
        self.assertTrue(within_borders(map, 5, 9))

        # y boundaries
        self.assertFalse(within_borders(map, 1, -1))
        self.assertTrue(within_borders(map, 1, 9))
        self.assertFalse(within_borders(map, 1, 10))
        self.assertFalse(within_borders(map, 1, 11))

        # x boundaries
        self.assertFalse(within_borders(map, -1, 2))
        self.assertTrue(within_borders(map, 0, 2))
        self.assertTrue(within_borders(map, 5, 2))
        self.assertFalse(within_borders(map, 6, 2))

    def test_is_wall(self):
        map = get_map()

        self.assertTrue(is_wall(map, 0, 0))
        self.assertTrue(is_wall(map, 0, 1))
        self.assertFalse(is_wall(map, 1, 1))

    def test_is_pill(self):
        map = get_map()

        self.assertTrue(is_pill(map, 2, 4))
        self.assertTrue(is_pill(map, 2, 5))
        self.assertFalse(is_pill(map, 1, 1))

    def test_is_ghost(self):
        map = get_map()

        self.assertTrue(is_ghost(map, 1, 1))
        self.assertFalse(is_ghost(map, 2, 2))

    def test_total_pills(self):
        map = get_map()

        self.assertEqual(total_pills(map), 3)

        map_no_pills = [
            "|--------|",
            "|G..|..G.|",
            "|........|",
            "|G....@|.|",
            "|......|.|",
            "|--------|"
        ]

        self.assertEqual(total_pills(map_no_pills), 0)

    def test_find_pacman(self):
        map = get_map()

        self.assertEqual(find_pacman(map), (3, 6))

        map_no_pacman = ["..", ".."]
        self.assertEqual(find_pacman(map_no_pacman), (-1, -1))

    def test_next_position(self):
        x, y = 2, 2
        self.assertEqual(next_position('a', x, y), (2, 1))
        self.assertEqual(next_position('s', x, y), (3, 2))
        self.assertEqual(next_position('w', x, y), (1, 2))
        self.assertEqual(next_position('d', x, y), (2, 3))

        self.assertEqual(next_position('b', x, y), (-1, -1))

    def test_move_pacman(self):
        map = get_map()

        x, y = find_pacman(map)

        self.assertTrue(is_pacman(map, x, y))

        new_x, new_y = x, y - 1
        move_pacman(map, x, y, new_x, new_y)

        self.assertFalse(is_pacman(map, x, y))
        self.assertTrue(is_pacman(map, new_x, new_y))

    def test_play_move(self):
        map = get_map()

        x, y = find_pacman(map)
        play(map, 'a')

        self.assertEqual(find_pacman(map), (x, y - 1))

    def test_play_eat_pills(self):
        map = get_map()

        x, y = find_pacman(map)
        play(map, 'a')

        self.assertEqual(find_pacman(map), (x, y - 1))
        self.assertEqual(total_pills(map), 3)

        play(map, 'w')

        self.assertEqual(find_pacman(map), (x - 1, y - 1))
        self.assertEqual(total_pills(map), 2)

    def test_play_die(self):
        simple_map = get_simple_map()

        game_finished, win, _ = play(simple_map, 'a')

        self.assertTrue(game_finished)
        self.assertFalse(win)

    def test_play_win(self):
        simple_map_2 = get_simple_map_2()

        game_finished, win, _ = play(simple_map_2, 'd')

        self.assertTrue(game_finished)
        self.assertTrue(win)

    def test_play_invalid(self):
        map = get_map()

        x, y = find_pacman(map)
        play(map, 'x')

        self.assertEqual(find_pacman(map), (x, y))

    def test_play_outside_borders(self):
        map = ["@..P"]

        x, y = find_pacman(map)
        play(map, 'a')

        self.assertEqual(find_pacman(map), (x, y))

    def test_play_wall(self):
        map = ["|@..P"]

        x, y = find_pacman(map)
        play(map, 'a')

        self.assertEqual(find_pacman(map), (x, y))

    def test_get_all_ghosts(self):
        map = get_map()

        ghosts = get_all_ghosts(map)

        self.assertEqual(ghosts[0], [1, 1])
        self.assertEqual(ghosts[1], [1, 7])
        self.assertEqual(ghosts[2], [3, 1])

        map = ["....."]

        ghosts = get_all_ghosts(map)
        self.assertEqual(ghosts, [])


if __name__ == "__main__":
    unittest.main()
