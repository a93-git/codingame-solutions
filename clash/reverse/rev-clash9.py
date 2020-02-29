""" Print the square of the sum of the digits of a number"""

number = int(input())
n = 0
while number > 0:
    n = n + number % 10
    number = number // 10

print(n**2)