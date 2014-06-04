from gauss_parser import parse

class TargetException(Exception):
    pass


class FactorException(Exception):
    pass


class OperationException(Exception):
    pass


def validate_type_3(structure):
    op = structure['op']
    target_row = structure['target_row']
    added_row = structure['added_row']
    pivot_row = structure['pivot_row']

    if 'factor' in structure.keys():
        factor = structure['factor']
        if type(factor) != float:
            raise FactorException("Factor type is not float")

    if target_row != added_row:
        raise TargetException("Type 3 operation target row mismatch")

    if op not in ('+', '-'):
        raise OperationError("Rows can only be added, rested")
