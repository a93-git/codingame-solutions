""" Find the average of given numbers"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = []
for i in input().split():
    x = int(i)
    a.append(x)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

res = sum(a)/len(a)
if str(res).split('.')[-1] != '0':
    print(res)
else:
    print(int(res))