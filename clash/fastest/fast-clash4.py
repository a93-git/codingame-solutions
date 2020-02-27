""" A number in string format is given, if the length of given numbere is not divisible by 3, print 'ERROR'
else, print the string formed by char representation of 3 digit partitions (from ASCII)

Remove the 0 padding from left
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

code = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
b = []

if len(code)%3 != 0:
    b.append('ERROR')
else:
    for i in range(len(code)):
        a = code[:3]
        code = code[3:]
        a = a.lstrip('0')
        try:
            b.append(str(chr(int(a))))
        except:
            pass

d = ''.join(b)
print(d)