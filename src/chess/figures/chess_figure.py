from dataclasses import dataclass
from abc import ABC, abstractmethod
from src.chess.figures.color import Color
from src.chess.board_utils import cell, position


@dataclass
class ChessFigure(ABC):
    position: tuple
    color: Color
    touched = False

    @abstractmethod
    def turns(self, figures):
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

    def calc_moves(self, figures, m):
        result = []
        cur_position = position(self.position, m)
        while cur_position is not None:
            if cell(figures, *cur_position) is None:
                result.append(cur_position)
                cur_position = position(cur_position, m)
            elif cell(figures, *cur_position).color != self.color:
                result.append(cur_position)
                break
            else: # blocked by ally
                break
        return result

    def calc_singly_moves(self, figures, ms):
        def calc_move(m):
            cur_position = position(self.position, m)
            if cur_position is None:
                return None
    
            if cell(figures, *cur_position) is None or \
               cell(figures, *cur_position).color != self.color:
                return cur_position
    
            return None
        
        return [m for m in [calc_move(m) for m in ms] if m is not None]

    def is_transformable_pawn(self):
        return False
