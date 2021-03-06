#!/usr/bin/env python3
import numpy as np
from gauss_parser import parse
from validator import validate_type_3

'''
This is an example of what could be done.
You need python 3 due to the print, or maybe just "import from the future" the print statement
'''


A = np.array([[1, 2, 3, 4], [6, 8, 0, 9], [-9, 8, 7, 10]])

rules = [
        'F2 -> F2 - 6 * F1',
        'F3 -> F3 + 9 * F1'
        ]

pm = {'+': lambda a, b: a + b, '-': lambda a, b: a - b}

print ("Matrix")
print (A)

print ("RULES:")

for r in rules:
    st = parse(r)
    
    print (r)

    try:
        validate_type_3(st)
        print ("translation:", st)
    except:
        print ("Invalid rule:", r)
        continue
    
    target = st['target_row']
    pivot = st['pivot_row']

    op = st['op']

    if 'factor' in st.keys():
        factor = st['factor']
        A[target, :] = pm[op](A[target,:], factor * A[pivot, :])

    else:
        A[target, :] = pm[op](A[target, :], A[pivot, :])

    print ("Result:")
    print (A)

