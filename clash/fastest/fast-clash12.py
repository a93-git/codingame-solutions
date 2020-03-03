""" X men, each man has X wives, each wife has X kids

What is the total population?
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(x + (x**2) + (x**3))