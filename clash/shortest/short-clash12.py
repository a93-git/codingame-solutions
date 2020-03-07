""" Find the least number of bits needed for binary representation of a number"""

z,t = input,int
n = t(z())
for i in range(n):
    x = t(z())
    print(len(bin(x)[2:]))
