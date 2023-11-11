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
        return result

    def is_out_of_board(self, literal, numeral):
        return literal not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h') or numeral > 8 or numeral <= 0
