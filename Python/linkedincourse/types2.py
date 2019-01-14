
# =============>This is a Normal mathematical tasks<==========
x = 7
x = 7 // 3  # rounds the number = 2 ans class int
#x = 7 / 3  # gives the floating number = 2.33333335 ans class float
#x = 7 % 3  # gives the reminder = 1 ans class int

#print("x is {}" .format(x))
#print(type(x))
# ================>This is how to add decimal accuracy vs procession<================
# x = .1 + .1 + .1 -.3 the answer is 5.551115123125783 because python doe not understand accuracy and precision to overcome do the import * from decimal
from decimal import *
x = .1 + .1 + .1 -.3
print("x is {}" .format(x))
print(type(x))
# =============>How to solve the above problem accuracy<===============
# And the type is class decimal.Decimal
# When dealing with money use this method
from decimal import *
a = Decimal('.10') # it will conver from string
b = Decimal('.30')
x = a + a + a - b
print("x is {}" .format(x))
print(type(x))



