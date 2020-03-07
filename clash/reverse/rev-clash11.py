""" Print the sum of ascii values of characters in a word

Print separate line for each space separated word
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

line = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
for i in line.split():
    print(sum([ord(x) for x in i]))