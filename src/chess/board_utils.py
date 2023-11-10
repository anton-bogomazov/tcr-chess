from src.chess.error import InconsistentStateError


literals = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')


def increment_literal(literal):
    if literal not in literals:
        raise InconsistentStateError('literal does not represent position on board')
    if literal == 'h':
        return 'h'
    return chr(ord(literal) + 1)


def decrement_literal(literal):
    if literal not in literals:
        raise InconsistentStateError('literal does not represent position on board')
    if literal == 'a':
        return 'a'
    return chr(ord(literal) - 1)


def increment_numeral(numeral):
    if numeral not in range(1, 9):
        raise InconsistentStateError('numeral does not represent position on board')
    if numeral == 8:
        return 8
    return numeral + 1


def decrement_numeral(numeral):
    if numeral not in range(1, 9):
        raise InconsistentStateError('numeral does not represent position on board')
    if numeral == 1:
        return 1
    return numeral - 1