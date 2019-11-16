# Write common numbers from the given 2 lists
a = [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89, 100]
b = [1, 2, 89, 3, 4, 5, 6, 7, 8, 21]
c = []


for x in b:
    if x in a:
        c.append(x)
for y in range(len(c) -1, 0, -1):
    for z in range(y):
        if c[z] > c[z + 1]:
            c[z], c[z + 1] = c[z + 1], c[z]
# OR use sort() tor sort
# c.sort()

print(c)
