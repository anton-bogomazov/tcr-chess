from src.chess.board_utils import inc_num_pos as up, dec_num_pos as down, dec_lit_pos as left, inc_lit_pos as right, position, cell
from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.color import Color


class Pawn(ChessFigure):

    # ugly
    def turns(self, figures):
        whites = {
            'short': [up],
            'long': [up, up],
            'attack_left': [up, left],
            'attack_right': [up, right],
        }
        blacks = {
            'short': [down],
            'long': [down, down],
            'attack_left': [down, left],
            'attack_right': [down, right],
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

        return set(moving_turns + attacking_turns)

    def notation(self):
        return 'p'

    def symbol(self):
        return '\u2659' if self.color == Color.WHITE else '\u265F'
            