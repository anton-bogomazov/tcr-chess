import unittest
from src.chess.board import increment_literal, decrement_literal, \
        increment_numeral, decrement_numeral
from src.chess.error import InconsistentStateError


class ChessBoardTest(unittest.TestCase):
    
    def test_util_increment_board_literal(self):
        self.assertEqual(
            'b', increment_literal('a')
        )
        
    def test_error_with_not_board_literal(self):
        with self.assertRaises(InconsistentStateError):
            increment_literal('i')

    def test_util_increment_board_literal_do_nothing_if_out_of_bounds(self):
        self.assertEqual(
            'h', increment_literal('h')
        )

    def test_util_decrement_board_literal(self):
        self.assertEqual(
            'a', decrement_literal('b')
        )

    def test_util_decrement_board_literal_do_nothing_if_out_of_bounds(self):
        self.assertEqual(
            'a', decrement_literal('a')
        )

    def test_util_increment_board_numeral(self):
        self.assertEqual(
            2, increment_numeral(1)
        )

    def test_util_increment_board_numeral_do_nothing_if_out_of_bounds(self):
        self.assertEqual(
            8, increment_numeral(8)
        )

    def test_util_decrement_board_numeral(self):
        self.assertEqual(
            2, decrement_numeral(3)
        )

    def test_util_decrement_board_numeral_do_nothing_if_out_of_bounds(self):
        self.assertEqual(
            1, decrement_numeral(1)
        )

    def test_error_with_not_board_numeral(self):
        with self.assertRaises(InconsistentStateError):
            decrement_numeral(9)

