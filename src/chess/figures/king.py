from src.chess.board_utils import inc_num_pos as up, dec_num_pos as down, dec_lit_pos as left, inc_lit_pos as right
from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.color import Color


class King(ChessFigure):
    def turns(self, figures=frozenset()):
        turns = (
            [up], [down], [left], [right],
            [up, right], [up, left], [down, right], [down, left],
        )

        return set(self.calc_singly_moves(figures, turns))

    def castle(self, to):
        self.position = to
        self.touched = True

    def notation(self):
        return 'K'

    def symbol(self):
        return '\u2654' if self.color == Color.WHITE else '\u265A'
            