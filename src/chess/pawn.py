from src.chess.board_utils import inc_num_pos, dec_num_pos, dec_lit_pos, inc_lit_pos, cell, position
from functools import reduce
from src.chess.figures import ChessFigure, Color


class Pawn(ChessFigure):
    def turns(self, figures=frozenset()):
        whites = {
            'short': [inc_num_pos],
            'long': [inc_num_pos, inc_num_pos],
            'attack_left': [inc_num_pos, dec_lit_pos],
            'attack_right': [inc_num_pos, inc_lit_pos],
        }
        blacks = {
            'short': [dec_num_pos],
            'long': [dec_num_pos, dec_num_pos],
            'attack_left': [dec_num_pos, dec_lit_pos],
            'attack_right': [dec_num_pos, inc_lit_pos],
        }
        turns = whites if self.color == Color.WHITE else blacks

        moving_turns = {position(self.position, turns['short'])} if self.touched \
                       else {position(self.position, turns['long']), position(self.position, turns['short'])}
        moving_turns = [t for t in moving_turns if t is not None]
        moving_turns = [move for move in moving_turns if cell(figures, *move) is None]

        attacking_turns = [position(self.position, turns['attack_left']), position(self.position, turns['attack_right'])]
        attacking_turns = [t for t in attacking_turns if t is not None]
        attacking_turns = [move for move in attacking_turns
                           if cell(figures, *move) is not None and
                              cell(figures, *move).color != self.color]

        return set([t for t in (moving_turns + attacking_turns) if t is not None])

    def notation(self):
        return 'p'

    def symbol(self):
        return '\u2659' if self.color == Color.WHITE else '\u265F'
            