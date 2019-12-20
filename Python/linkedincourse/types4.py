x = (1, 2, 3, 4, 5, 6, 7)
print("x is {}" .format(x))
print(type(x))  # prints <class 'tuple'> 

# Change valus in tuples and print
x = (1, 'two', 3.0, [4, 'four'],5)
print("x is {}" .format(x))
print(type(x))  # prints <class 'tuple'> 

# Print the element and check for the type
x = (1, 'two', 3.0, [4, 'four'],5)
print("x is {}" .format(x))
print(type(x[2]))  # prints <class 'float'> 

# Print the id and check for the id, they both are different because, they are 2 different objects
x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'],5)
print("x is {}" .format(x))
print(id(x))
print(id(y))

# Print the element with in the and id and check for the id, they both are same because the elements are the same
x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'],5)
print("x is {}".format(x))
a = 1
b = 1
print(id(x[a]))
print(id(y[b]))
if x[a] == y[b]:
    print('Yes they are same element')
else:
    print('No they are not the same element')

# Print the id and check for the id, are same for x and y they are not
# Here we are comparing the id of x and y
x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'],5)
print("x is {}".format(x))
print(id(x))
print(id(y))
if x is y:
    print('Yes they are same element')
else:
    print('No they are not the same element')

# Using isinstance
x = (1, 'two', 3.0, [4, 'four'], 5)
#y = [1, 'two', 3.0, [4, 'four'],5]
y = {1:2,3:4}
print("x is {}".format(x))
print(id(x))
print(id(y))
if isinstance(y, tuple):
    print('tuple')
elif isinstance(y, list):
    print('list')
else:
    print('Nope')


