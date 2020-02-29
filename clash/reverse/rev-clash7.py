""" Print the given string in a '*' box

s = 'abc'

output:

*******
* abc *
*******
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
n_star_top = n_star_bottom = len(a) + 4

star_top = '*' * n_star_top
star_bottom = '*' * n_star_bottom

print(star_top)
print("* {0} *".format(a))
print(star_bottom)