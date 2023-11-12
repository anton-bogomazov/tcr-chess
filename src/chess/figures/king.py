from src.chess.board_utils import cell, inc_num_pos as up, dec_num_pos as down, dec_lit_pos as left, inc_lit_pos as right
from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.color import Color


class King(ChessFigure):
    def turns(self, figures):
        turns = (
            [up], [down], [left], [right],
            [up, right], [up, left], [down, right], [down, left],
        )

        return set(self.calc_singly_moves(figures, turns))

    def castle(self, to):
        self.position = to
        self.touched = True

    def is_castling_blocked(self, figures, rook_position):
        from_literal, from_numeral = self.position
        to_literal, to_numeral = rook_position

        assert from_numeral == to_numeral

        if ord(from_literal) < ord(to_literal):
            n = 0
            while ord(from_literal) < ord(to_literal)-n:
                if cell(figures, to_literal, to_numeral) is not None:
                    return True
                n += 1
        if ord(from_literal) > ord(to_literal):
            n = 0
            while ord(from_literal) > ord(to_literal)+n:
                if cell(figures, to_literal, to_numeral) is not None:
                    return True
                n += 1

        return False

    def notation(self):
        return 'K'

    def symbol(self):
        return '\u2654' if self.color == Color.WHITE else '\u265A'
            