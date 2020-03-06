import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
l = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    l.append(list(line))

for i in range(height):
    for j in range(width):
        if l[i][j] == '0':
            res = str(j) + ' ' + str(i)
            # Check for right
            k = j
            while k < width:
                if k + 1 < width:
                    if l[i][k+1] == '0':
                        res = res + ' ' + str(k+1) + ' ' + str(i)
                        break
                k = k + 1
            if len(res) < 7:
                res = res + ' -1 -1'
            
            # Check for bottom
            t = i
            while t < height:
                if t + 1 < height:
                    if l[t+1][j] == '0':
                        res = res + ' ' + str(j) + ' ' + str(t+1)
                        break
                t = t + 1
            if len(res) < 11:
                res = res + ' -1 -1'
            print(res.strip())
