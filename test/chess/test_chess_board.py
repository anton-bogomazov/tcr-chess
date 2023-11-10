import unittest
from src.chess.board import increment_literal, decrement_literal


class ChessBoardTest(unittest.TestCase):
    
    def test_util_increment_board_literal(self):
        self.assertEqual(
            'b', increment_literal('a')
        )
        
    def test_util_decrement_board_literal(self):
        self.assertEqual(
            'a', decrement_literal('b')
        )
