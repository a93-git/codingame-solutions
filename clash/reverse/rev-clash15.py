""" Stupid question"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n_1, n_2 = input().split()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
res = ''
for i,j in zip(n_1, n_2):
    if i == j and i == '0':
        res = res + '0'
    elif i == j and i == '1':
        res =res + '1'
    elif i == '1' or j == '1':
        res = res + '1'
    else:
        res = res + '0'
print(res)