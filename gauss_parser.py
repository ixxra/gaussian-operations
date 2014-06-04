import re
'''
gauss_parser.py

parses instructions in gaussian elimination of the form

F2 -> F2 + 3 * F1

see "parser" for a more detailed explanation.

TODO: parse Row exchanges and Rows rescaling.
'''

class SyntaxError(Exception):
    pass


ROW = r'F(\d+)'

SPACE_MAYBE = r'\s*'

OP = r'([+-])'

ADITION = ROW + SPACE_MAYBE + OP + SPACE_MAYBE + r'(.+)'

NUMBER = r'(\d*\.?\d+)'

PRODUCT = NUMBER + SPACE_MAYBE + r'\*' + SPACE_MAYBE + ROW



def parse(command):
    '''
    parse(command) - parses a gaussian elimination command

    command must be something of the form

    F2 -> F2 + 3 * F1

    that is, transform Row number 2 into the result of adding three times Row number 1 to Row Number 2.

    returns a dictionary with the parsed instructions. 
    With the above example, it would be formated like this:

        {
            'target_row': 1, 
            'op': '+',
            'added_row': 1,
            'pivot_row': 0,
            factor: 3.0
        }

    where:
        
        target_row: row number to substitute in gaussian elimination
        op: either '+' or '-'
        added_row: Represents the first summand. In gaussian elimination, this should be equal to the target_row.
        pivot_row: The second summand. In gaussian elimination this is the row containing the pivot element.
        factor: The factor proportion of the pivot row. This is always a positive number, or None in situations like this:

            F2 -> F2 + F1
    '''
    try:
        lhs, rhs = map(lambda s: s.strip(), command.split('->'))
        
    except:
        raise SyntaxError()

    target = re.match(ROW, lhs) 

    if target is None:
        raise SyntaxError()
    
    target_row = int(target.group()[1:]) - 1
    
    try:
        row1, op, row2 = re.match(ADITION, rhs).groups()
        added_row = int(row1) - 1

    except:
        raise SyntaxError()


    try:
        number, row3 = re.match(PRODUCT, row2).groups()
        factor = float(number)
        pivot_row = int(row3) - 1

    except:
        try:
            row3, = re.match(ROW, row2).groups()
            factor = None
            pivot_row = int(row3) - 1
        except:
            raise SyntaxError()
    
    parsed_command = {
            'target_row': target_row, 
            'op': op,
            'added_row': added_row,
            'pivot_row': pivot_row,
    }

    if factor is not None:
        parsed_command['factor'] = factor

    return parsed_command

if __name__ == '__main__':
    command = 'F4 -> F4 + 2 * F3'
    print ('You see:')
    print (command)
    print ('I see:')
    print (parse(command))
