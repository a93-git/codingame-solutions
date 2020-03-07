""" Remove digits from a string"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
a = ['0','1','2','3','4','5','6','7','8','9']

for i in a:
    s = s.replace(i, '')
    
print(s)