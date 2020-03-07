"""Create longes sequnce of 1's by flipping single bit"""

s = input()

pos_0 = []
for i in range(len(s)):
    if s[i] == '0':
        pos_0.append(i)

len_1 = []
for i in pos_0:
    b = list(s)
    b[i] = '1'
    b = ''.join(b)
    d = [len(x) for x in b.split('0')]
    len_1.append(max(d))

print(max(len_1))