
# Enter 6 random numbers to sort in ascending order
print("Sort given numbers in ascending order")
list = []
while len(list) != 6:
    num = int(input(" Enter number :"))
    if num not in list:
        list.append(num)
    for x in range(len(list)-1, 0, -1):
        for y in range(x):
            if list[y] < list[y+1]:
                list[y], list[y+1] = list[y+1], list[y]
print(list)

# Enter 6 random numbers to sort in ascending order
print("Sort given numbers in descending order")
list = []
while len(list) != 6:
    num1 = int(input(" Enter number :"))
    if num1 not in list:
        list.append(num1)
    for x in range(len(list)-1, 0, -1):
        for y in range(x):
            if list[y] > list[y+1]:
                list[y], list[y+1] = list[y+1], list[y]
print(list)
