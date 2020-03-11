""" Print the count of numbers which fall in each category from numbers within an inclusive given range"""

a, b = [int(i) for i in input().split()]
s, e = [int(i) for i in input().split()]

c1, c2, c3, c4 = 0,0,0,0
for i in range(s, e+1):
    if i % a == 0 and i % b != 0:
        c1 += 1
    elif i%a != 0 and i % b == 0:
        c2 += 1
    elif i % a == 0 and i %b == 0:
        c3 += 1
    else:
        c4 += 1

print("{0} {1} {2} {3}".format(c1, c2, c3, c4))