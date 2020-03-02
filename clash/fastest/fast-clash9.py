""" Print a phone number in the format of (xxx) xxx-xxxx"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
def phone(s):
    res = ''
    res = res + '({0})'.format(s[:3])
    res = res + ' {0}'.format(s[3:6])
    res = res + '-{0}'.format(s[6:])
    return res
print(phone(s))