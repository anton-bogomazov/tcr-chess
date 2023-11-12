from src.chess.board_utils import inc_num_pos as up, dec_num_pos as down, dec_lit_pos as left, inc_lit_pos as right, position, cell
from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.queen import Queen
from src.chess.figures.color import Color
from src.chess.error import InconsistentStateError


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

        def turn(schema):
            return position(self.position, schema)

        def non_none(xs):
            return [x for x in xs if x is not None]

        def free_cell(pos):
            return cell(figures, *pos) is None
        
        def opponent_occupied(pos):
            return cell(figures, *pos) is not None and cell(figures, *pos).color != self.color

        moving_turns = turn(turns['short']) if self.touched else turn(turns['long']), turn(turns['short'])
        moving_turns = [pos for pos in non_none(moving_turns) if free_cell(pos)]

        attacking_turns = turn(turns['attack_left']), turn(turns['attack_right'])
        attacking_turns = [move for move in non_none(attacking_turns) if opponent_occupied(move)]

        return set(moving_turns + attacking_turns)

    def transform_to(self, fig_class=Queen):
        if not self.is_transformable_pawn():
            raise InconsistentStateError('transformation error: Pawn not on the boards edge')
    
        return fig_class(self.position, self.color)

    def is_transformable_pawn(self):
        def is_on_the_edge():
            blacks_edge = 8
            whites_edge = 1
            return self.color == Color.WHITE and self.position[1] == blacks_edge or \
                   self.color == Color.BLACK and self.position[1] == whites_edge
        
        return is_on_the_edge()

    def notation(self):
        return 'p'

    def symbol(self):
        return '\u2659' if self.color == Color.WHITE else '\u265F'
            