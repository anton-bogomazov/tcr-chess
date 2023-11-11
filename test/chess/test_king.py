import unittest
from src.chess.figures import Color
from src.chess.sets import standard_chess_figure_set as std_set
from src.chess.king import King
from src.chess.pawn import Pawn


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

    @unittest.skip('probably should be managed on upper level')
    def test_cant_move_to_attacked_cell(self):
        king = _king()

        figs = [
            king,
            _king(('c', 5)),
            _king(('d', 1)),
        ]
        self.assertEqual({
            ('b', 2), ('b', 3), ('d', 3),
        }, king.turns(figs))


def _king(position=('c', 3), color=Color.WHITE):
    return King(position, color)