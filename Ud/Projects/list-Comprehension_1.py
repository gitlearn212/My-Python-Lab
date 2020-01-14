# Lsit Comprehensions
# This is the normal way
print(''' This is the normal way ====>  
my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list) ''', '\n')


my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list, '\n')


# This is the comprehension method
# which is unique to python
print(
    ''' This is the comprehension method which is unique to python ===>  my_list = [param for param in iterable]

my_list = [char for char in 'hello'] ''', '\n')


my_list = [char for char in 'hello']
print(my_list), '\n'
