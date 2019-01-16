# Boolean operators
'''
and     ==> And
or      ==> OR
not     ==> NOT
in      ==> Value in set
not in  ==> Value not in set
is      ==> Same object Identity
is not  ==> Not same object Identity
 '''
# Try this exercise below
'''
a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
if not b:
    print('expression is True')
else:
    print('expression is False')

a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
if a is b:
    print('expression is True')
else:
    print('expression is False')


a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
if a is not b:
    print('expression is True')
else:
    print('expression is False')
'''

# Try another execise 2
'''
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
if y in x:
    print('expression is True')
else:
    print('expression is False')
'''
# Try another execise 3 chars are cse sensitive
'''
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
if 'leaf'in x:      # This will be False because we do not have Leafe in x listS
    print('expression is True')
else:
    print('expression is False')
'''

# Try another execise 3 try [0]
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
if y is x[0]:      # This will be True because the value in y is in the list (tuple) x[0] is bear in x . changing the value in x[0] will esult in False in this exercise
    print('expression is True')
else:
    print('expression is False')


