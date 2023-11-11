import unittest
from src.chess.figures.rook import Rook
from src.chess.figures.color import Color


class RookTest(unittest.TestCase):
    
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
        
    def test_can_take_only_first_encouneterd_opponent(self):
        sut = _rook(('a', 1), Color.BLACK)
        figures = [
            sut,
            _rook(('a', 4)),
            _rook(('a', 6)),
        ]
        self.assertEqual({
            ('a', 2), ('a', 3), ('a', 4),
            ('b', 1),
            ('c', 1),
            ('d', 1),
            ('e', 1),
            ('f', 1),
            ('g', 1),
            ('h', 1),
        }, sut.turns(figures))


def _rook(position=('c', 3), color=Color.WHITE):
    return Rook(position, color)
