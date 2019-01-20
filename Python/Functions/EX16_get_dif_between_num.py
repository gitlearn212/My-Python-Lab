# Write a program to get the difference between the given number and 17
# if the given number is greater than 17
# Double the absolute difference
'''
num = int(input("enter a number :"))
if num <= 17:
    print(num-17)
else:
    print((num-17)*2)
'''


def difference(x):
    if x <= 17:
        return(x - 17)
    else:
        return((x - 17) * 2)


num = int(input('Enter a number: '))
print(difference(num))
