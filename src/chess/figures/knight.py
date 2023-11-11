from src.chess.board_utils import inc_num_pos, dec_num_pos, dec_lit_pos, inc_lit_pos, cell, position
from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.color import Color


class Knight(ChessFigure):
    def turns(self, figures=frozenset()):
        turns = [
            [dec_lit_pos, dec_lit_pos, dec_num_pos],
            [dec_lit_pos, dec_lit_pos, inc_num_pos],
            [inc_lit_pos, inc_lit_pos, dec_num_pos],
            [inc_lit_pos, inc_lit_pos, inc_num_pos],

            [dec_lit_pos, inc_num_pos, inc_num_pos],
            [dec_lit_pos, dec_num_pos, dec_num_pos],
            [inc_lit_pos, inc_num_pos, inc_num_pos],
            [inc_lit_pos, dec_num_pos, dec_num_pos],
        ]

        return set(self.calc_singly_moves(figures, turns))

    def notation(self):
        return 'N'

    def symbol(self):
        return '\u2658' if self.color == Color.WHITE else '\u265E'
            