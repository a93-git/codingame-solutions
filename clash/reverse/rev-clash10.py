""" If any one bit in the corresponding bits of two given binary numbers is 1, set that bit to 1, else 0

00101
10100
------
10101
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

t = input()
t2 = input()

print(t, t2, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
res = ''
for i in range(len(t)):
    if t[i] == '1' or t2[i] == '1':
        res = res + '1'
    else:
        res = res + '0'
print(res)