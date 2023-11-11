from src.chess.board_utils import inc_num_pos as up, dec_num_pos as down, dec_lit_pos as left, inc_lit_pos as right, cell, position
from src.chess.figures.chess_figure import ChessFigure
from src.chess.color import Color



class King(ChessFigure):
    def turns(self, figures=frozenset()):
        turns = (
            [up], [down], [left], [right],
            [up, right], [up, left], [down, right], [down, left],
        )
        turns = [t for t in [position(self.position, t) for t in turns] if t is not None]
        possible_turns = [p for p in turns if cell(figures, *p) is None or
                                              cell(figures, *p).color != self.color]
        # exclude attacked by other figures cells
        # TODO FIXME can be moved under kings attack
        opponent_figures = [f for f in figures if f.color != self.color]
        attacked_cells = [f.turns(figures) for f in opponent_figures]
        possible_turns = [t for t in possible_turns if t not in attacked_cells]
        # TODO FIXME can be moved under pawn attack
        return set(possible_turns)

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
            