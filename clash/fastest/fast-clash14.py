""" Print n terms of a geometric series with common ratio r and first term 1"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, r = [int(i) for i in input().split()]
res = '1'
j = 1
for i in range(n-1):
    res = res + ' ' + str((j*r))
    j = j*r
print(res.strip())