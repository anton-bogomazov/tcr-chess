import time
from src.ui.gui import Gui


class GuiDriver:
    def __init__(self, game):
        self.game = game
        self.gui = Gui(game)

    def start(self, moves):
        for move in moves:
            self.game.turn(*move)
            self.gui.refresh()
            time.sleep(2)
