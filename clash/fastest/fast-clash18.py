""" Print 'false' if 0 in binary representation of the number else print 'true'"""
n = int(input())

if '0' in bin(n)[2:]:
    print('false')
else:
    print('true')
