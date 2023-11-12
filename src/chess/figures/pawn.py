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

    def transform_to(self, fig_class=Queen):
        blacks_edge = 8
        whites_edge = 1

        if self.color == Color.WHITE and self.position[1] != blacks_edge:
            raise InconsistentStateError('transformation error: Pawn not on the boards edge')
        elif self.color == Color.BLACK and self.position[1] != whites_edge:
            raise InconsistentStateError('transformation error: Pawn not on the boards edge')
        
        return fig_class(self.position, self.color)

    def is_transformable_pawn(self):
        return self.is_on_the_edge()
    
    def is_on_the_edge(self):
        blacks_edge = 8
        whites_edge = 1
    
        return self.color == Color.WHITE and self.position[1] == blacks_edge or \
               self.color == Color.BLACK and self.position[1] == whites_edge

    def notation(self):
        return 'p'

    def symbol(self):
        return '\u2659' if self.color == Color.WHITE else '\u265F'
            