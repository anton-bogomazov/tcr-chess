import itertools
from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum

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

    def neighbour(self, figures_in_scope, predicate):
        found = list(filter(lambda f: predicate(f), figures_in_scope))
        return None if len(found) == 0 else found[0]

    # Such a shitty code
    def is_same_literal(self, figure):
        return self.position[0] == figure.position[0]
    
    def is_same_numeral(self, figure):
        return self.position[1] == figure.position[1]
    
    def closest_left(self, figures_in_scope):
        return self.neighbour(figures_in_scope, lambda f: self.is_same_numeral(f) and self.position[0] > f.position[0])

    def closest_right(self, figures_in_scope):
        return self.neighbour(figures_in_scope, lambda f: self.is_same_numeral(f) and self.position[0] < f.position[0])

    def closest_top(self, figures_in_scope):
        return self.neighbour(figures_in_scope, lambda f: self.is_same_literal(f) and self.position[1] < f.position[1])

    def closest_bottom(self, figures_in_scope):
        return self.neighbour(figures_in_scope, lambda f: self.is_same_literal(f) and self.position[1] > f.position[1])

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
    def turns(self):
        literal, numeral = self.position
        short_diff = 1
        long_diff = 2

        if self.color == Color.BLACK:
            short_diff = -1
            long_diff = -2
        
        short_turn = (literal, numeral + short_diff)
        long_turn = (literal, numeral + long_diff)
        return {short_turn} if self.touched else {short_turn, long_turn}

    def notation(self):
        return 'p'

    def symbol(self):
        return '\u2659' if self.color == Color.WHITE else '\u265F'
    