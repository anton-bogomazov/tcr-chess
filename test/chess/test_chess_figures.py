import unittest
from src.chess.figures import *
from src.chess.figures import Color


class ChessFiguresTest(unittest.TestCase):
    
    def test_white_pawn_possible_turns(self):
        self.assertEqual(
            white_pawn().turns(), {('a', 3), ('a', 4)}
        )

    def test_black_pawn_possible_turns(self):
        self.assertEqual(
            Pawn(('a', 7), Color.BLACK).turns(), {('a', 6), ('a', 5)}
        )

    def test_two_different_pawns_are_not_eq(self):
        self.assertNotEqual(
            Pawn(('a', 2), Color.WHITE),
            Pawn(('a', 2), Color.BLACK)
        )

    def test_pawn_possible_turns_only_short_turn_after_touch(self):
        pawn = white_pawn()
        pawn.move(('a', 3))
        self.assertEqual(
            pawn.turns(), {('a', 4)}
        )

    def test_pawn_move(self):
        pawn = white_pawn()
        pawn.move(('a', 3))
        self.assertEqual(pawn.position, ('a', 3))

    def test_knight_possible_turns(self):
        knight = white_knight()
        self.assertEqual(len(knight.turns()), 8)
        self.assertEqual(knight.turns(), {
            ('b', 1), ('d', 1), ('b', 5), ('d', 5),
            ('a', 2), ('a', 4), ('e', 2), ('e', 4),
        })

    def test_knight_possible_turns_less_moves_on_the_boards_edge(self):
        knight = white_knight(('a', 3))
        self.assertEqual(len(knight.turns()), 4)

    def test_knight_possible_turns_least_possible_turns_in_the_corner(self):
        knight = white_knight(('a', 8))
        self.assertEqual(len(knight.turns()), 2)

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


def white_king():
    return King(('c', 3), Color.WHITE)


def white_queen():
    return Queen(('c', 3), Color.WHITE)


def white_pawn():
    return Pawn(('a', 2), Color.WHITE)


def white_knight(position=('c', 3)):
    return Knight(position, Color.WHITE)


def white_bishop():
    return Bishop(('c', 3), Color.WHITE)


def white_rook():
    return Rook(('c', 3), Color.WHITE)


if __name__ == '__main__':
    unittest.main()
    