import unittest
from src.chess.figures import *
from src.chess.figures import Color


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

    def test_king_possible_turns(self):
        king = white_king()
        self.assertEqual(len(king.turns()), 8)
        self.assertEqual(king.turns(), {
            ('b', 3), ('c', 2), ('b', 2), ('d', 4),
            ('d', 3), ('c', 4), ('d', 2), ('b', 4)
        })



def white_queen():
    return Queen(('c', 3), Color.WHITE)


def white_bishop():
    return Bishop(('c', 3), Color.WHITE)


def white_rook():
    return Rook(('c', 3), Color.WHITE)


if __name__ == '__main__':
    unittest.main()
    