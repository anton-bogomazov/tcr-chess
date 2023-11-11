import unittest
from src.chess.figures import Color
from src.chess.sets import standard_chess_figure_set as std_set
from src.chess.king import King


class KingTest(unittest.TestCase):
    ...


def white_king():
    return King(('c', 3), Color.WHITE)
