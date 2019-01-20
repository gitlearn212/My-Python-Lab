# Get the volume of sphere with radius 6
# So many ways of programming for this task
# check each one of them
from math import pi

'''
def volume_sphere(x):

    # x = 6.0
    result = ((4.0/3.0) * pi * (x ** 3))
    # return result
    print(result)


r = 6.0
# print(volume_sphere(r))
volume_sphere(r)

'''
# OR write a normal program with function (with out Def)
# import pi as above or assign value to pi as below
pi = 3.1415926535897931
r = 6.0
# result = ((4.0 / 3.0) * pi * (r ** 3))
# print(result)
print(f'{(4.0/3.0) * pi * (r **3)}')
