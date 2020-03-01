""" Print the temperature closest to 0.

In case of two numbers being equally close to 0, print the positive one"""


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = []
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    temps.append(t)

print(temps, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
ret = []
for i in temps:
    ret.append(abs(0-i))

print(ret, file=sys.stderr)

try:
    if ret.count(min(ret)) > 1:
        _a = []
        _min = temps[ret.index(min(ret))]
        for i in range(len(ret)):
            if abs(_min) == abs(temps[i]):
               _a.append(i)
        print(_a, file=sys.stderr)
        print(max([temps[x] for x in _a]))
    else:
        print(temps[ret.index(min(ret))])
except:
    print(0)