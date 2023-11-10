import itertools
from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum
from src.chess.board_utils import inc_num_pos, dec_num_pos, dec_lit_pos, inc_lit_pos, cell
from functools import reduce

# figures can be blocked by other figures. restrict it
# Modify move method


class Color(Enum):
    WHITE = 1,
    BLACK = 2
    
    
@dataclass
class ChessFigure(ABC):
    position: tuple
    color: Color
    touched = False

    @abstractmethod
    def turns(self):
        raise NotImplementedError

    @abstractmethod
    def notation(self):
        raise NotImplementedError

    @abstractmethod
    def symbol(self):
        raise NotImplementedError

    def move(self, to):
        self.position = to
        self.touched = True

    def is_out_of_board(self, literal, numeral):
        return literal not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h') or numeral > 8 or numeral <= 0


class King(ChessFigure):
    def turns(self):
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


class Queen(ChessFigure):
    def turns(self):
        literal, numeral = self.position
        rook_turns = [(chr(ord(literal) - i), numeral) for i in range(1, 8)] +\
                     [(chr(ord(literal) + i), numeral) for i in range(1, 8)] +\
                     [(chr(ord(literal)), numeral + i) for i in range(1, 8)] +\
                     [(chr(ord(literal)), numeral - i) for i in range(1, 8)]
        bishop_turns = [(chr(ord(literal) - i), numeral - i) for i in range(1, 8)] +\
                       [(chr(ord(literal) + i), numeral + i) for i in range(1, 8)] +\
                       [(chr(ord(literal) - i), numeral + i) for i in range(1, 8)] +\
                       [(chr(ord(literal) + i), numeral - i) for i in range(1, 8)]

        return set(filter(lambda t: not self.is_out_of_board(*t), rook_turns + bishop_turns)) - {self.position}

    def notation(self):
        return 'Q'

    def symbol(self):
        return '\u2655' if self.color == Color.WHITE else '\u265B'


class Rook(ChessFigure):

    def neighbours(self, figures_in_scope, predicate):
        return list(filter(lambda f: predicate(f), figures_in_scope))

    # Such a shitty code
    def is_same_literal(self, figure):
        return self.position[0] == figure.position[0]
    
    def is_same_numeral(self, figure):
        return self.position[1] == figure.position[1]
    
    def closest_left(self, figures_in_scope):
        neighbours_on_left = self.neighbours(figures_in_scope, lambda f: self.is_same_numeral(f) and self.position[0] > f.position[0])
        return None if len(neighbours_on_left) == 0 else sorted(neighbours_on_left, key=lambda x: x.position[0], reverse=True)[0]

    def closest_right(self, figures_in_scope):
        neighbours_on_right = self.neighbours(figures_in_scope, lambda f: self.is_same_numeral(f) and self.position[0] < f.position[0])
        return None if len(neighbours_on_right) == 0 else sorted(neighbours_on_right, key=lambda x: x.position[0])[0]

    def closest_top(self, figures_in_scope):
        neighbours_on_top = self.neighbours(figures_in_scope, lambda f: self.is_same_literal(f) and self.position[1] < f.position[1])
        return None if len(neighbours_on_top) == 0 else sorted(neighbours_on_top, key=lambda x: x.position[1])[0]

    def closest_bottom(self, figures_in_scope):
        neighbours_on_bottom = self.neighbours(figures_in_scope, lambda f: self.is_same_literal(f) and self.position[1] > f.position[1])
        return None if len(neighbours_on_bottom) == 0 else sorted(neighbours_on_bottom, key=lambda x: x.position[1], reverse=True)[0]
    
    def is_figure_takeable(self, figure):
        return not isinstance(figure, King) and figure.color != self.color
        
    def possible_moves(self, figures):
        figures_in_scope = list(filter(lambda f: f.position in list(self.turns()), figures))
        closest_top = self.closest_top(figures_in_scope)
        closest_bottom = self.closest_bottom(figures_in_scope)
        closest_left = self.closest_left(figures_in_scope)
        closest_right = self.closest_right(figures_in_scope)

        def is_not_blocked(turn):
            top = closest_top is None or turn[1] < closest_top.position[1]
            bottom = closest_bottom is None or turn[1] > closest_bottom.position[1]
            right = closest_right is None or turn[0] < closest_right.position[0]
            left = closest_left is None or turn[0] > closest_left.position[0]
            return top and bottom and right and left

        closest_figs = [closest_top, closest_bottom, closest_left, closest_right]
        closest_figs = [f for f in closest_figs if f is not None]
        takeable = filter(self.is_figure_takeable, closest_figs)

        return set(itertools.chain(filter(is_not_blocked, self.turns()),
                            map(lambda f: f.position, takeable)))
    
    def turns(self):
        literal, numeral = self.position
        turns = [(chr(ord(literal) - i), numeral) for i in range(1, 8)] +\
                [(chr(ord(literal) + i), numeral) for i in range(1, 8)] +\
                [(chr(ord(literal)), numeral + i) for i in range(1, 8)] +\
                [(chr(ord(literal)), numeral - i) for i in range(1, 8)]

        return set(filter(lambda t: not self.is_out_of_board(*t), turns)) - {self.position}

    def castle(self, kings_to):
        self.position = self.rook_castling_to(kings_to)
        self.touched = True
        
    def rook_castling_to(self, to):
        if to == ('g', 1):
            return ('f', 1)
        if to == ('c', 1):
            return ('d', 1)
        if to == ('g', 8):
            return ('f', 8)
        if to == ('c', 8):
            return ('d', 8)

    def notation(self):
        return 'R'

    def symbol(self):
        return '\u2656' if self.color == Color.WHITE else '\u265C'


