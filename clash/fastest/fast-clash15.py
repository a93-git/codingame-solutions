""" Print the average ASCII value of a string"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

t = 0

for i in s:
    t = t + ord(i)
    
print(t//len(s))