""" Convert milliseconds to 0d 0h 0m 0s format"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

d = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
days = 86400000
h = 3600000
m = 60000
s = 1000
a = ''
if d == 0:
    a = '0s'
else:
    _days = d // days
    if _days != 0:
        d = d%days
        a = a + str(_days) + 'd '
    _h = d // h
    if _h != 0:
        d = d%h
        a = a + str(_h) + 'h '
    _m = d // m
    if _m != 0:
        d = d%m
        a = a + str(_m) + 'm '
    _s = d // s
    if _s != 0:
        a = a + str(_s) + 's'

a = a.rstrip()
        
print(a)