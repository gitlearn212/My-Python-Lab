# Check if the specified value is in the group
def is_group(number):
    group = [1, 4, 6, 8, ]
    # return number in group
    if number in group:
        print(f'Number {number} is in the group {group}')
    else:
        print(f'Number {number} is not in the group {group}')


num = int(input('enter a number: '))
is_group(num)
