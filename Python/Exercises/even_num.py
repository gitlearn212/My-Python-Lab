'''
Using the given list 'a' , write a list that has only even numbers
Try this with for loop and write a code in one line

'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# <=========== ONE LINE CODE ============>
# b = [element for element in a if element % 2 == 0]
# print(b)
# <========== FOR LOOP =================>
for i in list((a)):
    if i % 2 == 0:
        print(i)
b = [test for test in a if test % 2 == 0]
print(b)
