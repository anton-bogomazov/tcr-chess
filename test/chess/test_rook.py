import unittest
from src.chess.figures.rook import Rook
from src.chess.figures.color import Color


class PawnTest(unittest.TestCase):
    
    def test_rook_possible_turns(self):
        self.assertEqual(
            _rook().turns([]), {
                ('a', 3), ('c', 1),
                ('b', 3), ('c', 2),
                ('d', 3), ('c', 4),
                ('e', 3), ('c', 5),
                ('f', 3), ('c', 6),
                ('g', 3), ('c', 7),
                ('h', 3), ('c', 8),
            }
        )
        

def _rook():
    return Rook(('c', 3), Color.WHITE)
