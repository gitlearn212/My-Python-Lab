# Calculate the some of three given number
# if the given numbers(all 3 number) are same than trice the value


def sum_trice(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    return sum


# num = input("enter a numbe: ")
# num2 = int(input("enter a numbe: "))
# num3 = int(input("enter a numbe: "))
# print(trice(num, num2, num3))
print(sum_trice(1, 2, 3))
# this answer is 7(unless all three numbers are same, the cal will be addition)
print(sum_trice(1, 3, 3))
# this answwer is 27
print(sum_trice(1, 1, 1))
