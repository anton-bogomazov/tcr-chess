from src.chess.board_utils import cell, inc_num_pos as up, dec_num_pos as down, dec_lit_pos as left, inc_lit_pos as right
from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.color import Color
from src.chess.error import CastlingNotPossibleError


class King(ChessFigure):
    def turns(self, figures):
        turns = (
            [up], [down], [left], [right],
            [up, right], [up, left], [down, right], [down, left],
        )

        return set(self.calc_singly_moves(figures, turns))

    def checked(self, figures):
        opponents_figures = [f for f in figures if f.color != self.color]
        for fig in opponents_figures:
            if self.position in fig.turns(figures):
                return True
        return False

    def castle(self, figures, to):
        if self.touched:
            raise CastlingNotPossibleError('king is touched')
        if self.get_castling_rook(figures, to) is None or self.get_castling_rook(figures, to).touched:
            raise CastlingNotPossibleError('rook is touched or moved')
        if self.is_castling_blocked(figures, to):
            raise CastlingNotPossibleError('castling blocked by figures')
        
        self.position = to
        self.touched = True
        self.get_castling_rook(figures, to).castle(to)

    def is_castling_blocked(self, figures, to):
        from_literal, from_numeral = self.position
        to_literal, to_numeral = to

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

    def get_castling_rook(self, figures, to):
        if to == ('g', 1):
            return cell(figures, *('h', 1))
        if to == ('c', 1):
            return cell(figures, *('a', 1))
        if to == ('g', 8):
            return cell(figures, *('h', 8))
        if to == ('c', 8):
            return cell(figures, *('a', 8))

    def notation(self):
        return 'K'

    def symbol(self):
        return '\u2654' if self.color == Color.WHITE else '\u265A'
            