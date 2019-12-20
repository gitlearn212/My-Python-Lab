''' Aritmettic Operators

+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Integer Division
%   Remainder(Modulo)
**  Exponent
-   Unary negative
+   Unery positive
============================================
'''
'''x = 5
y = 3
z = x - y
print(f'result is {z}')
'''
'''# Trying with / division Division operator
# The answer is a float (1.666666666667) eventhogh the operators are integrs the answer is float this is how the / Division work in python 3 but not in python 2
x = 5
y = 3
z = x / y
print(f'result is {z}')
'''
# Trying with // Integer Division 
# The answer is a integer (1) but it will only print the first digit with out the reminder nor add the value anythin .5 to a full value (1.6 is printed as 1 and not 2)
'''x = 5
y = 3
z = x // y
print(f'result is {z}')
'''
# Trying with % modulo operator
# The answer 2 it will print only the reminder
'''x = 5
y = 3
z = x % y
print(f'result is {z}')
'''
# Trying with Unery operator
# The answer is a float (1.666666666667) eventhogh the operators are integrs the answer is float this is how the / Division work
''' x = 5
y = 3
z = x / y
z = -2  
print(f'result is {z}')  # The result is -2
'''

# Trying with Unery operator
# The answer is a float (1.666666666667) eventhogh the operators are integrs the answer is float this is how the / Division work
'''
x = 5
y = 3
z = x / y
z = +2  
print(f'result is {z}')  # The result is 2
'''
# Trying with Unery operator
# The answer is a float (1.666666666667) eventhogh the operators are integrs the answer is float this is how the / Division work
x = 5
y = 3
z = x / y
z = -2
z = +z # if z = -z then the result is 2
print(f'result is {z}') # The result is -2
