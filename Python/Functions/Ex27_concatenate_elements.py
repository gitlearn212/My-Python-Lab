# write a program to concatenate all elements in the given list
def concatenate(list):
    result = ''
    for element in list:
        result += str(element)
    return result


count = 0
numbers = []
while count != 6:
    num = (input('Enter some numbers: '))
    numbers.append(num)
    count += 1
print(numbers)
print(concatenate(numbers))
