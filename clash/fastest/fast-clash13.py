""" Good teeth - 1, rotten teeth - 0, pulled out teeth - -
Pull out the rotten tooth
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    row = input()
    res = row.replace('0', '-')
    print(res)