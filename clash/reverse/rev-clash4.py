""" Given a number, if the last digit is not 0, print the remainder of the number divided by the last digit

if the last digit is 0, print the number by removing the first digit"""


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

a = n % 10

if a == 0:
    print(n % (10 ** (len(str(n))-1)))
else:
    print(int(n/a))
