from oop.game import Game
from oop.map import create_map
from oop.ui import AsciiArtUI

map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G....@|.|",
    "|...P..|.|",
    "|--------|"
]

map = create_map(map)
ui = AsciiArtUI(True) # or SimpleUI
game = Game(map, ui)
game.play()