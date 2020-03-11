""" Print the sum of numbers corresponding to strings containing the search term"""

n = int(input())
z = []
for i in range(n):
    city, population = input().split()
    population = int(population)
    z.append((city, population))
search = input()

r = 0
for i in z:
    if search in i[0]:
        r = r + i[1]

print(r)