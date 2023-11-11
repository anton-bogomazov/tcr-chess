import unittest
from src.chess.figures.bishop import Bishop
from src.chess.figures.queen import Queen
from src.chess.figures.rook import Rook
from src.chess.color import Color


class ChessFiguresTest(unittest.TestCase):

    def test_bishop_possible_turns(self):
        bishop = white_bishop()
        self.assertEqual(len(bishop.turns()), 11)
        self.assertEqual(bishop.turns(), {
            ('a', 1), ('b', 2), ('d', 2), ('e', 1), ('f', 6),
            ('a', 5), ('b', 4), ('d', 4), ('e', 5), ('g', 7), ('h', 8),
        })

    def test_rook_possible_turns(self):
        self.assertEqual(
            white_rook().turns(), {
                ('a', 3), ('c', 1),
                ('b', 3), ('c', 2),
                ('d', 3), ('c', 4),
                ('e', 3), ('c', 5),
                ('f', 3), ('c', 6),
                ('g', 3), ('c', 7),
                ('h', 3), ('c', 8),
            }
        )

    def test_queen_possible_turns_is_a_combination_of_rook_and_bishop_turns(self):
        rook = white_queen()
        self.assertEqual(len(rook.turns()), 25)
        self.assertEqual(rook.turns(), {
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



def white_queen():
    return Queen(('c', 3), Color.WHITE)


def white_bishop():
    return Bishop(('c', 3), Color.WHITE)


def white_rook():
    return Rook(('c', 3), Color.WHITE)


if __name__ == '__main__':
    unittest.main()
    