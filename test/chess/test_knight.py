import unittest
from src.chess.knight import Knight
from src.chess.pawn import Pawn
from src.chess.figures import Color
from src.chess.sets import standard_chess_figure_set as std_figures


class KnightTest(unittest.TestCase):
    
    def test_knight_possible_turns(self):
        sut = _knight()
        
        self.assertEqual(sut.turns(std_figures()), {
            ('b', 1), ('d', 1), ('b', 5), ('d', 5),
            ('a', 2), ('a', 4), ('e', 2), ('e', 4),
        })

    def test_knight_possible_turns_less_moves_on_the_boards_edge(self):
        sut = _knight(('a', 3))
        
        self.assertEqual(len(sut.turns(std_figures())), 4)

    def test_knight_possible_turns_least_possible_turns_in_the_corner(self):
        sut = _knight(('a', 8))
        
        self.assertEqual(len(sut.turns(std_figures())), 2)
        
    def test_knight_can_jump_over_figures(self):
        sut = _knight(('e', 4))
        
        figures = [
            Pawn(('d', 5), Color.BLACK),
            sut
        ]
        self.assertEqual(len(sut.turns(figures)), len(sut.turns(figures)))
    

def _knight(position=('c', 3), color=Color.WHITE):
    return Knight(position, color)
