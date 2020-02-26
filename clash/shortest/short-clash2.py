""" Lychrel number check"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# rev
def r(n):
    a = 0
    #b = n
    while(n>0):
        a = (a*10) + n%10
        n = n // 10
    return a
    
# check if palindrome
def c(n):
    a = r(n)
    if a == n:
        return True
    else:
        return False

l = [str(n)]

if c(n):
    print(n)
else:
    while(1):
        old_number = n
        reverse = r(n)
        n = old_number + reverse
        l.append(str(n))
        is_pal = c(n)
        if is_pal:
            print(' '.join(l).strip())
            break
            