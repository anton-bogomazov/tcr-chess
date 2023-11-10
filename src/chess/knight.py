from src.chess.board_utils import inc_num_pos, dec_num_pos, dec_lit_pos, inc_lit_pos, cell
from functools import reduce
from src.chess.figures import ChessFigure, Color


class Knight(ChessFigure):
    def turns(self, figures=frozenset()):
        literal, numeral = self.position
        turns = [
            (chr(ord(literal) - 2), numeral - 1),
            (chr(ord(literal) - 2), numeral + 1),
            (chr(ord(literal) + 2), numeral - 1),
            (chr(ord(literal) + 2), numeral + 1),
            (chr(ord(literal) - 1), numeral - 2),
            (chr(ord(literal) - 1), numeral + 2),
            (chr(ord(literal) + 1), numeral - 2),
            (chr(ord(literal) + 1), numeral + 2),
        ]
        return set(filter(lambda t: not self.is_out_of_board(*t), turns))

    def notation(self):
        return 'N'

    def symbol(self):
        return '\u2658' if self.color == Color.WHITE else '\u265E'
            