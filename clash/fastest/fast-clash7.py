""" Given a string s, morph it into form of string f

e.g s = 'abc', f = 'xX, x', result = 'aB, c'
"""

import sys
import math

s = list(input())
f = list(input())

for i in range(len(f)):
    if f[i] == 'x':
        s[i] = s[i].lower()
    elif f[i] == 'X':
        s[i] = s[i].upper()
    else:
        s.insert(i, f[i])

res = ''.join(s)
print(res)