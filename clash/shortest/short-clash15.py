""" Print the input string in alternating upper and lowercase"""

import string
s = input()
t = 0
r=''
for i in s:
    if i.lower() not in string.ascii_lowercase:
        r = r + i
        continue
    if t == 0:
        r = r + i.upper()
        t = 1
    else:
        r = r + i.lower()
        t = 0
print(r)