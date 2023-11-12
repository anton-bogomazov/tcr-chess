import unittest
from src.chess.figures.color import Color
from src.chess.figures.king import King
from src.chess.figures.pawn import Pawn


class KingTest(unittest.TestCase):
    
    def test_king_possible_turns(self):
        king = _king()

        self.assertEqual(king.turns([]), {
            ('b', 3), ('c', 2), ('b', 2), ('d', 4),
            ('d', 3), ('c', 4), ('d', 2), ('b', 4)
        })

    def test_can_be_blocked(self):
        king = _king()

        figs = [
            king,
            Pawn(('c', 4), Color.WHITE),
            Pawn(('c', 2), Color.BLACK),
        ]
        self.assertEqual({
            ('b', 3), ('c', 2), ('b', 2), ('d', 4),
            ('d', 3), ('d', 2), ('b', 4)
        }, king.turns(figs))


def _king(position=('c', 3), color=Color.WHITE):
    return King(position, color)
