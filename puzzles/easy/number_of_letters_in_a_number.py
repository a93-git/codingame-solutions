import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

start, n = [int(i) for i in input().split()]
_temp = 0
for i in range(1,n+1):
    res = 0
    b_r = bin(start)[2:]
    n_0, n_1 = b_r.count('0')*4, b_r.count('1')*3
    res = n_0 + n_1
    start = res
    if _temp == start:
        break
    else:
        _temp = start
print(start)