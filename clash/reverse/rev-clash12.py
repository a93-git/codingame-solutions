""" Unscramble the line

Pnioge == Pigeon
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

scrambled = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

res = ''
for i in range(0, len(scrambled), 2):
    res = res + scrambled[i]
if len(scrambled) %2 == 0:
    for i in range(len(scrambled)-1, 0, -2):
        res = res + scrambled[i]
else:
    for i in range(len(scrambled)-2, 0, -2):
        res = res + scrambled[i]
print(res)