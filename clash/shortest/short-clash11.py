""" Find the difference between sum of digits at odd and even pos"""

s=str
n,r,l,i,w = s(input()),range,len,int,sum
o = r(0, l(s(n)), 2)
e = r(1, l(s(n)), 2)
p = w([i(s(n)[x]) for x in o])
q = w([i(s(n)[x]) for x in e])
print(p - q)