# write a python program which accepts some numbers with comma seperated
# and generate a list and tuple

values = input('Enter numbers with comma-seperated: ')
'''
list = values.split(",")
tuple = tuple(list)
print('List  => ', list)
print('Tuple =>', tuple)
'''
# OR

# print('Tuple = ', tuple(values.split(",")))
# print('List  = ', list(values.split(",")))

# Or

print(f'Tuple = {tuple(values.split(","))}\nList = {list(values.split(","))}')
