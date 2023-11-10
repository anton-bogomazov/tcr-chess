from src.chess.board_utils import inc_num_pos, dec_num_pos, dec_lit_pos, inc_lit_pos, cell, position
from src.chess.figures import ChessFigure, Color


class Knight(ChessFigure):
    def turns(self, figures=frozenset()):
        turns = (
            [dec_lit_pos, dec_lit_pos, dec_num_pos],
            [dec_lit_pos, dec_lit_pos, inc_num_pos],
            [inc_lit_pos, inc_lit_pos, dec_num_pos],
            [inc_lit_pos, inc_lit_pos, inc_num_pos],

            [dec_lit_pos, inc_num_pos, inc_num_pos],
            [dec_lit_pos, dec_num_pos, dec_num_pos],
            [inc_lit_pos, inc_num_pos, inc_num_pos],
            [inc_lit_pos, dec_num_pos, dec_num_pos],
        )
        possible_turns = [t for t in [position(self.position, t) for t in turns] if t is not None]

        return set(possible_turns)

    def notation(self):
        return 'N'

    def symbol(self):
        return '\u2658' if self.color == Color.WHITE else '\u265E'
            