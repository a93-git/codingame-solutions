""" Print a triangle of n with n-rows
n = 3
3
33
333

n = 4
4
44
444
4444
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

for i in range(1,n+1):
    s = ''
    for j in range(i):
        s = s + str(n)
    print(s)