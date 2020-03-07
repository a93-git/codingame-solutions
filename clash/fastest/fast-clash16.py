""" To buy - nnn items
ith items cost = i * mmm
has - aaa
borrow - ?
"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

mmm, aaa, nnn = [int(i) for i in input().split()]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
req = sum([i*mmm for i in range(1, nnn+1)])
borrow = req - aaa
if borrow < 0:
    borrow = 0
print(borrow)