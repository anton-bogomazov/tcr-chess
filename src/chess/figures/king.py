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
        castling_rook = get_castling_rook(figures, to)
        if castling_rook is None or castling_rook.touched:
            raise CastlingNotPossibleError('rook is touched or moved')
        if is_castling_blocked(self.position, figures, to):
            raise CastlingNotPossibleError('castling blocked by figures')
        
        self.move(to)
        castling_rook.castle(to)

    def notation(self):
        return 'K'

    def symbol(self):
        return '\u2654' if self.color == Color.WHITE else '\u265A'
       
            
def get_castling_rook(figures, to):
    castling_rook_map = {
        ('g', 1): cell(figures, *('h', 1)),
        ('c', 1): cell(figures, *('a', 1)),
        ('g', 8): cell(figures, *('h', 8)),
        ('c', 8): cell(figures, *('a', 8)),
    }
    
    return castling_rook_map[to]
    
    
def is_castling_blocked(position, figures, to):
    from_literal, from_numeral = position
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
