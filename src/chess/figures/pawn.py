from src.chess.board_utils import inc_num_pos as up, dec_num_pos as down, dec_lit_pos as left, inc_lit_pos as right, position, cell
from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.queen import Queen
from src.chess.figures.color import Color
from src.chess.error import InconsistentStateError


class Pawn(ChessFigure):

    long_turn = False

    def move(self, to):
        if self.long_turn:
            self.long_turn = False
        if abs(self.position[1] - to[1]) == 2:
            self.long_turn = True
        super(Pawn, self).move(to)

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
        attacking_turns = turn(turns['attack_left']), turn(turns['attack_right'])

        return set(list(filter(free_cell, non_none(moving_turns))) +\
                list(filter(opponent_occupied, non_none(attacking_turns))))

    def has_en_passant(self, figures, to):
        return self.get_en_passant(figures, to) is not None

    # pile of shi~
    def get_en_passant(self, figures, to):
        def is_passant_fig(fig):
            if fig is None or fig.color == self.color or not isinstance(fig, Pawn):
                return False
            return fig.long_turn

        r_passant_pos = position(self.position, [right])
        l_passant_pos = position(self.position, [left])
        right_passant = None
        try:
            right_passant = cell(figures, *r_passant_pos)
        except:
            ...
        left_passant = None
        try:
            left_passant = cell(figures, *l_passant_pos)
        except:
            ...
        def non_none(xs):
            return [x for x in xs if x is not None]

        diff = ord(self.position[0]) - ord(to[0])
        passants = []
        if diff < 0:
            passants.append(right_passant)
        elif diff > 0:
            passants.append(left_passant)

        passants = list(filter(is_passant_fig, non_none(passants)))
        if len(passants) == 2:
            raise InconsistentStateError('cannot exists 2 passants')
        if len(passants) == 0:
            return None
        return passants[0]

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
            