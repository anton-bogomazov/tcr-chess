from src.chess.board_utils import inc_num_pos, dec_num_pos, dec_lit_pos, inc_lit_pos, cell, position
from src.chess.figures import ChessFigure, Color


class King(ChessFigure):
    def turns(self, figures=frozenset()):
        literal, numeral = self.position
        turns = [
            (chr(ord(literal) + 1), numeral + 1),
            (chr(ord(literal) - 1), numeral - 1),
            (chr(ord(literal) - 1), numeral + 1),
            (chr(ord(literal) + 1), numeral - 1),
            (chr(ord(literal)), numeral - 1),
            (chr(ord(literal)), numeral + 1),
            (chr(ord(literal) + 1), numeral),
            (chr(ord(literal) - 1), numeral),
        ]
        return set(filter(lambda t: not self.is_out_of_board(*t), turns))

    def castle(self, to):
        self.position = to
        self.touched = True

    def notation(self):
        return 'K'

    def symbol(self):
        return '\u2654' if self.color == Color.WHITE else '\u265A'
            