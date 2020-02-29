""" Print all the odd numbers between 1 and a given integer n"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
for i in range(1, n+1, 2):
    print(i)