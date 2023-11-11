import unittest
from src.chess.figures.knight import Knight
from src.chess.figures.pawn import Pawn
from src.chess.figures.color import Color
from src.chess.figures.sets import standard_chess_figure_set as std_set


class KnightTest(unittest.TestCase):
    
    def test_knight_possible_turns(self):
        sut = _knight()
        
        self.assertEqual(sut.turns([]), {
            ('b', 1), ('d', 1), ('b', 5), ('d', 5),
            ('a', 2), ('a', 4), ('e', 2), ('e', 4),
        })

    def test_knight_possible_turns_blocked_by_allies(self):
        sut = _knight(('g', 1))

        self.assertEqual(sut.turns(std_set()), {
            ('f', 3), ('h', 3),
        })

    def test_knight_possible_turns_attack_foe(self):
        sut = _knight(('h', 6))

        self.assertEqual(sut.turns(std_set()), {
            ('g', 4), ('f', 5), ('g', 8), ('f', 7),
        })

    def test_knight_possible_turns_less_moves_on_the_boards_edge(self):
        sut = _knight(('a', 3))
        
        self.assertEqual({
            ('b', 1), ('b', 5),
            ('c', 2), ('c', 4),
        }, sut.turns([]))

    def test_knight_possible_turns_least_possible_turns_in_the_corner(self):
        sut = _knight(('a', 8))
        
        self.assertEqual({
            ('b', 6), ('c', 7),
        }, sut.turns([]))
        
    def test_knight_can_jump_over_figures(self):
        sut = _knight(('e', 4))
        
        figures = [
            Pawn(('d', 5), Color.BLACK),
            sut
        ]
        self.assertEqual(8, len(sut.turns(figures)))
    

def _knight(position=('c', 3), color=Color.WHITE):
    return Knight(position, color)
