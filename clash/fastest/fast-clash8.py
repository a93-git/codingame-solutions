""" Give a string with XOR value for the given binary input"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n_1, n_2 = input().split()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

res = ''

for i in range(len(n_1)):
    res = res + str(int(n_1[i]) ^ int(n_2[i]))
print(res)