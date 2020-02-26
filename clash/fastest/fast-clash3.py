""" Get the sum of alphabet values of a string of non-zero length"""

import sys
import math

s = input()

l = list(s)

res = 0
for i in l:
    if ord(i) <= 122 and ord(i) >= 97:
        res = res + (ord(i) - 96)
    elif ord(i) <= 90 and ord(i) >= 65:
        res = res + (ord(i) - 64)
    else:
        res = res + 0

print(res)