"""Given a number you must multiply it by itself and all numbers below it and return the total sum of each multiplication."""

n = int(input())
print(sum([n*x for x in range(1,n+1)]))