class Bishop(ChessFigure):
    def turns(self):
        literal, numeral = self.position
        turns = [(chr(ord(literal) - i), numeral - i) for i in range(1, 8)] +\
                [(chr(ord(literal) + i), numeral + i) for i in range(1, 8)] +\
                [(chr(ord(literal) - i), numeral + i) for i in range(1, 8)] +\
                [(chr(ord(literal) + i), numeral - i) for i in range(1, 8)]

        return set(filter(lambda t: not self.is_out_of_board(*t), turns)) - {self.position}

    def notation(self):
        return 'B'

    def symbol(self):
        return '\u2657' if self.color == Color.WHITE else '\u265D'


class Knight(ChessFigure):

    def possible_moves(self, figures):
        return self.turns()
        
    def turns(self):
        literal, numeral = self.position
        turns = [
            (chr(ord(literal) - 2), numeral - 1),
            (chr(ord(literal) - 2), numeral + 1),
            (chr(ord(literal) + 2), numeral - 1),
            (chr(ord(literal) + 2), numeral + 1),
            (chr(ord(literal) - 1), numeral - 2),
            (chr(ord(literal) - 1), numeral + 2),
            (chr(ord(literal) + 1), numeral - 2),
            (chr(ord(literal) + 1), numeral + 2),
        ]
        return set(filter(lambda t: not self.is_out_of_board(*t), turns))

    def notation(self):
        return 'N'

    def symbol(self):
        return '\u2658' if self.color == Color.WHITE else '\u265E'


class Pawn(ChessFigure):
    def turns(self, figures=''):
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

        def position(moves):
            result = self.position
            for move in moves:
                result = move(result)
            return result

        moving_turns = {position(turns['short'])} if self.touched \
                       else {position(turns['long']), position(turns['short'])}
        moving_turns = [move for move in moving_turns if cell(figures, *move) is None]

        attacking_turns = {position(turns['attack_left']), position(turns['attack_right'])}
        attacking_turns = [move for move in attacking_turns
                           if cell(figures, *move) is not None and
                              cell(figures, *move).color != self.color]

        return set(moving_turns + attacking_turns)

    def notation(self):
        return 'p'

    def symbol(self):
        return '\u2659' if self.color == Color.WHITE else '\u265F'
    