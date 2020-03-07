""" Print the input char in between equal number of '*'s """

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

c = input()
l = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
if l %2 == 0:
    print('CAN\'T')
else:
    print('*' * (l//2) + c + '*' * (l//2))
