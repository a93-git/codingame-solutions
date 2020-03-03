""" Print the third angle of a triangle given two angles"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a, b = [int(i) for i in input().split()]

print(180-(a+b))