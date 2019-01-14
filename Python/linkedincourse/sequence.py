# list is a mutable function so value can be re assigned but in tuple the value is not re assignable.Tuple is immutable
x = [1, 2, 3, 4, 5]
for i in x:
    #or print(i, end= ' ', flush=True)
    # or print(f'{i}',end= ' ')
    print('i is {}'.format(i),end = ' ')

# ====>Re assigning the value of list x <=======
x = [1, 2, 3, 4, 5]
x[2] = 43 # Here is how to re-assign the third number 3 to 43
for i in x:
    #or print(i, end= ' ', flush=True)
    # or print(f'{i}',end= ' ')
    print('i is {}'.format(i))

# ====>Re assigning the value in tuple x # prodeces an erro tuple Object does not support iteam assignment <=======
# To run remove the x[2]=43 line
x = (1, 2, 3, 4, 5)  # Tuple uses ( )
# x[2] = 43 # When re-assigning the third number 3 to 43 the statement produces an error because Tuple is Immutable ( Values are constant and the y do not change)
for i in x:
    #or print(i, end= ' ', flush=True)
    # or print(f'{i}',end= ' ')
    print('i is {}'.format(i))
# THIS TUPLE Or use range ins tead tuple ( range is also immutable values can not be changed)
x in range(5)
for i in x:
    #or print(i, end= ' ', flush=True)
    # or print(f'{i}',end= ' ')
    print('i is {}'.format(i))

# To change the tuple (range) to mutable(list) add x = list(range) this will chage the immutable tuple to list
# For examble
x = list(range(5))
x[2] = 45
for i in x:
    #or print(i, end= ' ', flush=True)
    # or print(f'{i}',end= ' ')
    print('i is {}'.format(i))
