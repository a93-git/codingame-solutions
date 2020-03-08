""" Find the direction based on current pos and target pos"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    # x2 = light_x, y2 = light_y
    if initial_tx < light_x and initial_ty < light_y:
        print('SE')
        initial_tx += 1
        initial_ty += 1
    elif initial_tx > light_x and initial_ty > light_y:
        print('NW')
        initial_tx -= 1
        initial_ty -= 1
    elif initial_tx > light_x and initial_ty < light_y:
        print('SW')
        initial_tx -= 1
        initial_ty += 1
    elif initial_tx < light_x and initial_ty > light_y:
        print('NW')
        initial_tx += 1
        initial_ty -= 1
    elif initial_tx < light_x and initial_ty == light_y:
        print('E')
        initial_tx += 1
        initial_ty += 0
    elif initial_tx > light_x and initial_ty == light_y:
        print('W')
        initial_tx -= 1
        initial_ty += 0
    elif initial_tx == light_x and initial_ty < light_y:
        print('S')
        initial_tx += 0
        initial_ty += 1
    elif initial_tx == light_x and initial_ty > light_y:
        print('N')
        initial_tx += 0
        initial_ty -= 1