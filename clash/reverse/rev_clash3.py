""" Calculate an arithmetic expression of the form (xN +- y = z) and give the value of 'N'

In case of float result, return ceil value"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

e = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

lhs = e.split('=')[0]
rhs = e.split('=')[1]

if '+' in lhs:
    _lhs1 = lhs.split('+')[0]
    _lhs2 = lhs.split('+')[1]
    if _lhs1.strip('N') == '':
        _lhs1 = 1
        _rhs = (int(rhs) - int(_lhs2)) / _lhs1
    else:
        _rhs = (int(rhs) - int(_lhs2)) / int(_lhs1.strip('N'))
    print(math.ceil(_rhs))
else:
    _lhs1 = lhs.split('-')[0]
    _lhs2 = lhs.split('-')[1]
    if _lhs1.strip('N') == '':
        _lhs1 = 1
        _rhs = (int(rhs) + int(_lhs2)) / _lhs1
    else:
        _rhs = (int(rhs) + int(_lhs2)) / int(_lhs1.strip('N'))
    print(math.ceil(_rhs))
