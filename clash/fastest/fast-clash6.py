""" Collatz sequence"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
l = []
l.append(n)
while n != 1:
    if n%2 == 0:
        n = int(n/2)
        l.append(n)
    else:
        n = (3*n) + 1
        l.append(n)
m = [str(x) for x in l]
a = ' '.join(m)
print(a)