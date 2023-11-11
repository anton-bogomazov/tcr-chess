import unittest
from src.chess.figures.color import Color
from src.chess.figures.queen import Queen


class QueenTest(unittest.TestCase):
    
    def test_queen_possible_turns_is_a_combination_of_rook_and_bishop_turns(self):
        rook = _queen()
        self.assertEqual(rook.turns([]), {
            ('a', 3), ('c', 1),
            ('b', 3), ('c', 2),
            ('d', 3), ('c', 4),
            ('e', 3), ('c', 5),
            ('f', 3), ('c', 6),
            ('g', 3), ('c', 7),
            ('h', 3), ('c', 8),
        }.union(
            {
                ('a', 1), ('b', 2), ('d', 2), ('e', 1), ('f', 6),
                ('a', 5), ('b', 4), ('d', 4), ('e', 5), ('g', 7), ('h', 8),
            }
        ))



def _queen(position=('c', 3), color=Color.WHITE):
    return Queen(position, color)
