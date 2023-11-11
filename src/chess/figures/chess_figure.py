from dataclasses import dataclass
from abc import ABC, abstractmethod
from src.chess.figures.color import Color


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

    def is_out_of_board(self, literal, numeral):
        return literal not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h') or numeral > 8 or numeral <= 0
