from src.chess.game import standard_chess_game
from src.ui.cli import Cli
from src.ui.gui import Gui
from src.ui.gui_driver import GuiDriver


# once checked king cant castle
# implement en passant capturing
def main():
    game = standard_chess_game()
    mode = 'gui'
    match mode:
        case 'gui':
            Gui(game).start()
        case 'cli':
            Cli(game).start()
        case 'auto':
            GuiDriver(game).start([])
        case _:
            Cli(game).start()


if __name__ == '__main__':
    main()
    