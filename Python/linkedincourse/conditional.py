# Conditional statement (operation) if, else, true and false
# This conditions work like a SWITCH in other programming Languages
# This statement will print (if True) because if is True
'''
if True:
     print('if True')
elif False:
    print('elsf false')
else:
     print('Neither True')
'''
# This statement will print (elif False) because if is False and elif is True
'''
if False:
     print('if True')
elif True:
    print('elif false')
else:
     print('Neither True nor False')

'''
# This statement will print (Neither True nor False) because if and elif are false
''''
if False:
     print('if True')
elif False:
    print('elif false')
else:
     print('Neither True nor False')
'''
# This statement will print (if True) if is True and it will skip the other conditios
if True:
     print('if True')
elif True:
    print('elsf false')
else:
     print('Neither True nor False')