import unittest
from src.chess.figures import Color
from src.chess.sets import standard_chess_figure_set as std_set
from src.chess.king import King


class KingTest(unittest.TestCase):
    
    def test_king_possible_turns(self):
        king = _king()
        self.assertEqual(len(king.turns()), 8)
        self.assertEqual(king.turns(), {
            ('b', 3), ('c', 2), ('b', 2), ('d', 4),
            ('d', 3), ('c', 4), ('d', 2), ('b', 4)
        })


def _king(position=('c', 3), color=Color.WHITE):
    return King(position, color)
