""" Check if two input strings of non-zero length are anagrams of each other"""

s1,s2 = input().split()
l,p=list,print
a,b=l(s1),l(s2)
a.sort(),b.sort()
p(1) if a == b else p(0)