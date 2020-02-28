""" Convert string to 1337 code"""

s = input()
a={'O':'0','L':'1','Z':'2','E':'3','A':'4','S':'5','G':'6','T':'7','B':'8','Q':'9'}
for i in a.keys():
    if i in s:
        s = s.replace(i, a[i])
    if i.lower() in s.lower():
        s = s.replace(i.lower(), a[i])
print(s)