from oop.game import Game
from oop.map import create_map
from oop.ui import SimpleUI

map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G....@|.|",
    "|...P..|.|",
    "|--------|"
]

map = create_map(map)
ui = SimpleUI() # or AsciiArtUI
game = Game(map, ui)
game.play()