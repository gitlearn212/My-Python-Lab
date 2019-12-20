# Prints the Largest number from the given list
num = 0
number = [3, 32, 657, 89, 1, 3, 6]

for largest in number:
    if largest > num:
        num = largest
print(f'Largest number is {num}')

# Prints the smallest number from the given list
for smallest in number:
    if smallest <= num:
        num = smallest
print(f'smallest number is {num}')

# Print numbers in ascending order
number.sort()
print(f' Numbers in Ascending order {number}')

# Print numbers in descending order
number.sort(reverse=True)
print(f' Numbers in Descending order {number}')
