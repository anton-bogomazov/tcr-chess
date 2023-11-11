from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.color import Color


class Queen(ChessFigure):
    def turns(self, figures=frozenset()):
        literal, numeral = self.position
        rook_turns = [(chr(ord(literal) - i), numeral) for i in range(1, 8)] +\
                     [(chr(ord(literal) + i), numeral) for i in range(1, 8)] +\
                     [(chr(ord(literal)), numeral + i) for i in range(1, 8)] +\
                     [(chr(ord(literal)), numeral - i) for i in range(1, 8)]
        bishop_turns = [(chr(ord(literal) - i), numeral - i) for i in range(1, 8)] +\
                       [(chr(ord(literal) + i), numeral + i) for i in range(1, 8)] +\
                       [(chr(ord(literal) - i), numeral + i) for i in range(1, 8)] +\
                       [(chr(ord(literal) + i), numeral - i) for i in range(1, 8)]

        return set(filter(lambda t: not self.is_out_of_board(*t), rook_turns + bishop_turns)) - {self.position}

    def notation(self):
        return 'Q'

    def symbol(self):
        return '\u2655' if self.color == Color.WHITE else '\u265B'
