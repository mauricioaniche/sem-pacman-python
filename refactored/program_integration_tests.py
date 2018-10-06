import pytest
from refactored.program import run
from refactored.randomgen import generate_int
from refactored.ui import ui_final_message, ui_print


def fake_ui_key_setup(keys):
    pytest.fake_keys = keys


def fake_ui_key():
    current_key = pytest.fake_keys.pop(0)
    return current_key


def fake_int_setup(nums):
    pytest.fake_ints = nums


def fake_int(a, b):
    current_number = pytest.fake_ints.pop(0)
    return current_number


def test_win():
    win_map = ["|G...P.@|"]

    fake_ui_key_setup(['a', 'a'])
    game_finished, win = run(win_map, ui_print, fake_ui_key, ui_final_message, generate_int)

    assert game_finished is True
    assert win is True


def test_lose():
    lose_map = ["|G....@P|"]

    fake_ui_key_setup(['a', 'a', 'a', 'a', 'a'])
    game_finished, win = run(lose_map, ui_print, fake_ui_key, ui_final_message, generate_int)

    assert game_finished is True
    assert win is False


def test_ghost_wins():
    lose_map = [
        "|G...@|",
        "|.....|"
        "|.....|"
        "|.....|"
        "|..P..|"
    ]

    fake_ui_key_setup(['a', 'a', 'a'])
    fake_int_setup([0, 0, 0, 0, 0, 0])

    game_finished, win = run(lose_map, ui_print, fake_ui_key, ui_final_message, fake_int)

    assert game_finished is True
    assert win is False
