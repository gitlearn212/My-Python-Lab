# Count the string for the given number of times
def count_string(str, n):
    result = " "
    for x in range(n):
        result += str
    return result


strings = input('Enter a string: ')
n = int(input('Entaer a value: '))
# print(strings)
print(count_string(strings, n))
print(count_string('abc ', n))
