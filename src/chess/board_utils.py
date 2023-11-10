from src.chess.error import InconsistentStateError, OutOfBoardError
from functools import reduce


literals = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')


def increment_literal(literal):
    if literal not in literals:
        raise InconsistentStateError('literal does not represent position on board')
    if literal == 'h':
        raise OutOfBoardError()
    return chr(ord(literal) + 1)


def decrement_literal(literal):
    if literal not in literals:
        raise InconsistentStateError('literal does not represent position on board')
    if literal == 'a':
        raise OutOfBoardError()
    return chr(ord(literal) - 1)


def increment_numeral(numeral):
    if numeral not in range(1, 9):
        raise InconsistentStateError('numeral does not represent position on board')
    if numeral == 8:
        raise OutOfBoardError()
    return numeral + 1


def decrement_numeral(numeral):
    if numeral not in range(1, 9):
        raise InconsistentStateError('numeral does not represent position on board')
    if numeral == 1:
        raise OutOfBoardError()
    return numeral - 1


def dec_lit_pos(position):
    l, n = position
    return (decrement_literal(l), n)


def inc_lit_pos(position):
    l, n = position
    return (increment_literal(l), n)


def dec_num_pos(position):
    l, n = position
    return (l, decrement_numeral(n))


def inc_num_pos(position):
    l, n = position
    return (l, increment_numeral(n))
 
 
def cell(figures, literal, numeral):
    found_figures = [fig for fig in figures if fig.position == (literal, numeral)]
    match len(found_figures):
        case 0:
            return None
        case 1:
            return found_figures[0]
        case _:
            raise InconsistentStateError('two figures in the same cell')


def position(fig_pos, moves):
    try:
        return reduce(lambda acc, f: f(acc), moves, fig_pos)
    except OutOfBoardError:
        return None
