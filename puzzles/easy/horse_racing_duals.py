""" Find the min differences between two numbers for the given number set"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
_min = 0
p = []
for i in range(n):
    pi = int(input())
    p.append(pi)
p.sort()
curr_val = p[0]
prev_val = p[1]
old_diff = abs(prev_val - curr_val)
for i in p[2:]:
    curr_val = i
    new_diff = abs(curr_val - prev_val)
    if old_diff > new_diff:
        old_diff = new_diff
    prev_val = curr_val
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(old_diff)