# Write a python program to test
# weather the given number is within 100 of 1000 or 2000
# ( 100 is near 1000 or 2000)


def near_thousands(n):
    return ((abs(1000-n) <= 1000) or (abs(2000-n) <= 100))


num = int(input('Enter a number: '))
print(near_thousands(num))
