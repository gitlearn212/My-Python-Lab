# Bool

x = 7
print("x is {}" .format(x))
#print(type(x))  # prints <class 'init'> it is an integer type one of the built in type
# Type True or False and class is bool type
# Bool type is for logical values and expression

x = False #True
print("x is {}" .format(x))
print(type(x))  # prints <class 'bool'> it is bool type

x = 7 < 5# or 7 > 5
print("x is {}" .format(x))
print(type(x))  # x is trus (7 > 5) and false (7 < 5)and the  <class 'bool'>

x = None
print("x is {}" .format(x))
print(type(x))  # x the value in None and the <class 'Nonetype'>

# === Inthe following excersise x = None or (ZERO) 0
# It will print the x value as None and the class None Type
# It will print the x value as 0 and the class int  if the value is 0 <--(ZERO)
# It will print x value is an empty string it is false and the class str
# The if statement checks for the x value. as it is none it prints the false
# If the x value is a int or float the statement will print True
# In short if the x value is empty string or None or 0 then it is False else True

x = None
print("x is {}".format(x))
print(type(x)) # x the value in None and the <class 'Nonetype'>

if x:
    print('True')
else:
    print('False')






