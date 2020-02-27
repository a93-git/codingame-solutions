""" Swap char at position i with char at position i+1, if it exists"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

print(s, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
_s = ''
for i in range(0, len(s), 2):
    if i+1 <= len(s) - 1:
       _s = _s + s[i+1] + s[i]
    else:
        _s = _s + s[i]

print(_s)