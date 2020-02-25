import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = int(input())
n = int(input())

res = 1
for i in range(n):
    if x > 0:
        res = res * x
    x = x - 1 
    
print(res)