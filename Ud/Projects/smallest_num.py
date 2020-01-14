'''
NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " % i))
    NumList.append(value)

smallest = NumList[0]
for j in range(1, Number):
    if(smallest > NumList[j]):
        smallest = NumList[j]
        position = j

print("The Smallest Element in this List is : ", smallest)
print("The Index position of the Smallest Element is : ", position)

'''


def smallest(list1):
    smallest = None
    
    for value in list1:
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value
    
    return smallest

    print(value)
laist1 = [23, 45, 7, 90, 6757, 0,32, 56]
print(smallest(laist1))

'''

small = None
list1 = [23, 45, 7, 90, 6757, 32, 56]
for value in [23, 45, 7, 90, 6757, 32, 56]:
    if small is None:
        small = value
    elif value < small:
        small = value
print(small)
'''

