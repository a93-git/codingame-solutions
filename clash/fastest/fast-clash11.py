""" Print a string with the difference and sum of two given numbers concatenated"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a, b = [int(i) for i in input().split()]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(str(a-b)+str(a+b))