import unittest
from src.chess.figures.king import King
from src.chess.figures.pawn import Pawn
from src.chess.figures.color import Color
from src.chess.figures.sets import standard_chess_figure_set as std_figures


class PawnTest(unittest.TestCase):
    
    def test_white_pawn_possible_turns(self):
        self.assertEqual(
            _pawn().turns(std_figures()),
            {('a', 3), ('a', 4)}
        )

    def test_black_pawn_possible_turns(self):
        self.assertEqual(
            _pawn(('a', 7), Color.BLACK).turns(std_figures()),
            {('a', 6), ('a', 5)}
        )

    def test_only_attacking_turn(self):
        sut = _pawn(('e', 4))
        sut.touched = True
        figures = [
            sut,
            _pawn(('e', 5)), # friendly block
            _pawn(('d', 5), Color.BLACK),
            King(('f', 5), Color.BLACK),
        ]
        self.assertEqual({('f', 5), ('d', 5)}, sut.turns(figures))

    def test_two_different_pawns_are_not_eq(self):
        self.assertNotEqual(
            _pawn(('a', 2), Color.WHITE),
            _pawn(('a', 2), Color.BLACK)
        )

    def test_pawn_possible_turns_only_short_turn_after_touch(self):
        pawn = _pawn()
        pawn.move(('a', 3))
        self.assertEqual(
            pawn.turns([]), {('a', 4)}
        )

    def test_pawn_move(self):
        pawn = _pawn()
        pawn.move(('a', 3))
        self.assertEqual(pawn.position, ('a', 3))


def _pawn(position=('a', 2), color=Color.WHITE):
    return Pawn(position, color)
