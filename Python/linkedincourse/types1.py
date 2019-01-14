

x = 'seven'.capitalize() # prins the first letter as capital .upper print all letter in capital case and lower prin all letters in lower case
x = 'seven {} {}'.format(8,9) # places  8 and 9 in the {} in order
x = 'seven {1} {0}' .format(8,9) # it swap the order as {9}{8}
x = 'seven {0:<9} {1:>2}' .format(8, 9) # {1<9} spaces to left {0>9} spaces to right
x = 'seven "{1:<9}" "{0:>2}"' .format(8, 9) # {1<9} spaces to left {0>9} spaces to right to check use "{1:<9}" and "{0:>2}"
x = 'seven "{1:<09}" "{0:>09}"' .format(8, 9) # {1<9} spaces to left {0>9} spaces to right to check use "{1:<09}" and "{0:>09} and count the digits for the space "
# or do a f for format
#a = 4
#b = 5
#x= f'seven {a} {b}'
#x= f'seven {} {}'
print("x is {}" .format(x))
print(type(x))



